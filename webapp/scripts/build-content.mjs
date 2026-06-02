// Parses the Day01-20 Python-100-Days markdown lessons into a structured
// lessons.json consumed by the Next.js app. Runs in pre-dev / pre-build.
//
// Source lives one level up from webapp/ in the repo: ../Day01-20/*.md
import { readFileSync, writeFileSync, readdirSync, existsSync, mkdirSync, cpSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = join(__dirname, "..", "..");
const SRC_DIR = join(REPO_ROOT, "Day01-20");
const OUT_DIR = join(__dirname, "..", "src", "content");
const PUBLIC_RES = join(__dirname, "..", "public", "lesson-res");

if (!existsSync(SRC_DIR)) {
  console.error(`[build-content] source dir not found: ${SRC_DIR}`);
  process.exit(1);
}
if (!existsSync(OUT_DIR)) mkdirSync(OUT_DIR, { recursive: true });

// Copy lesson images into public/ so the reader can serve them.
const SRC_RES = join(SRC_DIR, "res");
if (existsSync(SRC_RES)) {
  cpSync(SRC_RES, PUBLIC_RES, { recursive: true });
}

// English titles for bilingual UI (source titles are Chinese).
const EN_TITLES = {
  1: "Getting to Know Python",
  2: "Your First Python Program",
  3: "Variables in Python",
  4: "Operators in Python",
  5: "Branching (if / elif / else)",
  6: "Loops (for / while)",
  7: "Branching & Loops in Practice",
  8: "Lists, Part 1",
  9: "Lists, Part 2",
  10: "Tuples",
  11: "Strings",
  12: "Sets",
  13: "Dictionaries",
  14: "Functions & Modules",
  15: "Functions in Practice",
  16: "Functions, Intermediate",
  17: "Functions, Advanced",
  18: "Object-Oriented Programming: Intro",
  19: "Object-Oriented Programming: Deeper",
  20: "Object-Oriented Programming: Applications",
};

// Short English topic tags used for grouping/filtering.
const TOPIC = {
  1: "basics", 2: "basics", 3: "basics", 4: "basics",
  5: "control-flow", 6: "control-flow", 7: "control-flow",
  8: "data-structures", 9: "data-structures", 10: "data-structures",
  11: "data-structures", 12: "data-structures", 13: "data-structures",
  14: "functions", 15: "functions", 16: "functions", 17: "functions",
  18: "oop", 19: "oop", 20: "oop",
};

function parseFile(filename) {
  const m = filename.match(/^(\d+)\.(.+)\.md$/);
  if (!m) return null;
  const day = parseInt(m[1], 10);
  const titleCn = m[2];
  let raw = readFileSync(join(SRC_DIR, filename), "utf8");

  // Rewrite repo-relative image paths to the public/ copy.
  // <img src="res/dayNN/x.png" ...> and ![alt](res/dayNN/x.png)
  raw = raw
    .replace(/(<img[^>]*\bsrc=")res\//g, "$1/lesson-res/")
    .replace(/(\]\()res\//g, "$1/lesson-res/");

  // first heading text (strip leading ## )
  const firstHeading = (raw.match(/^#{1,3}\s+(.+)$/m) || [])[1] || titleCn;

  // crude reading-time + summary: take first non-heading paragraph
  const paragraphs = raw
    .split(/\n{2,}/)
    .map((p) => p.trim())
    .filter((p) => p && !p.startsWith("#") && !p.startsWith("```") && !p.startsWith(">"));
  const summary = (paragraphs[0] || "")
    .replace(/[`*]/g, "")
    .replace(/\s+/g, " ")
    .slice(0, 120);

  const codeBlocks = (raw.match(/```/g) || []).length / 2;
  const words = raw.length; // CJK: char count ~ reading load
  const minutes = Math.max(3, Math.round(words / 450));

  return {
    day,
    slug: String(day).padStart(2, "0"),
    titleCn: firstHeading.trim(),
    titleEn: EN_TITLES[day] || firstHeading.trim(),
    topic: TOPIC[day] || "misc",
    summary,
    codeBlocks: Math.round(codeBlocks),
    readMinutes: minutes,
    markdown: raw,
  };
}

const files = readdirSync(SRC_DIR)
  .filter((f) => /^\d+\..+\.md$/.test(f))
  .sort((a, b) => parseInt(a) - parseInt(b));

const lessons = files.map(parseFile).filter(Boolean);

writeFileSync(
  join(OUT_DIR, "lessons.json"),
  JSON.stringify(lessons, null, 2),
  "utf8"
);

console.log(`[build-content] wrote ${lessons.length} lessons -> src/content/lessons.json`);
