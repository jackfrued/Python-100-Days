import { notFound } from "next/navigation";
import { getLesson, getLessons, getQuestionsForDay } from "@/lib/data";
import { CodingRunner } from "@/components/CodingRunner";

export function generateStaticParams() {
  return getLessons().map((l) => ({ slug: l.slug }));
}

export default function PracticeQuizPage({ params }: { params: { slug: string } }) {
  const lesson = getLesson(params.slug);
  if (!lesson) notFound();

  const questions = getQuestionsForDay(lesson.day);

  return (
    <CodingRunner
      slug={lesson.slug}
      day={lesson.day}
      titleCn={lesson.titleCn}
      titleEn={lesson.titleEn}
      topic={lesson.topic}
      questions={questions}
    />
  );
}
