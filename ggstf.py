
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

url = "https://www.dustloop.com/wiki/index.php?title=GGST/Anji_Mito/Frame_Data"
tmpArr = url.split("/")
charName = tmpArr[len(tmpArr) - 2]

req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
web_byte = urlopen(req).read()

page_html = web_byte.decode("utf-8")
page_soup = soup(page_html, "html.parser")

table = page_soup.findAll("table", {"class": "cargoDynamicTable"})
th = table[0].findAll("th")
with open(charName.lower() + '_df.csv', 'w') as file:
    for i in range(1,12):
        if i == 11:
            file.write(th[i].text + "\n")
        else:
            file.write(th[i].text + ", ")
    
    td = table[0].findAll("td")
    i = 0 
    while (i < len(td)):
        if (td[i].text == "") and (i % 13 == 0):
            i += 1
        else:
            file.write(td[i].text+ ",")
            i += 1
        if i % 12 == 0:
            file.write("\n")
           
    for i in range(1,3):
        td = table[i].findAll("td")
        while (i < len(td)):
            if td[i].text == "":
                i += 1
            # elif i % 
            else:
                file.write(td[i].text+ ",")
                i += 1
            if i % 12 == 0:
                file.write("\n")
    

