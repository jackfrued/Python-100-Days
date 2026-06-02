import { getLessons, getTotalQuestions } from "@/lib/data";
import { HomeView } from "@/components/HomeView";

export default function HomePage() {
  const lessons = getLessons();
  return (
    <HomeView lessonCount={lessons.length} questionCount={getTotalQuestions()} />
  );
}
