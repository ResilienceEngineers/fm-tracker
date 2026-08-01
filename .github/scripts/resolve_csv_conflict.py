"""One-shot: resolve unresolved merge conflict in events.csv.
- HEAD side: 227 rows, 13-col schema (no hormuz_linked)
- Merged side: 175 rows, 14-col schema (with hormuz_linked)
Strategy: keep 14-col schema, union rows by (entity|chain|date), default
hormuz_linked=True for all legacy rows (all current events are Hormuz-linked
per the tracker's original scope). Newest-first dedup keeps the fresher notes.
"""
import csv
import io
from pathlib import Path

repo = Path(__file__).parent.parent.parent
csv_path = repo / "events.csv"

FULL_COLS = [
    "day", "entity", "country", "chain", "wave", "fm_type",
    "volume_kt", "is_eu_direct", "source", "notes", "date",
    "indicator_class", "tier", "hormuz_linked",
]
OLD_COLS = FULL_COLS[:-1]  # 13-col schema without hormuz_linked

raw = csv_path.read_text(encoding="utf-8-sig")
lines = raw.split("\n")

# Locate conflict markers
head_marker = next(i for i, l in enumerate(lines) if l.startswith("<<<<<<<"))
sep_marker = next(i for i, l in enumerate(lines) if l.startswith("======="))
tail_marker = next(i for i, l in enumerate(lines) if l.startswith(">>>>>>>"))

head_block = "\n".join(lines[head_marker + 1 : sep_marker])
merged_block = "\n".join(lines[sep_marker + 1 : tail_marker])

def parse_block(block_text, expected_cols):
    reader = csv.DictReader(io.StringIO(block_text))
    rows = list(reader)
    # If the reader misparsed (wrong column count), fall back
    if reader.fieldnames != expected_cols:
        print(f"  warn: reader saw {reader.fieldnames}, expected {expected_cols}")
    return rows

head_rows = parse_block(head_block, OLD_COLS)
merged_rows = parse_block(merged_block, FULL_COLS)

print(f"HEAD side: {len(head_rows)} rows ({len(head_rows[0]) if head_rows else 0} cols)")
print(f"Merged side: {len(merged_rows)} rows ({len(merged_rows[0]) if merged_rows else 0} cols)")

# Union, keyed by (entity|chain|date). Prefer the row with more columns filled;
# on tie prefer the row that already has hormuz_linked set.
def key(row):
    return (
        (row.get("entity", "") or "").strip().lower(),
        (row.get("chain", "") or "").strip().lower(),
        (row.get("date", "") or "").strip(),
    )

def fill_score(row):
    return sum(1 for v in row.values() if (v or "").strip())

pool = {}
for r in merged_rows + head_rows:
    # Upgrade HEAD rows to 14-col schema
    if "hormuz_linked" not in r:
        r["hormuz_linked"] = "True"
    k = key(r)
    if k not in pool or fill_score(r) > fill_score(pool[k]):
        pool[k] = r

merged = list(pool.values())
print(f"Merged pool: {len(merged)} unique rows")

# Sort by date desc, then day asc for stability
merged.sort(key=lambda r: (r.get("date", ""), r.get("day", "")), reverse=True)

# Write back (14-col schema, quote everything for consistency with bot output)
with open(csv_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=FULL_COLS, quoting=csv.QUOTE_ALL)
    w.writeheader()
    for r in merged:
        w.writerow({c: r.get(c, "") or "" for c in FULL_COLS})

print(f"Wrote {len(merged)} rows to events.csv (14-col schema, all hormuz_linked=True)")
