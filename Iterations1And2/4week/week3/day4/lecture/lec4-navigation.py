
soup = BeautifulSoup(html, "html.parser")
tag = soup.body
contents = soup.body.contents[1]
print(contents)
contents.next_sibling
element.parent
element.previous_sibling

find_parent
find_previous_sibling
data = soup.select()

