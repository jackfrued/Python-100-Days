"use client";

// Loads the self-hosted Pyodide runtime (public/pyodide) once and runs user
// code against hidden assert tests entirely in the browser. No backend, no CDN.

type PyodideAPI = {
  runPythonAsync: (code: string) => Promise<unknown>;
  globals: { get: (k: string) => unknown };
  setStdout: (opts: { batched: (s: string) => void }) => void;
  setStderr: (opts: { batched: (s: string) => void }) => void;
};

declare global {
  interface Window {
    loadPyodide?: (opts: { indexURL: string }) => Promise<PyodideAPI>;
    __pyodide?: Promise<PyodideAPI>;
  }
}

const INDEX_URL = "/pyodide/";

function loadScriptOnce(src: string): Promise<void> {
  return new Promise((resolve, reject) => {
    if (document.querySelector(`script[data-pyodide]`)) return resolve();
    const s = document.createElement("script");
    s.src = src;
    s.async = true;
    s.dataset.pyodide = "1";
    s.onload = () => resolve();
    s.onerror = () => reject(new Error("Failed to load pyodide.js"));
    document.head.appendChild(s);
  });
}

export function getPyodide(): Promise<PyodideAPI> {
  if (typeof window === "undefined") {
    return Promise.reject(new Error("Pyodide only runs in the browser"));
  }
  if (!window.__pyodide) {
    window.__pyodide = (async () => {
      await loadScriptOnce(`${INDEX_URL}pyodide.js`);
      if (!window.loadPyodide) throw new Error("loadPyodide not found");
      return window.loadPyodide({ indexURL: INDEX_URL });
    })();
  }
  return window.__pyodide;
}

export interface RunResult {
  ok: boolean;
  // structured outcome
  passed: number;
  total: number;
  stdout: string;
  error?: string; // syntax/runtime error in the user's code (not an assert failure)
  failures: { index: number; message: string }[]; // failed asserts
}

// Harness that runs user code, then executes each assert line individually so
// we can report which checks passed/failed without leaking the others.
function buildHarness(userCode: string, tests: string): string {
  // Base64-encode payloads (UTF-8 safe) to avoid any quoting/escaping issues.
  const b64 = (s: string) => {
    const bytes = new TextEncoder().encode(s);
    let bin = "";
    bytes.forEach((b) => (bin += String.fromCharCode(b)));
    return btoa(bin);
  };

  return `
import json, base64, traceback, io, contextlib

_user = base64.b64decode("${b64(userCode)}").decode("utf-8")
_tests_src = base64.b64decode("${b64(tests)}").decode("utf-8")

_result = {"ok": False, "passed": 0, "total": 0, "stdout": "", "error": None, "failures": []}
_ns = {}
_buf = io.StringIO()

try:
    with contextlib.redirect_stdout(_buf):
        exec(_user, _ns)
except Exception:
    _result["error"] = traceback.format_exc(limit=3)
    _result["stdout"] = _buf.getvalue()
    print(json.dumps(_result))
else:
    # split tests into top-level statements; run asserts one at a time
    import ast
    try:
        _tree = ast.parse(_tests_src)
    except SyntaxError:
        _result["error"] = "Invalid test source"
        print(json.dumps(_result))
    else:
        _stmts = _tree.body
        _result["total"] = sum(1 for s in _stmts if isinstance(s, ast.Assert))
        _idx = 0
        _aborted = False
        with contextlib.redirect_stdout(_buf):
            for _s in _stmts:
                _code = ast.Module(body=[_s], type_ignores=[])
                _src = ast.unparse(_s)
                try:
                    exec(compile(_code, "<test>", "exec"), _ns)
                    if isinstance(_s, ast.Assert):
                        _result["passed"] += 1
                        _idx += 1
                except AssertionError as e:
                    if isinstance(_s, ast.Assert):
                        _idx += 1
                        msg = str(e) if str(e) else _src
                        _result["failures"].append({"index": _idx, "message": msg})
                except Exception:
                    _result["failures"].append({"index": _idx + 1, "message": traceback.format_exc(limit=2)})
                    _aborted = True
                    break
        _result["stdout"] = _buf.getvalue()
        _result["ok"] = (len(_result["failures"]) == 0 and not _aborted and _result["total"] > 0)
        print(json.dumps(_result))
`;
}

export async function runTests(userCode: string, tests: string): Promise<RunResult> {
  const py = await getPyodide();
  let captured = "";
  py.setStdout({ batched: (s) => (captured += s) });
  py.setStderr({ batched: () => {} });
  await py.runPythonAsync(buildHarness(userCode, tests));
  // The harness prints exactly one JSON line as its last output.
  const line = captured.trim().split("\n").filter(Boolean).pop() || "{}";
  try {
    return JSON.parse(line) as RunResult;
  } catch {
    return {
      ok: false,
      passed: 0,
      total: 0,
      stdout: captured,
      error: "Runner failed to produce a result.",
      failures: [],
    };
  }
}
