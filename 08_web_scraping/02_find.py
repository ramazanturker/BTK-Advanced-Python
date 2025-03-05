from bs4 import BeautifulSoup

with open("08_web_scraping/index.html", encoding = "utf-8") as file:
    html = file.read()

object = BeautifulSoup(html, "html.parser")

result = object.div
result = object.find("div")
result = object.find_all("div")
result = len(object.find_all("div"))
result = object.find_all("div")[1].h2
result = object.find_all("div")[1].ul
result = object.find_all("div")[1].ul.find_all("li")[2]
result = object.find_all("div")[1].ul.find_all("li")[2].string

for div in object.find_all("div"):
    if div.h2.a != None:
        print(div.h2.a.string.strip())
    else:
        print(div.h2.string.strip())

for a in object.find_all("a"):
    print(a)