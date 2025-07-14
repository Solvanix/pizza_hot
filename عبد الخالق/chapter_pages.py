from bs4 import BeautifulSoup

html_path = "/mnt/c/Users/ali/Desktop/عبد الخالق/ocr_full_analysis.html"
keywords = ["الفصل", "الباب", "العقيدة", "المقدمة", "الخاتمة"]

with open(html_path, encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

for div in soup.find_all("div", class_="page"):
    page_title = div.find("h2").text.strip()
    page_num = int(page_title.replace("صفحة", "").strip())
    content = div.get_text()

    for keyword in keywords:
        if keyword in content:
            print(f"📘 الكلمة '{keyword}' موجودة في صفحة {page_num}")
            break
