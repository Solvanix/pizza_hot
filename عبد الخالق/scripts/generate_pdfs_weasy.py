import os
from weasyprint import HTML

segments_dir = "/mnt/c/Users/ali/Desktop/عبد الخالق/segments/"
output_dir = "/mnt/c/Users/ali/Desktop/عبد الخالق/pdfs/"
os.makedirs(output_dir, exist_ok=True)

arabic_css = """
<style>
  @font-face {
    font-family: 'Amiri';
    src: url('file:///mnt/c/Users/ali/Desktop/عبد الخالق/fonts/Amiri-1.002/Amiri-Regular.ttf');
  }
  body {
    font-family: 'Amiri', serif;
    direction: rtl;
    unicode-bidi: bidi-override;
    line-height: 1.6;
    padding: 1em;
  }
  h1, h2, h3 {
    color: #003366;
    text-align: center;
  }
</style>
"""

files = sorted(f for f in os.listdir(segments_dir) if f.startswith("unit_") and f.endswith(".html"))

for filename in files:
    input_path = os.path.join(segments_dir, filename)
    output_path = os.path.join(output_dir, filename.replace(".html", ".pdf"))

    with open(input_path, encoding="utf-8") as f:
        raw_html = f.read()

    full_html = arabic_css + raw_html

    HTML(string=full_html).write_pdf(output_path)
    print(f"✅ PDF بخط Amiri تم إنشاؤه: {output_path}")
