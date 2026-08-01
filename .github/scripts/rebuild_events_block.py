"""One-shot: rebuild BRIEF:RECENT_EVENTS_DATA block in index.html from events.csv,
emitting the `hormuz:` key so the scope filter works without waiting for the
next bot cron.

Self-contained (no anthropic dep) — inlines the CSV read + render logic that
matches update_brief.py."""
import csv
import re
from pathlib import Path

repo = Path(__file__).parent.parent.parent
csv_path = repo / "events.csv"


def load_events():
    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def js_str(s):
    return (s or "").replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").replace("\r", "").strip()


def render(events, max_events=220):
    sorted_events = sorted(events, key=lambda e: e.get("date", ""), reverse=True)[:max_events]
    lines = []
    for e in sorted_events:
        cls = (e.get("indicator_class") or "FM").strip()
        tier_val = (e.get("tier") or "1").strip()
        hormuz_val = (e.get("hormuz_linked") or "True").strip().lower()
        hormuz_bool = "true" if hormuz_val == "true" else "false"
        line = (
            "{ "
            f'date: "{js_str(e.get("date", ""))}", '
            f'operator: "{js_str(e.get("entity", ""))}", '
            f'country: "{js_str(e.get("country", ""))}", '
            f'chain: "{js_str(e.get("chain", ""))}", '
            f'kind: "{js_str(cls)}", '
            f'tier: "T{js_str(tier_val)}", '
            f'hormuz: {hormuz_bool}, '
            f'source: "{js_str(e.get("source", ""))}", '
            f'summary: "{js_str(e.get("notes", ""))}"'
            " }"
        )
        lines.append(line)
    return ",\n".join(lines)


events = load_events()
block = render(events)

for fn in ["index.html"]:
    p = repo / fn
    txt = p.read_text(encoding="utf-8")
    pattern = re.compile(
        r"(// BRIEF:RECENT_EVENTS_DATA_START\r?\n)(.*?)(\r?\n// BRIEF:RECENT_EVENTS_DATA_END)",
        re.DOTALL,
    )
    if not pattern.search(txt):
        print(f"  markers not found in {fn}")
        continue
    new_txt = pattern.sub(lambda m: m.group(1) + block + m.group(3), txt, count=1)
    p.write_text(new_txt, encoding="utf-8", newline="\n")
    print(f"  updated {fn}: {len(events)} events -> {len(block)} chars")
