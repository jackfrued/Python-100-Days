"use client";

import { useMemo, useState } from "react";
import Link from "next/link";
import { useLang } from "@/lib/lang-context";
import { topicMeta } from "@/lib/data";
import { runTests, getPyodide, type RunResult } from "@/lib/pyodide-runner";
import { Markdown } from "@/lib/markdown";
import { CodeEditor } from "@/components/CodeEditor";
import type { CodingQuestion, Topic } from "@/lib/types";

interface Props {
  slug: string;
  day: number;
  titleCn: string;
  titleEn: string;
  topic: Topic;
  questions: CodingQuestion[];
}

export function CodingRunner({ slug, day, titleCn, titleEn, topic, questions }: Props) {
  const { t, lang } = useLang();
  const tm = topicMeta(topic);

  const [order, setOrder] = useState<number[]>(() => questions.map((_, i) => i));
  const [idx, setIdx] = useState(0);
  const [phase, setPhase] = useState<"quiz" | "result">("quiz");

  // per-question editor state, keyed by id
  const [code, setCode] = useState<Record<string, string>>({});
  const [result, setResult] = useState<Record<string, RunResult | undefined>>({});
  const [solved, setSolved] = useState<Record<string, boolean>>({});
  const [showHint, setShowHint] = useState<Record<string, boolean>>({});
  const [showSol, setShowSol] = useState<Record<string, boolean>>({});

  const [busy, setBusy] = useState(false);
  const [loadingRuntime, setLoadingRuntime] = useState(false);
  const [loadError, setLoadError] = useState(false);

  const estMinutes = useMemo(
    () => questions.reduce((s, q) => s + (q.estMinutes || 4), 0),
    [questions]
  );

  if (questions.length === 0) {
    return (
      <div className="mx-auto max-w-2xl px-4 py-16 text-center">
        <p className="text-slate-500">{t("noQuestions")}</p>
        <Link href="/practice" className="mt-4 inline-block text-blue-600 hover:underline">
          {t("backToPractice")}
        </Link>
      </div>
    );
  }

  const q = questions[order[idx]];
  const total = order.length;
  const editorValue = code[q.id] ?? q.starter;
  const res = result[q.id];
  const solvedCount = order.filter((qi) => solved[questions[qi].id]).length;

  async function onRun() {
    setBusy(true);
    setLoadError(false);
    try {
      // warm the runtime (shows the "loading" hint only the first time)
      setLoadingRuntime(true);
      await getPyodide();
      setLoadingRuntime(false);
      const r = await runTests(editorValue, q.tests);
      setResult((m) => ({ ...m, [q.id]: r }));
      if (r.ok) setSolved((m) => ({ ...m, [q.id]: true }));
    } catch {
      setLoadError(true);
    } finally {
      setLoadingRuntime(false);
      setBusy(false);
    }
  }

  function reset() {
    setCode((m) => ({ ...m, [q.id]: q.starter }));
    setResult((m) => ({ ...m, [q.id]: undefined }));
  }

  function next() {
    if (idx + 1 >= total) return setPhase("result");
    setIdx(idx + 1);
  }

  function restart(unsolvedOnly = false) {
    const base = questions.map((_, i) => i);
    const ord = unsolvedOnly ? base.filter((i) => !solved[questions[i].id]) : base;
    setOrder(ord.length ? ord : base);
    setIdx(0);
    setResult({});
    setShowSol({});
    if (!unsolvedOnly) {
      setCode({});
      setSolved({});
    }
    setPhase("quiz");
  }

  // ---- Result screen ----
  if (phase === "result") {
    const msg =
      solvedCount === total ? t("allSolved") : solvedCount > 0 ? t("someSolved") : t("fewSolved");
    const unsolved = order.filter((qi) => !solved[questions[qi].id]);
    return (
      <div className="mx-auto max-w-2xl px-4 py-12">
        <div className="rounded-2xl border border-slate-200 bg-white p-8 text-center shadow-sm">
          <div className="text-sm font-medium text-slate-400">{t("yourResult")}</div>
          <div className="mt-2 text-5xl font-extrabold text-slate-900">
            {solvedCount}
            <span className="text-2xl text-slate-400"> / {total}</span>
          </div>
          <p className="mt-3 text-slate-600">{msg}</p>
          <div className="mt-6 flex flex-wrap justify-center gap-3">
            <button
              onClick={() => restart(false)}
              className="rounded-lg bg-emerald-600 px-5 py-2 text-sm font-semibold text-white hover:bg-emerald-700"
            >
              {t("retry")}
            </button>
            {unsolved.length > 0 && (
              <button
                onClick={() => restart(true)}
                className="rounded-lg border border-amber-300 bg-amber-50 px-5 py-2 text-sm font-semibold text-amber-700 hover:bg-amber-100"
              >
                {t("retryUnsolved")} ({unsolved.length})
              </button>
            )}
            <Link
              href="/practice"
              className="rounded-lg border border-slate-300 px-5 py-2 text-sm font-semibold text-slate-600 hover:bg-slate-100"
            >
              {t("allLessons")}
            </Link>
          </div>
        </div>
      </div>
    );
  }

  // ---- Quiz screen ----
  const progress = Math.round(((idx + (solved[q.id] ? 1 : 0)) / total) * 100);

  return (
    <div className="mx-auto max-w-3xl px-4 py-8">
      <div className="flex items-center justify-between">
        <Link href="/practice" className="text-sm font-medium text-slate-500 hover:text-slate-800">
          {t("backToPractice")}
        </Link>
        <div className="flex items-center gap-2 text-xs text-slate-400">
          <span className={`rounded-full px-2.5 py-0.5 font-semibold ${tm.color}`}>
            {lang === "cn" ? tm.cn : tm.en}
          </span>
          <span>
            {t("day")}
            {day}
            {t("dayUnit")}
          </span>
        </div>
      </div>

      <h1 className="mt-2 text-lg font-bold text-slate-900">{lang === "cn" ? titleCn : titleEn}</h1>
      <p className="text-xs text-slate-400">
        {t("estTime")}: {t("estMinutes")}
        {estMinutes} {t("minutes")} · {solvedCount}/{total} {t("solved")}
      </p>

      <div className="mt-4 h-2 w-full overflow-hidden rounded-full bg-slate-200">
        <div className="h-full rounded-full bg-emerald-500 transition-all" style={{ width: `${progress}%` }} />
      </div>
      <div className="mt-2 flex items-center justify-between text-xs text-slate-400">
        <span>
          {t("question")} {idx + 1} {t("questionUnit")} {t("of")} {total}
        </span>
        <DifficultyTag difficulty={q.difficulty} />
      </div>

      {/* prompt */}
      <div className="mt-4 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
        <div className="flex items-center gap-2">
          <h2 className="font-bold text-slate-900">{lang === "cn" ? q.title_cn : q.title_en}</h2>
          {solved[q.id] && (
            <span className="rounded-full bg-emerald-100 px-2 py-0.5 text-xs font-semibold text-emerald-700">
              ✓ {t("solved")}
            </span>
          )}
        </div>
        <div className="mt-2 text-sm">
          <Markdown source={lang === "cn" ? q.prompt_cn : q.prompt_en} />
        </div>

        {/* editor */}
        <div className="mt-4">
          <CodeEditor value={editorValue} onChange={(v) => setCode((m) => ({ ...m, [q.id]: v }))} disabled={busy} />
        </div>

        {/* actions */}
        <div className="mt-3 flex flex-wrap items-center gap-2">
          <button
            onClick={onRun}
            disabled={busy}
            className="rounded-lg bg-blue-600 px-5 py-2 text-sm font-semibold text-white transition enabled:hover:bg-blue-700 disabled:opacity-50"
          >
            {busy ? t("running") : "▶ " + t("run")}
          </button>
          <button
            onClick={reset}
            disabled={busy}
            className="rounded-lg border border-slate-300 px-4 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100 disabled:opacity-50"
          >
            {t("reset")}
          </button>
          {(q.hint_cn || q.hint_en) && (
            <button
              onClick={() => setShowHint((m) => ({ ...m, [q.id]: !m[q.id] }))}
              className="rounded-lg px-3 py-2 text-sm font-medium text-amber-700 hover:bg-amber-50"
            >
              💡 {t("showHint")}
            </button>
          )}
          <button
            onClick={() => setShowSol((m) => ({ ...m, [q.id]: !m[q.id] }))}
            className="rounded-lg px-3 py-2 text-sm font-medium text-slate-500 hover:bg-slate-100"
          >
            {t("showSolution")}
          </button>
          <div className="ml-auto">
            <button
              onClick={next}
              className="rounded-lg bg-slate-900 px-5 py-2 text-sm font-semibold text-white hover:bg-slate-700"
            >
              {idx + 1 >= total ? t("finish") : t("next")} →
            </button>
          </div>
        </div>

        {loadingRuntime && <p className="mt-3 text-xs text-slate-400">{t("loadingRuntime")}</p>}
        {loadError && <p className="mt-3 text-sm text-rose-600">{t("loadRuntimeFailed")}</p>}

        {/* hint */}
        {showHint[q.id] && (q.hint_cn || q.hint_en) && (
          <div className="mt-3 rounded-xl bg-amber-50 p-3 text-sm text-amber-800">
            <span className="font-semibold">{t("hint")}: </span>
            {lang === "cn" ? q.hint_cn : q.hint_en}
          </div>
        )}

        {/* result */}
        {res && <ResultPanel res={res} />}

        {/* solution */}
        {showSol[q.id] && (
          <div className="mt-3">
            <div className="mb-1 text-xs font-semibold text-slate-500">{t("solution")}</div>
            <pre className="overflow-x-auto rounded-xl bg-slate-900 p-4 text-sm text-slate-100">
              <code className="font-mono">{q.solution}</code>
            </pre>
          </div>
        )}
      </div>
    </div>
  );
}

