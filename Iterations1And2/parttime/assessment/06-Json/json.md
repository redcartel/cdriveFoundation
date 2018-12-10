## Final Assessment json:

* Open the provided json file containing stock market data

* Output a new json file ```processed.json``` that has the format:

```
{
    "United States Steel Corp": {
        "Symbol": "X",
        "LastPrice": 29.4
    },
    "Exantas Capital Corp": {
        "Symbol": "XAN",
        "LastPrice": 10.76
    },
    etc...
}
```

where each company "Name" from the market data is keyed to a sub-dictionary containing
"Symbol" and "LastPrice."