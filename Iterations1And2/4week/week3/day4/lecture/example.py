from bs4 import BeautifulSoup
import requests

html = requests.get("http://www.example.com").text
soup = BeautifulSoup(html, "html.parser")

def show(n):
    if n == 1:
        print(soup)
        print(type(soup))
    
    elif n == 2:
        print(soup.body)
        print(type(soup.body))
    
    elif n == 3:
        # find finds tags by name
        print(soup.body.find("div"))
    
    elif n == 4:
        print(soup.body.find("div").find("h1"))
    elif n == 5:
        print(soup.find_all("div"))
    elif n == 6:
        print(soup.select("body div p a"))
    elif n == 7:
        a = soup.select("body div p a")
        print(a[0].get_text())
        print(a[0].attrs)
        href = a[0].attrs.get("href", None)
        if href:
            print(requests.get(href).text)
