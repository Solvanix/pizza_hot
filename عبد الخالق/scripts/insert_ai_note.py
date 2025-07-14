import os

base_dir = "/mnt/c/Users/ali/Desktop/عبد الخالق"
note_html = '''
<!-- قسم الذكاء الاصطناعي -->
<div style="margin-top:2em; padding:1em; background:#fffbe6; border:1px dashed #f0ad4e; border-radius:8px;">
  <h3 style="color:#c77500;">💡 تحليل الملف باستخدام الذكاء الاصطناعي</h3>
  <p>يمكنك فتح هذا الملف في خدمة <strong><a href="https://pdf.ai/" target="_blank">PDF.ai</a></strong> والتفاعل معه باستخدام الذكاء الاصطناعي.</p>
  <ul>
    <li>💻 اضغط على الرابط وافتح الموقع</li>
    <li>📂 حمّل الملف المطلوب من مجلد <code>pdfs/</code></li>
    <li>🔍 ابدأ بطرح أسئلتك عن المحتوى</li>
    <li>⚠️ يتطلب التسجيل بحساب مجاني لتفعيل الخدمة</li>
  </ul>
  <p><strong>خيار إضافي:</strong> يمكنك أيضًا استخدام أدوات مثل <a href="https://chatpdf.com" target="_blank">ChatPDF</a> أو <a href="https://humata.ai" target="_blank">Humata</a> لتحليل محتوى الملف مباشرة.</p>
</div>
'''

def insert_note_to_html(path):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    if note_html.strip() in html:
        return  # تم إدراجه مسبقًا
    if "</body>" in html:
        html = html.replace("</body>", f"{note_html}\n</body>")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ تمت إضافة الملاحظة إلى: {path}")

# تصفّح جميع ملفات HTML داخل المشروع
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            insert_note_to_html(os.path.join(root, file))
