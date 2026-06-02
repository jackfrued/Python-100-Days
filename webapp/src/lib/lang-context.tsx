"use client";

import { createContext, useContext, useEffect, useState, useCallback } from "react";
import type { Lang } from "./i18n";
import { STRINGS, type StringKey } from "./i18n";

interface LangCtx {
  lang: Lang;
  setLang: (l: Lang) => void;
  toggle: () => void;
  t: (key: StringKey) => string;
}

const Ctx = createContext<LangCtx | null>(null);

export function LangProvider({ children }: { children: React.ReactNode }) {
  // Chinese is the default per the source material.
  const [lang, setLangState] = useState<Lang>("cn");

  useEffect(() => {
    const saved = window.localStorage.getItem("py100-lang");
    if (saved === "cn" || saved === "en") setLangState(saved);
  }, []);

  const setLang = useCallback((l: Lang) => {
    setLangState(l);
    window.localStorage.setItem("py100-lang", l);
    document.documentElement.lang = l === "cn" ? "zh-CN" : "en";
  }, []);

  const toggle = useCallback(() => {
    setLang(lang === "cn" ? "en" : "cn");
  }, [lang, setLang]);

  const t = useCallback((key: StringKey) => STRINGS[key][lang], [lang]);

  return <Ctx.Provider value={{ lang, setLang, toggle, t }}>{children}</Ctx.Provider>;
}

export function useLang(): LangCtx {
  const ctx = useContext(Ctx);
  if (!ctx) throw new Error("useLang must be used within LangProvider");
  return ctx;
}
