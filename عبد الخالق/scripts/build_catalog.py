import json

catalog = [
    {"title": "الفصل الأول: الثقافة الإسلامية", "start": 11, "end": 36},
    {"title": "الفصل الثاني: مصادر الثقافة", "start": 37, "end": 84},
    {"title": "الفصل الثالث: خصائص الثقافة", "start": 85, "end": 114},
    {"title": "الفصل الرابع: الإسلام والعلم", "start": 115, "end": 146},
    {"title": "الفصل الخامس: التحديات الثقافية", "start": 147, "end": 180},
    {"title": "الفصل السادس: الأخلاق في الإسلام", "start": 181, "end": 210},
    {"title": "الفصل السابع: النظم الإسلامية", "start": 211, "end": 284},
    {"title": "الفصل الثامن: الشبهات والردود", "start": 285, "end": 306}
]

with open("/mnt/c/Users/ali/Desktop/عبد الخالق/catalog/catalog_map.json", "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)
print("✅ خريطة الفهرس تم إنشاؤها بنجاح")
