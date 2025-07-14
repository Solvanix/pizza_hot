import os
from weasyprint import HTML

base = "/mnt/c/Users/ali/Desktop/عبد الخالق"
segments_dir = f"{base}/segments/"
cover_path    = f"{base}/cover.html"
toc_path      = f"{base}/toc.html"
output_pdf    = f"{base}/pdfs/full_document.pdf"
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

def read_html(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

full_html = arabic_css
full_html += read_html(cover_path)
full_html += read_html(toc_path)
full_html += "<div>"

files = sorted(f for f in os.listdir(segments_dir) if f.startswith("unit_") and f.endswith(".html"))
for filename in files:
    content = read_html(os.path.join(segments_dir, filename))
    title = f"<hr><h1>الفصل {filename.split('_')[1].replace('.html','')}</h1>"
    full_html += title + content

full_html += "</div>"

HTML(string=full_html).write_pdf(output_pdf)
print(f"✅ PDF شامل بالغلاف والفهرس تم إنشاؤه بنجاح: {output_pdf}")
