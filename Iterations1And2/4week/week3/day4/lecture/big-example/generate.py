
from random import randint

letters = "abcdefghijklmnopqrstuvwxyz"
def random_str():
    string = ""
    for _ in range(randint(2,6)):
        string = string + letters[randint(0,25)]
    return string

row = lambda n: [random_str() + ": {}".format(randint(1,1000)) for _ in range(n)]
table = [row(10) for _ in range(100)]


with open("table.html", "w") as file_object:
    print("<table id='#data' class='table'>", file=file_object)
    for row in table:
        _class = "row"
        if randint(1,3) == 3:
            _class += " highlight"
        print("\t<tr class='{}'>".format(_class), file=file_object)
        for element in row:
            _tdclass = "element"
            if randint(1,10) == 3:
                _tdclass += " important"
            print("\t\t<td class='{}'>".format(_tdclass), file=file_object)
            print("\t\t\t{}".format(element), file=file_object)
            print("\t\t</td>", file=file_object)
        print("\t</tr>", file=file_object)
    print("</table>", file=file_object)
