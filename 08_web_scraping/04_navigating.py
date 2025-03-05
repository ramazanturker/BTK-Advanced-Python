from bs4 import BeautifulSoup

with open("08_web_scraping/index.html", encoding = "utf-8") as file:
    html = file.read()

object = BeautifulSoup(html, "html.parser")

result = object.body.div.contents[3]

# for i in object.body.div.children:
#     print(i)

# for i in object.body.div.descendants:
#     print(i)

result = object.body.h2.parent
result = object.body.h2.parent.parent

result = object.body.ul.next_element.next_element

result = object.body.div.next_sibling.next_sibling
result = object.body.div.find_next_sibling("div").find_next_sibling("div").find_previous_sibling("div")

print(result)