import os
from xhtml2pdf import pisa

segments_dir = "/mnt/c/Users/ali/Desktop/عبد الخالق/segments/"
output_dir = "/mnt/c/Users/ali/Desktop/عبد الخالق/pdfs/"
os.makedirs(output_dir, exist_ok=True)

arabic_css = """
<style>
  body {
    font-family: 'Arial', 'Amiri', 'Traditional Arabic', sans-serif;
    direction: rtl;
    unicode-bidi: bidi-override;
    line-height: 1.6;
  }
  h1, h2, h3 { color: #003366; }
</style>
"""

files = sorted(f for f in os.listdir(segments_dir) if f.startswith("unit_") and f.endswith(".html"))

for filename in files:
    input_path = os.path.join(segments_dir, filename)
    output_path = os.path.join(output_dir, filename.replace(".html", ".pdf"))

    with open(input_path, encoding="utf-8") as f:
        html_content = f.read()

    final_html = arabic_css + html_content

    with open(output_path, "wb") as result:
        pisa_status = pisa.CreatePDF(final_html, dest=result)
        if pisa_status.err:
            print(f"❌ فشل إنشاء PDF من {filename}")
        else:
            print(f"✅ PDF محسّن تم إنشاؤه: {output_path}")
