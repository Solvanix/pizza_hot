import os

base_dir = "/mnt/c/Users/ali/Desktop/عبد الخالق"
notes_html = """
<!-- 🖥️ ملاحظة محلية -->
<div style='margin-top:2em; padding:1em; background:#e7f4ff; border:1px solid #90caf9; border-radius:8px;'>
  <h3 style='color:#1565c0;'>🖥️ ملاحظة محلية:</h3>
  <p>هذه الصفحة مُخصصة للاستخدام المحلي فقط على هذا الجهاز، ولم يتم نشرها على الإنترنت بعد.</p>
  <ul>
    <li>✅ مثبتة داخل متصفح <strong>Google Chrome - بروفايل رقم 2</strong></li>
    <li>📱 نسخة الجوال مثبّتة على سطح المكتب في شريط التنقل (Navigation Bar)</li>
    <li>🧭 سيتم عرض نسخة خارجية لاحقًا من خلال أدوات أو واجهات عامة</li>
  </ul>
</div>

<!-- 💡 أدوات التحليل -->
<div style='margin-top:2em; padding:1em; background:#fffbe6; border:1px dashed #f0ad4e; border-radius:8px;'>
  <h3 style='color:#c77500;'>💡 تحليل الملف باستخدام الذكاء الاصطناعي</h3>
  <p>يمكنك فتح هذا الملف في خدمة <strong><a href='https://pdf.ai/' target='_blank'>PDF.ai</a></strong> والتفاعل معه باستخدام الذكاء الاصطناعي.</p>
  <ul>
    <li>💻 قم بتسجيل الدخول باستخدام بريدك الإلكتروني أو حساب Google/GitHub</li>
    <li>📂 حمّل الملف المطلوب من مجلد <code>pdfs/</code></li>
    <li>🔍 ابدأ بطرح الأسئلة عن المحتوى</li>
    <li>⚠️ ملاحظة: النسخة المجانية من PDF.ai غالبًا لا تقبل ملفات أكبر من صفحتين</li>
  </ul>
  <p><strong>خيارات إضافية:</strong> استخدم <a href='https://chatpdf.com' target='_blank'>ChatPDF</a> أو <a href='https://humata.ai' target='_blank'>Humata</a> لتحليل ملفات أكبر دون قيود صارمة.</p>
</div>

<!-- 🧠 النوافذ المثبّتة -->
<div style='margin-top:2em; padding:1em; background:#fff3e0; border:1px solid #ffa726; border-radius:8px;'>
  <h3 style='color:#ef6c00;'>🧠 نوافذ التحليل المثبّتة:</h3>
  <ul>
    <li>📄 نافذة <strong>ChatPDF</strong> تحتوي نسخة تفاعلية من المقرر لتحليل الفصول</li>
    <li>📤 نافذة <strong>Humata.ai</strong> مثبتة ويتم الدخول إليها بالبريد <code>eng.ali.khateb@gmail.com</code></li>
    <li>💬 يمكن استخدامهما مع هذه الصفحة للحصول على تجربة تحليل ذكي متكاملة</li>
  </ul>
</div>
"""

def insert_notes(path):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    if notes_html.strip() in html:
        return
    if "</body>" in html:
        html = html.replace("</body>", f"{notes_html}\n</body>")
        backup = path.replace(".html", ".bak")
        with open(backup, "w", encoding="utf-8") as f: f.write(html)
        with open(path, "w", encoding="utf-8") as f: f.write(html)
        print(f"✅ تم تحديث الملف: {path}")

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            insert_notes(os.path.join(root, file))
