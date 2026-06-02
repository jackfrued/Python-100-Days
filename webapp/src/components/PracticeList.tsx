"use client";

import Link from "next/link";
import { useLang } from "@/lib/lang-context";
import { topicMeta } from "@/lib/data";
import type { Topic } from "@/lib/types";

interface Item {
  slug: string;
  day: number;
  titleCn: string;
  titleEn: string;
  topic: Topic;
  questionCount: number;
  estMinutes: number;
}

export function PracticeList({ items }: { items: Item[] }) {
  const { t, lang } = useLang();

  return (
    <div className="mx-auto max-w-5xl px-4 py-10">
      <h1 className="text-2xl font-bold text-slate-900">{t("practiceTitle")}</h1>
      <p className="mt-1 text-slate-600">{t("practiceSub")}</p>

      <div className="mt-8 grid gap-3 sm:grid-cols-2">
        {items.map((l) => {
          const tm = topicMeta(l.topic);
          return (
            <Link
              key={l.slug}
              href={`/practice/${l.slug}`}
              className="group rounded-xl border border-slate-200 bg-white p-4 transition hover:border-emerald-300 hover:shadow-sm"
            >
              <div className="flex items-center gap-2">
                <span className={`rounded-full px-2.5 py-0.5 text-xs font-semibold ${tm.color}`}>
                  {lang === "cn" ? tm.cn : tm.en}
                </span>
                <span className="text-xs text-slate-400">
                  {t("day")}
                  {l.day}
                  {t("dayUnit")}
                </span>
              </div>
              <h3 className="mt-2 font-semibold text-slate-900 group-hover:text-emerald-700">
                {lang === "cn" ? l.titleCn : l.titleEn}
              </h3>
              <div className="mt-3 flex items-center gap-3 text-xs text-slate-500">
                <span>
                  {l.questionCount} {t("questions")}
                </span>
                <span>·</span>
                <span>
                  {t("estMinutes")}
                  {l.estMinutes} {t("minutes")}
                </span>
              </div>
            </Link>
          );
        })}
      </div>

      {items.length === 0 && (
        <p className="mt-12 text-center text-slate-400">{t("noQuestions")}</p>
      )}
    </div>
  );
}
