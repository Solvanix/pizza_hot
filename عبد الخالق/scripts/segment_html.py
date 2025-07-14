from bs4 import BeautifulSoup
import json
import os

html_path = "/mnt/c/Users/ali/Desktop/عبد الخالق/ocr_full_analysis.html"
segments_dir = "/mnt/c/Users/ali/Desktop/عبد الخالق/segments/"
catalog_path = "/mnt/c/Users/ali/Desktop/عبد الخالق/catalog/catalog_map.json"

# تحميل ملف OCR
with open(html_path, encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# تحميل خريطة الفهرس
with open(catalog_path, encoding="utf-8") as f:
    catalog = json.load(f)

# استخراج الصفحات في قالب {رقم الصفحة: عنصر الصفحة}
pages = {
    int(div.find("h2").text.replace("صفحة", "").strip()): div
    for div in soup.find_all("div", class_="page")
}

# إنشاء مجلد التقسيم إن لم يكن موجودًا
os.makedirs(segments_dir, exist_ok=True)

# التقسيم حسب الفهرس
for idx, item in enumerate(catalog, start=1):
    start, end = item["start"], item["end"]
    title = item["title"]
    selected_pages = [pages[p] for p in range(start, end + 1) if p in pages]
    content = "\n".join(str(div) for div in selected_pages)

    output_file = os.path.join(segments_dir, f"unit_{idx:02}.html")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"<h1>{title}</h1>\n{content}")

print("✅ تم تقسيم الملف إلى وحدات بناءً على خريطة الفهرس")
