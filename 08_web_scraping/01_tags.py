from bs4 import BeautifulSoup


with open("08_web_scraping/index.html") as file:
    html = file.read()

object = BeautifulSoup(html, "html.parser")

result = object
result = type(object)
result = type(html)
result = object.prettify()
result = object.title
result = type(object.title)
result = object.title.name
result = object.title.string

result = object.body
result = object.body.h1
result = object.body.h1.string
result = object.h1.string

result = object.div
result = object.h2
result = object.ul
result = object.ul.li

print(result)