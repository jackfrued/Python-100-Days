"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useLang } from "@/lib/lang-context";

export function NavBar() {
  const { t, lang, toggle } = useLang();
  const pathname = usePathname();

  const links = [
    { href: "/", label: t("navHome"), match: (p: string) => p === "/" },
    { href: "/learn", label: t("navLearn"), match: (p: string) => p.startsWith("/learn") },
    { href: "/practice", label: t("navPractice"), match: (p: string) => p.startsWith("/practice") },
  ];

  return (
    <header className="sticky top-0 z-20 border-b border-slate-200 bg-white/85 backdrop-blur">
      <nav className="mx-auto flex max-w-5xl items-center justify-between px-4 py-3">
        <Link href="/" className="flex items-center gap-2 font-bold text-slate-900">
          <span className="grid h-8 w-8 place-items-center rounded-lg bg-blue-600 text-white">
            Py
          </span>
          <span className="hidden sm:inline">{t("appName")}</span>
        </Link>

        <div className="flex items-center gap-1">
          {links.map((l) => {
            const active = l.match(pathname);
            return (
              <Link
                key={l.href}
                href={l.href}
                className={`rounded-lg px-3 py-1.5 text-sm font-medium transition ${
                  active
                    ? "bg-blue-600 text-white"
                    : "text-slate-600 hover:bg-slate-100"
                }`}
              >
                {l.label}
              </Link>
            );
          })}
          <button
            onClick={toggle}
            className="ml-2 rounded-lg border border-slate-300 px-2.5 py-1.5 text-xs font-semibold text-slate-600 hover:bg-slate-100"
            aria-label="toggle language"
            title={lang === "cn" ? "Switch to English" : "切换到中文"}
          >
            {t("langLabel")}
          </button>
        </div>
      </nav>
    </header>
  );
}
