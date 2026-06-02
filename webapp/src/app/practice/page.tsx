import { getLessons, getQuestionsForDay } from "@/lib/data";
import { PracticeList } from "@/components/PracticeList";

export default function PracticePage() {
  const items = getLessons()
    .map((l) => {
      const qs = getQuestionsForDay(l.day);
      const estMinutes = qs.reduce((s, q) => s + (q.estMinutes || 4), 0);
      return {
        slug: l.slug,
        day: l.day,
        titleCn: l.titleCn,
        titleEn: l.titleEn,
        topic: l.topic,
        questionCount: qs.length,
        estMinutes: Math.max(1, estMinutes),
      };
    })
    .filter((l) => l.questionCount > 0);

  return <PracticeList items={items} />;
}
