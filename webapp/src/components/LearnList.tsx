"use client";

import Link from "next/link";
import { useLang } from "@/lib/lang-context";
import { TOPICS, topicMeta } from "@/lib/data";
import type { Lesson } from "@/lib/types";

type LessonWithCount = Lesson & { questionCount: number };

export function LearnList({ lessons }: { lessons: LessonWithCount[] }) {
  const { t, lang } = useLang();

  const byTopic = TOPICS.map((topic) => ({
    topic,
    items: lessons.filter((l) => l.topic === topic.id),
  })).filter((g) => g.items.length > 0);

  return (
    <div className="mx-auto max-w-5xl px-4 py-10">
      <h1 className="text-2xl font-bold text-slate-900">{t("learnTitle")}</h1>
      <p className="mt-1 text-slate-600">{t("learnSub")}</p>

      <div className="mt-8 space-y-10">
        {byTopic.map(({ topic, items }) => (
          <section key={topic.id}>
            <div className="mb-3 flex items-center gap-2">
              <span className={`rounded-full px-3 py-1 text-xs font-semibold ${topic.color}`}>
                {lang === "cn" ? topic.cn : topic.en}
              </span>
              <span className="text-sm text-slate-400">
                {items.length} {lang === "cn" ? "课" : "lessons"}
              </span>
            </div>
            <div className="grid gap-3 sm:grid-cols-2">
              {items.map((l) => (
                <Link
                  key={l.slug}
                  href={`/learn/${l.slug}`}
                  className="group rounded-xl border border-slate-200 bg-white p-4 transition hover:border-blue-300 hover:shadow-sm"
                >
                  <div className="flex items-start justify-between gap-3">
                    <div>
                      <div className="text-xs font-medium text-slate-400">
                        {t("day")}
                        {l.day}
                        {t("dayUnit")}
                      </div>
                      <h3 className="mt-0.5 font-semibold text-slate-900 group-hover:text-blue-600">
                        {lang === "cn" ? l.titleCn : l.titleEn}
                      </h3>
                    </div>
                  </div>
                  <div className="mt-3 flex items-center gap-3 text-xs text-slate-500">
                    <span>
                      {l.readMinutes} {t("minutesRead")}
                    </span>
                    {l.questionCount > 0 && (
                      <span className="text-emerald-600">
                        {l.questionCount} {t("questions")}
                      </span>
                    )}
                  </div>
                </Link>
              ))}
            </div>
          </section>
        ))}
      </div>
    </div>
  );
}
