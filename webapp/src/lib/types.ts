export type Topic =
  | "basics"
  | "control-flow"
  | "data-structures"
  | "functions"
  | "oop"
  | "misc";

export interface Lesson {
  day: number;
  slug: string;
  titleCn: string;
  titleEn: string;
  topic: Topic;
  summary: string;
  codeBlocks: number;
  readMinutes: number;
  markdown: string;
}

export type Difficulty = "easy" | "medium" | "hard";

/**
 * A hands-on coding exercise. The user implements `entry` (a function or, for
 * OOP lessons, a class) in the editor; we run their code plus `tests` (a block
 * of asserts) in-browser via Pyodide. `solution` is the hidden reference used
 * to verify the tests at generation time — it is NOT shipped to the editor by
 * default but is available as a "show solution" reveal.
 */
export interface CodingQuestion {
  id: string;
  difficulty: Difficulty;
  title_cn: string;
  title_en: string;
  prompt_cn: string; // what to implement, constraints, examples
  prompt_en: string;
  entry: string; // the function/class name the tests call, e.g. "fizzbuzz"
  starter: string; // starter code shown in the editor (stub)
  solution: string; // reference solution (hidden, used for verification + reveal)
  tests: string; // python assert block that references `entry`
  hint_cn?: string;
  hint_en?: string;
  estMinutes: number;
}

export interface LessonQuestions {
  day: number;
  topic: Topic;
  questions: CodingQuestion[];
}
