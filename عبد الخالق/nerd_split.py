import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

# 📥 مسار ملف PDF
pdf_path = "/mnt/c/Users/ali/Desktop/عبد الخالق/nerd_book.pdf"

# 📤 مسار ملف HTML الناتج
output_html = "/mnt/c/Users/ali/Desktop/عبد الخالق/ocr_full_analysis.html"

# 📖 فتح ملف PDF
doc = fitz.open(pdf_path)

# ✍️ فتح ملف HTML للكتابة
with open(output_html, "w", encoding="utf-8") as html:
    html.write("<html><head><meta charset='utf-8'><title>تحليل كامل للملف باستخدام OCR</title></head><body>\n")

    for i in range(doc.page_count):
        page = doc.load_page(i)
        pix = page.get_pixmap(dpi=200)  # دقة عالية
        img_data = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_data))

        # 🔍 تطبيق OCR باستخدام اللغة العربية
        text = pytesseract.image_to_string(image, lang="ara")

        # 📄 كتابة النص داخل HTML
        html.write(f"<div class='page'><h2>صفحة {i + 1}</h2><pre>{text}</pre></div>\n")
        print(f"✅ تم تحليل الصفحة {i + 1} / {doc.page_count}")

    html.write("</body></html>")

print("🎯 تم استخراج النص وتحليله إلى HTML بنجاح!")
