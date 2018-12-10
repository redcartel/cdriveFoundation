import requests
import json


def lookup(symbol):
    URL = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol={}"
    try:
        response = requests.get(URL.format(symbol))
        jsonstring = response.text
    except:
        return None
    dictionary = json.loads(jsonstring)
    return dictionary['LastPrice']


if __name__ == "__main__":
    symbol = input("Give me a stock symbol: ")
    value = lookup(symbol)
    if not value:
        print("Error looking up value.")
        quit()
    print("Most recent value: {}".format(value))