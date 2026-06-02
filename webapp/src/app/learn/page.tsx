import { getLessons, getQuestionCount } from "@/lib/data";
import { LearnList } from "@/components/LearnList";

export default function LearnPage() {
  const lessons = getLessons().map((l) => ({
    ...l,
    questionCount: getQuestionCount(l.day),
  }));
  return <LearnList lessons={lessons} />;
}
