from pathlib import Path

target = Path("bonus/next-dashboard/app/page.js")
content = target.read_text(encoding="utf-8")
clean = content.replace('\\"', '"')
target.write_text(clean, encoding="utf-8")
print(f"Cleaned {target}, length {len(clean)}")