function ResultPanel({ res }: { res: RunResult }) {
  const { t } = useLang();
  if (res.error) {
    return (
      <div className="mt-4 rounded-xl bg-rose-50 p-4 text-sm">
        <div className="font-semibold text-rose-800">✗ {t("runtimeError")}</div>
        <pre className="mt-2 overflow-x-auto whitespace-pre-wrap rounded-lg bg-rose-100/60 p-3 font-mono text-xs text-rose-900">
          {res.error.trim()}
        </pre>
      </div>
    );
  }
  if (res.ok) {
    return (
      <div className="mt-4 rounded-xl bg-emerald-50 p-4 text-sm">
        <div className="font-semibold text-emerald-800">
          ✓ {t("testsPassed")} ({res.passed}/{res.total} {t("cases")})
        </div>
        {res.stdout.trim() && <OutputBlock stdout={res.stdout} />}
      </div>
    );
  }
  return (
    <div className="mt-4 rounded-xl bg-rose-50 p-4 text-sm">
      <div className="font-semibold text-rose-800">
        ✗ {t("testsFailed")} — {res.passed}/{res.total} {t("passedOf")}
      </div>
      {res.failures.length > 0 && (
        <div className="mt-2 space-y-1">
          <div className="text-xs font-medium text-rose-700">{t("failedCase")}:</div>
          {res.failures.map((f, i) => (
            <pre
              key={i}
              className="overflow-x-auto whitespace-pre-wrap rounded-lg bg-rose-100/60 p-2 font-mono text-xs text-rose-900"
            >
              #{f.index}: {f.message}
            </pre>
          ))}
        </div>
      )}
      {res.stdout.trim() && <OutputBlock stdout={res.stdout} />}
    </div>
  );
}

function OutputBlock({ stdout }: { stdout: string }) {
  const { t } = useLang();
  return (
    <div className="mt-2">
      <div className="text-xs font-medium text-slate-500">{t("output")}:</div>
      <pre className="mt-1 overflow-x-auto rounded-lg bg-slate-800 p-2 font-mono text-xs text-slate-100">
        {stdout.replace(/\n+$/, "")}
      </pre>
    </div>
  );
}

function DifficultyTag({ difficulty }: { difficulty: CodingQuestion["difficulty"] }) {
  const { t } = useLang();
  const map = {
    easy: { label: t("easy"), cls: "text-emerald-600" },
    medium: { label: t("medium"), cls: "text-amber-600" },
    hard: { label: t("hard"), cls: "text-rose-600" },
  } as const;
  const m = map[difficulty];
  return (
    <span className={m.cls}>
      {t("difficulty")}: {m.label}
    </span>
  );
}
