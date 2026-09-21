#!/usr/bin/env python3
"""Bake partials/header.html and partials/footer.html into every page's HTML.

The nav and footer must exist in the static HTML so crawlers that don't run
JavaScript can see the internal links. partials/ stays the single source of
truth: edit those two files, then run this script before committing.

  python3 scripts/inline-partials.py           rewrite pages in place
  python3 scripts/inline-partials.py --check   exit 1 if any page is stale
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MOUNTS = {
    "site-header-mount": ROOT / "partials" / "header.html",
    "site-footer-mount": ROOT / "partials" / "footer.html",
}
START, END = "<!--partial:start-->", "<!--partial:end-->"


def render(page_html: str) -> str:
    for mount_id, partial in MOUNTS.items():
        body = partial.read_text().strip("\n")
        pattern = re.compile(
            r'(<div id="%s">)(?:%s.*?%s)?(</div>)' % (mount_id, re.escape(START), re.escape(END)),
            re.S,
        )
        page_html = pattern.sub(
            lambda m: f"{m.group(1)}{START}\n{body}\n{END}{m.group(2)}", page_html
        )
    return page_html


def main() -> int:
    check = "--check" in sys.argv
    stale = []
    for page in sorted(ROOT.glob("*.html")):
        old = page.read_text()
        if 'id="site-header-mount"' not in old:
            continue
        new = render(old)
        if new != old:
            stale.append(page.name)
            if not check:
                page.write_text(new)
    if check:
        print("stale pages: " + ", ".join(stale) if stale else "all pages up to date")
        return 1 if stale else 0
    print("updated: " + ", ".join(stale) if stale else "nothing to update")
    return 0


if __name__ == "__main__":
    sys.exit(main())
