"use client";

import Link from "next/link";
import { useLang } from "@/lib/lang-context";
import { topicMeta } from "@/lib/data";
import type { Topic } from "@/lib/types";

export function LessonHeader({
  day,
  slug,
  titleCn,
  titleEn,
  topic,
  readMinutes,
  questionCount,
  footer = false,
}: {
  day: number;
  slug: string;
  titleCn: string;
  titleEn: string;
  topic: Topic;
  readMinutes: number;
  questionCount: number;
  footer?: boolean;
}) {
  const { t, lang } = useLang();
  const tm = topicMeta(topic);

  if (footer) {
    return (
      <div className="mt-12 flex flex-wrap items-center justify-between gap-4 border-t border-slate-200 pt-6">
        <Link href="/learn" className="text-sm font-medium text-slate-500 hover:text-slate-800">
          {t("backToLessons")}
        </Link>
        {questionCount > 0 && (
          <Link
            href={`/practice/${slug}`}
            className="rounded-lg bg-emerald-600 px-4 py-2 text-sm font-semibold text-white hover:bg-emerald-700"
          >
            {t("goPractice")}
          </Link>
        )}
      </div>
    );
  }

  return (
    <header>
      <Link href="/learn" className="text-sm font-medium text-slate-500 hover:text-slate-800">
        {t("backToLessons")}
      </Link>
      <div className="mt-3 flex items-center gap-2">
        <span className={`rounded-full px-3 py-1 text-xs font-semibold ${tm.color}`}>
          {lang === "cn" ? tm.cn : tm.en}
        </span>
        <span className="text-sm text-slate-400">
          {t("day")}
          {day}
          {t("dayUnit")}
        </span>
        <span className="text-sm text-slate-400">·</span>
        <span className="text-sm text-slate-400">
          {readMinutes} {t("minutesRead")}
        </span>
      </div>
      <h1 className="mt-2 text-2xl font-extrabold text-slate-900">
        {lang === "cn" ? titleCn : titleEn}
      </h1>
      {lang === "en" && (
        <p className="mt-1 text-sm text-slate-400">{titleCn}</p>
      )}
      {questionCount > 0 && (
        <Link
          href={`/practice/${slug}`}
          className="mt-4 inline-flex items-center gap-1 rounded-lg bg-emerald-50 px-3 py-1.5 text-sm font-semibold text-emerald-700 hover:bg-emerald-100"
        >
          {t("goPractice")} · {questionCount} {t("questions")}
        </Link>
      )}
    </header>
  );
}
