// Merge a single-lesson workflow result into questions.json (insert/replace by day, keep sorted).
import { readFileSync, writeFileSync } from "node:fs";

const outFile = process.argv[2];
const bankUrl = new URL("../src/content/questions.json", import.meta.url);

const parsed = JSON.parse(readFileSync(outFile, "utf8"));
const incoming = (parsed.result?.lessons ?? parsed.lessons ?? []);
if (!incoming.length) {
  console.error("no incoming lessons");
  process.exit(1);
}

const bank = JSON.parse(readFileSync(bankUrl, "utf8"));
for (const lesson of incoming) {
  const i = bank.lessons.findIndex((l) => l.day === lesson.day);
  if (i >= 0) bank.lessons[i] = lesson;
  else bank.lessons.push(lesson);
}
bank.lessons.sort((a, b) => a.day - b.day);

writeFileSync(bankUrl, JSON.stringify(bank, null, 2), "utf8");
const total = bank.lessons.reduce((n, l) => n + l.questions.length, 0);
console.log(`merged day(s): ${incoming.map((l) => l.day).join(",")}`);
console.log(`bank now: ${bank.lessons.length} lessons, ${total} exercises`);
console.log("per-day:", bank.lessons.map((l) => l.day + ":" + l.questions.length).join(" "));
