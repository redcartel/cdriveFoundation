

element.get_text() # content text
element.name # not a method, returns the tag name
element.attrs # dictionary containing attributes (including id and class, class will be a list

# chain methods:
soup.find("h3").get_text()

