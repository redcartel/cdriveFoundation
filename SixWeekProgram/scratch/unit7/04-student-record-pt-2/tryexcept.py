import json

try:
    file_object = open("results.json", "r")
    data = json.load(file_object)
except FileNotFoundError:
    data = {}


try:
    myint = int(input("input an integer"))
except ValueError:
    myint = 0
