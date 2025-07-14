import os
from weasyprint import HTML

segments_dir = "/mnt/c/Users/ali/Desktop/عبد الخالق/segments/"
cover_path = "/mnt/c/Users/ali/Desktop/عبد الخالق/cover.html"
output_pdf = "/mnt/c/Users/ali/Desktop/عبد الخالق/pdfs/full_document.pdf"
os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

arabic_css = """
<style>
  @font-face {
    font-family: 'Amiri';
    src: url('file:///mnt/c/Users/ali/Desktop/عبد الخالق/fonts/Amiri-Regular.ttf');
  }
  body {
    font-family: 'Amiri', serif;
    direction: rtl;
    unicode-bidi: bidi-override;
    line-height: 1.6;
    padding: 1.5em;
    background: #fefefe;
  }
  h1, h2, h3 {
    color: #003366;
    text-align: center;
    margin-top: 1.2em;
  }
  hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 2em 0;
  }
</style>
"""

# اقرأ الغلاف أولاً
with open(cover_path, encoding="utf-8") as f:
    cover_html = f.read()

full_html = arabic_css + cover_html + "<div>"

# ثم بقية الفصول
files = sorted(f for f in os.listdir(segments_dir) if f.startswith("unit_") and f.endswith(".html"))
for filename in files:
    with open(os.path.join(segments_dir, filename), encoding="utf-8") as f:
        content = f.read()
    chapter_title = f"<hr><h1>الفصل {filename.split('_')[1].replace('.html','')}</h1>"
    full_html += chapter_title + content

full_html += "</div>"

HTML(string=full_html).write_pdf(output_pdf)
print(f"✅ PDF شامل مع الغلاف تم إنشاؤه بنجاح: {output_pdf}")
