#!/usr/bin/env python3
"""md2html.py — render a report .md to standalone HTML for PDF conversion.

Minimal on purpose: headings, paragraphs, lists, tables, code fences, inline
bold/italic/code, links. No external deps. Usage: md2html.py in.md out.html
"""
import html
import re
import sys


def inline(s):
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def main(src, dst):
    out, in_code, in_list, in_table = [], False, False, False
    for raw in open(src, encoding="utf-8").read().splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            out.append("<pre><code>" if not in_code else "</code></pre>")
            in_code = not in_code
            continue
        if in_code:
            out.append(html.escape(raw))
            continue
        if re.match(r"^\|.+\|$", line) and set(line.replace("|", "").strip()) <= set("-: "):
            continue  # table separator
        if line.startswith("|") and line.endswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if not in_table:
                out.append("<table>")
                in_table = True
                tag = "th"
            else:
                tag = "td"
            out.append("<tr>" + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in cells) + "</tr>")
            continue
        if in_table:
            out.append("</table>")
            in_table = False
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            n = len(m.group(1))
            out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
            continue
        m = re.match(r"^\s*[-*]\s+(.*)$", line)
        if m:
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(m.group(1))}</li>")
            continue
        if in_list:
            out.append("</ul>")
            in_list = False
        if line.strip():
            out.append(f"<p>{inline(line)}</p>")
    for flag, close in ((in_list, "</ul>"), (in_table, "</table>"), (in_code, "</code></pre>")):
        if flag:
            out.append(close)
    body = "\n".join(out)
    open(dst, "w", encoding="utf-8").write(
        "<!doctype html><meta charset=utf-8><style>"
        "body{font:11pt/1.45 -apple-system,Segoe UI,Arial;max-width:46em;margin:2em auto;color:#111}"
        "h1{font-size:17pt}h2{font-size:13pt;margin-top:1.4em}table{border-collapse:collapse;width:100%}"
        "td,th{border:1px solid #bbb;padding:4px 6px;text-align:left;vertical-align:top}"
        "code{background:#f2f2f2;padding:0 2px}pre{background:#f6f6f6;padding:8px;overflow-x:auto}"
        "</style><body>" + body + "</body>"
    )


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
