"use client";

import { useRef } from "react";

// Minimal, dependency-free code editor: a monospace textarea with Tab→spaces,
// auto-indent on newline, and a gutter of line numbers. Good enough for short
// exercises and avoids shipping a multi-hundred-KB editor library.
export function CodeEditor({
  value,
  onChange,
  disabled,
}: {
  value: string;
  onChange: (v: string) => void;
  disabled?: boolean;
}) {
  const ref = useRef<HTMLTextAreaElement>(null);
  const lineCount = value.split("\n").length;

  function handleKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    const ta = e.currentTarget;
    const { selectionStart: s, selectionEnd: end } = ta;

    if (e.key === "Tab") {
      e.preventDefault();
      const insert = "    ";
      const next = value.slice(0, s) + insert + value.slice(end);
      onChange(next);
      requestAnimationFrame(() => {
        ta.selectionStart = ta.selectionEnd = s + insert.length;
      });
      return;
    }

    if (e.key === "Enter") {
      // auto-indent: copy leading whitespace of current line, add 4 after ':'
      const lineStart = value.lastIndexOf("\n", s - 1) + 1;
      const curLine = value.slice(lineStart, s);
      const indentMatch = curLine.match(/^[ \t]*/);
      let indent = indentMatch ? indentMatch[0] : "";
      if (/:\s*$/.test(curLine)) indent += "    ";
      if (indent) {
        e.preventDefault();
        const next = value.slice(0, s) + "\n" + indent + value.slice(end);
        onChange(next);
        requestAnimationFrame(() => {
          ta.selectionStart = ta.selectionEnd = s + 1 + indent.length;
        });
      }
    }
  }

  return (
    <div className="flex overflow-hidden rounded-xl border border-slate-700 bg-slate-900 font-mono text-sm">
      <div
        aria-hidden
        className="select-none whitespace-pre py-3 pl-3 pr-2 text-right text-slate-600"
        style={{ minWidth: "2.5rem" }}
      >
        {Array.from({ length: lineCount }, (_, i) => i + 1).join("\n")}
      </div>
      <textarea
        ref={ref}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        onKeyDown={handleKeyDown}
        disabled={disabled}
        spellCheck={false}
        autoCapitalize="off"
        autoCorrect="off"
        wrap="off"
        rows={Math.max(8, lineCount + 1)}
        className="flex-1 resize-none overflow-auto bg-transparent py-3 pr-3 leading-6 text-slate-100 outline-none disabled:opacity-70"
        style={{ tabSize: 4 }}
      />
    </div>
  );
}
