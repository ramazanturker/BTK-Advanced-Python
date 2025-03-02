import re

text = "btk academy python tutorials btk"
pattern = "btk"

match = re.search(pattern, text)

result = match
result = match.start()
result = match.end()

match = re.findall(pattern, text)

result = match

print(result)