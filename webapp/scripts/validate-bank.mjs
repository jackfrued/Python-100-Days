import { readFileSync } from "node:fs";

const bank = JSON.parse(
  readFileSync(new URL("../src/content/questions.json", import.meta.url), "utf8")
);

const errors = [];
const ids = new Set();
let count = 0;

for (const lesson of bank.lessons) {
  for (const q of lesson.questions) {
    count++;
    const loc = `day${lesson.day}/${q.id}`;
    if (ids.has(q.id)) errors.push(`${loc}: duplicate id`);
    ids.add(q.id);
    for (const f of [
      "difficulty",
      "title_cn",
      "title_en",
      "prompt_cn",
      "prompt_en",
      "entry",
      "starter",
      "solution",
      "tests",
    ]) {
      if (!q[f]) errors.push(`${loc}: missing ${f}`);
    }
    if (q.tests && !/\bassert\b/.test(q.tests)) errors.push(`${loc}: tests has no assert`);
    if (q.entry && q.starter && !q.starter.includes(q.entry))
      errors.push(`${loc}: starter does not define entry "${q.entry}"`);
    if (q.entry && q.solution && !q.solution.includes(q.entry))
      errors.push(`${loc}: solution does not define entry "${q.entry}"`);
    if (q.entry && q.tests && !q.tests.includes(q.entry))
      errors.push(`${loc}: tests do not reference entry "${q.entry}"`);
    if (q.estMinutes && (q.estMinutes < 1 || q.estMinutes > 15))
      errors.push(`${loc}: estMinutes out of range (${q.estMinutes})`);
  }
}

console.log(`Validated ${count} coding exercises across ${bank.lessons.length} lessons.`);
if (errors.length) {
  console.error(`\n${errors.length} ISSUES:`);
  errors.forEach((e) => console.error("  - " + e));
  process.exit(1);
} else {
  console.log("All structural checks passed ✓");
}
