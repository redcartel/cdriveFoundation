import requests
import json


def lookup(symbol):
    URL = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol={}"
    try:
        response = requests.get(URL.format(symbol))
        jsonstring = response.text
        dictionary = json.loads(jsonstring)
    except:
        return None
    return dictionary


if __name__ == "__main__":
    symbols = ['X',
    'XAN',
    'XEC',
    'XFLT',
    'XHR',
    'XIN',
    'XL',
    'XOM',
    'XOXO',
    'XPO',
    'XRF',
    'XRM',
    'XRX',
    'XYF',
    'XYL']
    dictionary = {}
    for ticker in symbols:
        print(".")
        info = lookup(ticker)
        if info:
            dictionary[ticker] = info
        with open("market-data.json", "w") as file_object:
            json.dump(dictionary, file_object, indent=1)
