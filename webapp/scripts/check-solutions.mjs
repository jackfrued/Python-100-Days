// End-to-end verification of the coding bank against a real python3:
//   - solution + tests  MUST pass (exit 0)
//   - starter  + tests  MUST fail (the stub shouldn't already satisfy the tests)
// Mirrors what the in-browser Pyodide runner does.
import { readFileSync, mkdtempSync, writeFileSync, rmSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { tmpdir } from "node:os";
import { join } from "node:path";

const bank = JSON.parse(
  readFileSync(new URL("../src/content/questions.json", import.meta.url), "utf8")
);

const dir = mkdtempSync(join(tmpdir(), "py100-check-"));
let checked = 0;
const problems = [];

function run(code) {
  const f = join(dir, "snippet.py");
  writeFileSync(f, code, "utf8");
  try {
    execFileSync("python3", [f], { encoding: "utf8", timeout: 8000, stdio: ["ignore", "pipe", "pipe"] });
    return { ok: true };
  } catch (e) {
    return { ok: false, err: String(e.stderr || e.message).split("\n").slice(-4).join(" ").trim() };
  }
}

for (const lesson of bank.lessons) {
  for (const q of lesson.questions) {
    checked++;
    const loc = `day${lesson.day}/${q.id}`;
    const sol = run(`${q.solution}\n\n${q.tests}\n`);
    if (!sol.ok) problems.push({ loc, kind: "SOLUTION FAILS TESTS", detail: sol.err });
    const stub = run(`${q.starter}\n\n${q.tests}\n`);
    if (stub.ok) problems.push({ loc, kind: "STARTER ALREADY PASSES", detail: "stub satisfies tests — exercise is trivial/broken" });
  }
}

rmSync(dir, { recursive: true, force: true });

console.log(`Ran solution+starter against tests for ${checked} exercises via python3.`);
if (problems.length) {
  console.log(`\n${problems.length} need review:`);
  for (const p of problems) {
    console.log(`\n[${p.kind}] ${p.loc}`);
    console.log("  " + p.detail);
  }
  process.exit(1);
} else {
  console.log("All solutions pass and all starters fail ✓");
}
