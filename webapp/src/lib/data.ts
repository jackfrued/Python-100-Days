import lessonsJson from "@/content/lessons.json";
import questionsJson from "@/content/questions.json";
import type { CodingQuestion, Lesson, LessonQuestions, Topic } from "./types";

const lessons = lessonsJson as Lesson[];
const questionBank = questionsJson as { lessons: LessonQuestions[] };

export function getLessons(): Lesson[] {
  return lessons;
}

export function getLesson(slug: string): Lesson | undefined {
  return lessons.find((l) => l.slug === slug);
}

export function getQuestionsForDay(day: number): CodingQuestion[] {
  return questionBank.lessons.find((l) => l.day === day)?.questions ?? [];
}

export function getQuestionCount(day: number): number {
  return getQuestionsForDay(day).length;
}

export function getTotalQuestions(): number {
  return questionBank.lessons.reduce((n, l) => n + l.questions.length, 0);
}

export const TOPICS: { id: Topic; cn: string; en: string; color: string }[] = [
  { id: "basics", cn: "Python 基础", en: "Basics", color: "bg-sky-100 text-sky-700" },
  { id: "control-flow", cn: "流程控制", en: "Control Flow", color: "bg-violet-100 text-violet-700" },
  { id: "data-structures", cn: "数据结构", en: "Data Structures", color: "bg-emerald-100 text-emerald-700" },
  { id: "functions", cn: "函数", en: "Functions", color: "bg-amber-100 text-amber-700" },
  { id: "oop", cn: "面向对象", en: "OOP", color: "bg-rose-100 text-rose-700" },
  { id: "misc", cn: "其他", en: "Misc", color: "bg-slate-100 text-slate-700" },
];

export function topicMeta(topic: Topic) {
  return TOPICS.find((t) => t.id === topic) ?? TOPICS[TOPICS.length - 1];
}
