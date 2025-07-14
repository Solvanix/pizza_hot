from bs4 import BeautifulSoup
import os
import json

units_dir = "/mnt/c/Users/ali/Desktop/عبد الخالق/site/units/"
output_path = "/mnt/c/Users/ali/Desktop/عبد الخالق/catalog/search_index.json"
index = []

for filename in sorted(os.listdir(units_dir)):
    if not filename.endswith(".html"): continue

    filepath = os.path.join(units_dir, filename)
    with open(filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        title = soup.find("h1").text.strip() if soup.find("h1") else filename
        raw_text = soup.get_text(separator=" ", strip=True)
        snippet = raw_text[:5000]  # قص النص لسهولة التخزين

        index.append({
            "file": filename,
            "title": title,
            "text": snippet
        })

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)

print("✅ تم إنشاء قاعدة البحث في search_index.json")
