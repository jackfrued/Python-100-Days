import React from "react";

// A compact, dependency-free Markdown renderer tuned for the lesson notes.
// Handles: ATX headings, fenced code blocks, ordered/unordered lists (with
// nesting via indentation), blockquotes, tables, horizontal rules, and inline
// spans (bold, inline code, links). Good enough for these specific files.

type Inline = React.ReactNode;

function renderInline(text: string, keyPrefix: string): Inline[] {
  const nodes: Inline[] = [];
  // Tokenize on `code`, **bold**, [text](url). Inline code wins first.
  // Strip simple $...$ math delimiters to plain text (rare, e.g. 1.23e2 notes).
  const cleaned = text.replace(/\\?\$([^$\n]+?)\\?\$/g, (_m, inner) => inner);

  const regex = /(`[^`]+`)|(\*\*[^*]+\*\*)|(!\[[^\]]*\]\([^)]+\))|(\[[^\]]+\]\([^)]+\))/g;
  let last = 0;
  let m: RegExpExecArray | null;
  let i = 0;
  while ((m = regex.exec(cleaned)) !== null) {
    if (m.index > last) nodes.push(cleaned.slice(last, m.index));
    const tok = m[0];
    const key = `${keyPrefix}-${i++}`;
    if (tok.startsWith("`")) {
      nodes.push(
        <code key={key}>{tok.slice(1, -1)}</code>
      );
    } else if (tok.startsWith("**")) {
      nodes.push(<strong key={key}>{tok.slice(2, -2)}</strong>);
    } else if (tok.startsWith("![")) {
      const im = tok.match(/^!\[([^\]]*)\]\(([^)]+)\)$/);
      if (im) {
        // eslint-disable-next-line @next/next/no-img-element
        nodes.push(
          <img key={key} src={im[2]} alt={im[1]} className="my-3 max-w-full rounded-lg border border-slate-200" />
        );
      } else {
        nodes.push(tok);
      }
    } else {
      const lm = tok.match(/^\[([^\]]+)\]\(([^)]+)\)$/);
      if (lm) {
        const href = lm[2];
        const external = /^https?:\/\//.test(href);
        nodes.push(
          <a
            key={key}
            href={href}
            target={external ? "_blank" : undefined}
            rel={external ? "noopener noreferrer" : undefined}
          >
            {lm[1]}
          </a>
        );
      } else {
        nodes.push(tok);
      }
    }
    last = m.index + tok.length;
  }
  if (last < cleaned.length) nodes.push(cleaned.slice(last));
  return nodes;
}

interface ListItem {
  indent: number;
  ordered: boolean;
  text: string;
}

function renderList(items: ListItem[], keyBase: string): React.ReactNode {
  // Build nested lists from indentation levels.
  const ordered = items[0]?.ordered ?? false;
  const out: React.ReactNode[] = [];
  let idx = 0;
  while (idx < items.length) {
    const item = items[idx];
    // gather children (more-indented items immediately following)
    const children: ListItem[] = [];
    let j = idx + 1;
    while (j < items.length && items[j].indent > item.indent) {
      children.push(items[j]);
      j++;
    }
    out.push(
      <li key={`${keyBase}-${idx}`}>
        {renderInline(item.text, `${keyBase}-${idx}`)}
        {children.length > 0 ? renderList(children, `${keyBase}-${idx}c`) : null}
      </li>
    );
    idx = j;
  }
  return ordered ? (
    <ol key={keyBase}>{out}</ol>
  ) : (
    <ul key={keyBase}>{out}</ul>
  );
}

