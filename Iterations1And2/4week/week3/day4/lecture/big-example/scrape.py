from bs4 import BeautifulSoup
import requests
import re

html = requests.get("http://127.0.0.1:5000").text
soup = BeautifulSoup(html, "html.parser")

def show(n):
    if n == 1:
        print(soup)
        print(type(soup))
    
    if n ==2:
        title = soup.select("div.jumbotron h1")[0].get_text()
        print("the title is: ")
        print(title)
    
    if n ==3:
        blocks = soup.select(".container .row .col-md-4")
        for block in blocks:
            if block.find("h2"):
                text = block.find("p").get_text()
                if re.search("second little", text):
                    print("found this text that matches:")
                    print(text)

    if n == 4:
        rows = soup.select("table tr")
        rownum = 0
        for row in rows:
            elements = row.find_all("td")
            elementnum = 0
            for element in elements:
                if "important" in element.attrs.get("class", []):
                    print("row {}, element {} imporant".format(rownum, elementnum))
                    result = re.search("(\w+):\s*(\d+)", element.get_text())
                    name, num = result.groups()
                    print("    name: {}, num {}".format(name, num))
                elementnum += 1
            rownum += 1
