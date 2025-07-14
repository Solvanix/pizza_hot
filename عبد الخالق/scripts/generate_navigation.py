import os

segments_dir = "/mnt/c/Users/ali/Desktop/عبد الخالق/segments/"
output_dir = "/mnt/c/Users/ali/Desktop/عبد الخالق/site/units/"
os.makedirs(output_dir, exist_ok=True)

files = sorted(f for f in os.listdir(segments_dir) if f.startswith("unit_") and f.endswith(".html"))

search_box = """<div style='margin:2em 0; background:#f0f8ff; padding:1em; border-radius:6px;'>
  <h3>🔍 بحث سريع داخل المشروع</h3>
  <input type="text" id="query" placeholder="اكتب كلمة أو سؤال أو عبارة" style="width:80%;">
  <button onclick="search()">بحث</button>
  <div id="results"></div>
  <script>
    async function search() {
      const q = document.getElementById("query").value.trim();
      if (!q) return;
      const res = await fetch("../../catalog/search_index.json").then(r => r.json());
      let hits = [];
      for (const page of res) {
        if (page.text.includes(q)) {
          hits.push(`<li><a href="../../site/units/${page.file}">${page.title}</a></li>`);
        }
      }
      document.getElementById("results").innerHTML = hits.length ?
        "<h4>النتائج:</h4><ul>" + hits.join("") + "</ul>" :
        "<p>❌ لا توجد نتائج مطابقة</p>";
    }
  </script>
</div>"""

for i, filename in enumerate(files):
    with open(os.path.join(segments_dir, filename), encoding="utf-8") as f:
        content = f.read()

    nav = ""
    if i > 0:
        nav += f'<a href="{files[i - 1]}">⬅️ السابق</a> | '
    nav += '<a href="../readme.html">📘 الفهرس</a>'
    if i < len(files) - 1:
        nav += f' | <a href="{files[i + 1]}">التالي ➡️</a>'

    pdf_link = f'<div><a href="../../pdfs/unit_{i+1:02}.pdf" target="_blank">📄 تحميل ملف PDF للفصل</a></div>'

    page = f"<div style='padding:1em;background:#eef;'>{nav}</div><hr>\n{pdf_link}\n<hr>\n{search_box}\n<hr>\n{content}\n<hr><div>{nav}</div>"

    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
        f.write(page)

print("✅ تم تضمين روابط ملفات PDF + نموذج البحث داخل صفحات الوحدات")
