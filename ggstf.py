
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

def colonToSlash(word):
    strW = str(word)
    for i in range(len(strW)):
        if strW[i] == ",":
            strW[i] = "/"
    return strW

url = "https://www.dustloop.com/wiki/index.php?title=GGST/Anji_Mito/Frame_Data"
tmpArr = url.split("/")
charName = tmpArr[len(tmpArr) - 2]

req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
web_byte = urlopen(req).read()

page_html = web_byte.decode("utf-8")
page_soup = soup(page_html, "html.parser")

table = page_soup.findAll("table", {"class": "cargoDynamicTable"})
th = table[0].findAll("th")
with open(charName.lower() + '_normal_df.csv', 'w') as file:
    for i in range(1,12):
        if i == 11:
            file.write(colonToSlash(th[i].text) + "\n")
        else:
            file.write(colonToSlash(th[i].text) + ", ")
    
    td = table[0].findAll("td")
    i = 0 
    for i in range(len(td)):
        if (i % 12 == 0):
            file.write(colonToSlash(th[i].text)+ "\n")
        elif (i == (len(td) - 1)):
            file.write(colonToSlash(th[i].text))
        else:
            file.write(colonToSlash(th[i].text) + ",")
    
with open(charName.lower() + '_special_df.csv', 'w') as file:
    th = table[1].findAll("th")
    for i in range(1,13):
        if i == 12:
            file.write(th[i].text + "\n")
        else:
            file.write(th[i].text + ", ")
    
    td = table[1].findAll("td")
    i = 0 
    for i in range(len(td)):
        if (i % 13 == 0):
            file.write(colonToSlash(th[i].text) + "\n")
        elif (i == (len(td) - 1)):
            file.write(colonToSlash(th[i].text))
        else:
            file.write(colonToSlash(th[i].text) + ",")
    



