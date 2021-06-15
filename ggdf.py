from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

url = "https://www.dustloop.com/wiki/index.php?title=GGST/May"
tmpArr = url.split("/")
charName = tmpArr[len(tmpArr) - 1]
print(charName)
req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
web_byte = urlopen(req).read()
page_html = web_byte.decode("utf-8")
page_soup = soup(page_html, "html.parser")
headers = page_soup.findAll("h3")
ssMove = page_soup.findAll("span", {"class": "input-badge"})
with open(charName.lower() + '_header.txt', 'w') as file:
    for i in range(len(headers)):
        if (headers[i].big):
            if len(headers[i].big.text) < 5 or headers[i].big.text == "Ground Throw" or headers[i].big.text == "Air Throw":
                file.write(headers[i].big.text + "\n")
    for i in range(len(ssMove)):
        if (ssMove[i].b):
            file.write(ssMove[i].b.text + "\n")
