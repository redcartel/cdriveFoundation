from bs4 import BeautifulSoup

with open("example.html", 'r') as file_object:
    html_string = file_object.read()

soup = BeautifulSoup(html_string, "html.parser")

# find & find_all

# print(soup)
# print(type(soup))

print(soup.body)
print(soup.body.div)
div = soup.body.find("div")
print(div)
print(type(div))
divs = soup.body.find_all("div")
print(divs)
print(type(divs))
first = soup.body.find(id='first')
specials = soup.find_all(_class='menuitem')
attrs = soup.find_all(attrs={'data-example': 'yes'})
print(d)