export function Markdown({ source }: { source: string }) {
  const lines = source.replace(/\r\n/g, "\n").split("\n");
  const blocks: React.ReactNode[] = [];
  let i = 0;
  let key = 0;

  while (i < lines.length) {
    const line = lines[i];

    // fenced code block
    const fence = line.match(/^```(\w*)/);
    if (fence) {
      const lang = fence[1];
      const buf: string[] = [];
      i++;
      while (i < lines.length && !/^```/.test(lines[i])) {
        buf.push(lines[i]);
        i++;
      }
      i++; // closing fence
      blocks.push(
        <pre key={key++} data-lang={lang}>
          <code>{buf.join("\n")}</code>
        </pre>
      );
      continue;
    }

    // heading
    const h = line.match(/^(#{1,6})\s+(.*)$/);
    if (h) {
      const level = h[1].length;
      const content = renderInline(h[2], `h-${key}`);
      const Tag = (`h${Math.min(level, 4)}` as keyof JSX.IntrinsicElements);
      blocks.push(<Tag key={key++}>{content}</Tag>);
      i++;
      continue;
    }

    // horizontal rule
    if (/^(\*{3,}|-{3,}|_{3,})\s*$/.test(line)) {
      blocks.push(<hr key={key++} className="my-6 border-slate-200" />);
      i++;
      continue;
    }

    // blockquote (consume consecutive > lines)
    if (/^>\s?/.test(line)) {
      const buf: string[] = [];
      while (i < lines.length && /^>\s?/.test(lines[i])) {
        buf.push(lines[i].replace(/^>\s?/, ""));
        i++;
      }
      blocks.push(
        <blockquote key={key++}>
          {renderInline(buf.join(" "), `bq-${key}`)}
        </blockquote>
      );
      continue;
    }

    // table (header row followed by |---| separator)
    if (/^\s*\|.*\|\s*$/.test(line) && i + 1 < lines.length && /^\s*\|?[\s:|-]+\|?\s*$/.test(lines[i + 1]) && lines[i + 1].includes("-")) {
      const splitRow = (r: string) =>
        r.trim().replace(/^\||\|$/g, "").split("|").map((c) => c.trim());
      const header = splitRow(line);
      i += 2; // skip header + separator
      const rows: string[][] = [];
      while (i < lines.length && /^\s*\|.*\|\s*$/.test(lines[i])) {
        rows.push(splitRow(lines[i]));
        i++;
      }
      blocks.push(
        <table key={key++}>
          <thead>
            <tr>
              {header.map((c, ci) => (
                <th key={ci}>{renderInline(c, `th-${key}-${ci}`)}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map((row, ri) => (
              <tr key={ri}>
                {row.map((c, ci) => (
                  <td key={ci}>{renderInline(c, `td-${key}-${ri}-${ci}`)}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      );
      continue;
    }

    // list (consume consecutive list lines, track indentation)
    if (/^\s*([-*+]|\d+\.)\s+/.test(line)) {
      const items: ListItem[] = [];
      while (i < lines.length && /^\s*([-*+]|\d+\.)\s+/.test(lines[i])) {
        const lm = lines[i].match(/^(\s*)([-*+]|\d+\.)\s+(.*)$/);
        if (!lm) break;
        items.push({
          indent: lm[1].length,
          ordered: /\d+\./.test(lm[2]),
          text: lm[3],
        });
        i++;
        // allow blank line then continued nested list? keep simple: stop on blank.
      }
      blocks.push(renderList(items, `list-${key++}`));
      continue;
    }

    // standalone HTML <img> tag (lessons embed these for figures)
    const imgTag = line.trim().match(/^<img[^>]*\bsrc="([^"]+)"[^>]*>$/);
    if (imgTag) {
      const altM = line.match(/\balt="([^"]*)"/);
      // eslint-disable-next-line @next/next/no-img-element
      blocks.push(
        <img
          key={key++}
          src={imgTag[1]}
          alt={altM ? altM[1] : ""}
          className="my-4 max-w-full rounded-lg border border-slate-200"
        />
      );
      i++;
      continue;
    }

    // blank line
    if (line.trim() === "") {
      i++;
      continue;
    }

    // paragraph: gather until blank / block start
    const buf: string[] = [line];
    i++;
    while (
      i < lines.length &&
      lines[i].trim() !== "" &&
      !/^(#{1,6}\s|```|>\s?|\s*([-*+]|\d+\.)\s+)/.test(lines[i]) &&
      !/^(\*{3,}|-{3,}|_{3,})\s*$/.test(lines[i])
    ) {
      buf.push(lines[i]);
      i++;
    }
    blocks.push(<p key={key++}>{renderInline(buf.join(" "), `p-${key}`)}</p>);
  }

  return <div className="prose-cn">{blocks}</div>;
}
