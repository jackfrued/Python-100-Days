"use client";

import Link from "next/link";
import { useLang } from "@/lib/lang-context";

export function HomeView({
  lessonCount,
  questionCount,
}: {
  lessonCount: number;
  questionCount: number;
}) {
  const { t, lang } = useLang();

  return (
    <div className="mx-auto max-w-5xl px-4 py-12">
      {/* Hero */}
      <section className="text-center">
        <h1 className="text-3xl font-extrabold tracking-tight text-slate-900 sm:text-4xl">
          {t("appName")}
        </h1>
        <p className="mx-auto mt-4 max-w-2xl text-lg text-slate-600">
          {t("tagline")}
        </p>
        <div className="mt-6 flex items-center justify-center gap-6 text-sm text-slate-500">
          <span>
            <b className="text-slate-900">{lessonCount}</b> {t("totalLessons")}
          </span>
          <span className="h-4 w-px bg-slate-300" />
          <span>
            <b className="text-slate-900">{questionCount}</b> {t("totalQuestions")}
          </span>
        </div>
      </section>

      {/* Two sectors */}
      <section className="mt-12 grid gap-6 sm:grid-cols-2">
        <Link
          href="/learn"
          className="group rounded-2xl border border-slate-200 bg-white p-8 shadow-sm transition hover:-translate-y-0.5 hover:border-blue-300 hover:shadow-md"
        >
          <div className="mb-4 grid h-12 w-12 place-items-center rounded-xl bg-blue-100 text-2xl">
            📖
          </div>
          <h2 className="text-xl font-bold text-slate-900">{t("learnTitle")}</h2>
          <p className="mt-2 text-slate-600">{t("learnSub")}</p>
          <span className="mt-5 inline-flex items-center font-semibold text-blue-600 group-hover:gap-1">
            {t("startLearning")} →
          </span>
        </Link>

        <Link
          href="/practice"
          className="group rounded-2xl border border-slate-200 bg-white p-8 shadow-sm transition hover:-translate-y-0.5 hover:border-emerald-300 hover:shadow-md"
        >
          <div className="mb-4 grid h-12 w-12 place-items-center rounded-xl bg-emerald-100 text-2xl">
            ✏️
          </div>
          <h2 className="text-xl font-bold text-slate-900">{t("practiceTitle")}</h2>
          <p className="mt-2 text-slate-600">{t("practiceSub")}</p>
          <span className="mt-5 inline-flex items-center font-semibold text-emerald-600 group-hover:gap-1">
            {t("startPracticing")} →
          </span>
        </Link>
      </section>

      <p className="mt-10 text-center text-sm text-slate-400">
        {lang === "cn"
          ? "建议：先读讲义，再做对应练习，每个练习控制在 20 分钟内。"
          : "Tip: read the notes, then drill the matching practice — each set under 20 minutes."}
      </p>
    </div>
  );
}
