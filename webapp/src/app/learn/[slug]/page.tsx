import { notFound } from "next/navigation";
import { getLesson, getLessons, getQuestionCount } from "@/lib/data";
import { Markdown } from "@/lib/markdown";
import { LessonHeader } from "@/components/LessonHeader";

export function generateStaticParams() {
  return getLessons().map((l) => ({ slug: l.slug }));
}

export default function LessonPage({ params }: { params: { slug: string } }) {
  const lesson = getLesson(params.slug);
  if (!lesson) notFound();

  const questionCount = getQuestionCount(lesson.day);

  // Strip the first heading from the body — we render our own bilingual title.
  const body = lesson.markdown.replace(/^#{1,3}\s+.*\n/, "");

  return (
    <article className="mx-auto max-w-3xl px-4 py-10">
      <LessonHeader
        day={lesson.day}
        slug={lesson.slug}
        titleCn={lesson.titleCn}
        titleEn={lesson.titleEn}
        topic={lesson.topic}
        readMinutes={lesson.readMinutes}
        questionCount={questionCount}
      />
      <div className="mt-8">
        <Markdown source={body} />
      </div>
      <LessonHeader
        day={lesson.day}
        slug={lesson.slug}
        titleCn={lesson.titleCn}
        titleEn={lesson.titleEn}
        topic={lesson.topic}
        readMinutes={lesson.readMinutes}
        questionCount={questionCount}
        footer
      />
    </article>
  );
}
