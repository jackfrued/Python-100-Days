import { readFileSync, writeFileSync } from "node:fs";

const out = process.argv[2];
const parsed = JSON.parse(readFileSync(out, "utf8"));
const lessons = parsed.result?.lessons ?? parsed.lessons ?? [];

if (!lessons.length) {
  console.error("no lessons found in result");
  process.exit(1);
}

// Sort lessons by day, questions by id, for stable output.
lessons.sort((a, b) => a.day - b.day);
const total = lessons.reduce((n, l) => n + (l.questions?.length ?? 0), 0);

writeFileSync(
  new URL("../src/content/questions.json", import.meta.url),
  JSON.stringify({ lessons }, null, 2),
  "utf8"
);
console.log("lessons:", lessons.length, "total questions:", total);
console.log("per-day:", lessons.map((l) => l.day + ":" + l.questions.length).join(" "));
