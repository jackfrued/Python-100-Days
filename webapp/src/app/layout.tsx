import type { Metadata } from "next";
import "./globals.css";
import { LangProvider } from "@/lib/lang-context";
import { NavBar } from "@/components/NavBar";

export const metadata: Metadata = {
  title: "Python 百日学练 · Learn & Practice",
  description:
    "基于 Python-100-Days 讲义的学习与练习平台 / Learn and practice the Python-100-Days course.",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="zh-CN" className="h-full">
      <body className="min-h-full flex flex-col">
        <LangProvider>
          <NavBar />
          <main className="flex-1 w-full">{children}</main>
          <footer className="border-t border-slate-200 py-6 text-center text-sm text-slate-500">
            基于{" "}
            <a
              className="text-blue-600 hover:underline"
              href="https://github.com/jackfrued/Python-100-Days"
              target="_blank"
              rel="noopener noreferrer"
            >
              Python-100-Days
            </a>{" "}
            讲义构建 · 题库由 AI 生成并校验
          </footer>
        </LangProvider>
      </body>
    </html>
  );
}
