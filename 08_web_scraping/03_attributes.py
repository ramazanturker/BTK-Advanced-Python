from bs4 import BeautifulSoup

with open("08_web_scraping/index.html", encoding = "utf-8") as file:
    html = file.read()

object = BeautifulSoup(html, "html.parser")

result = object.div
result = object.find("div")
result = object.find(id="item1")
result = object.find(id="item2")
result = object.find(id="header")
result = object.find(class_="item")
result = object.find_all(class_="item")[1]

result = object.select("#header")
result = object.select("#item1")
result = object.select(".item")

result = object.select_one(".item")
result = object.select_one("#item1")

result = object.div.attrs["id"]
result = object.div.attrs["class"]

result = object.ul.get_text(strip=True, separator="-")

for a in object.div.find_all("a"):
    # print(a.get("href"))
    print(a["href"])