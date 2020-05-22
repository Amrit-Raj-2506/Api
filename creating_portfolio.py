import requests
import json
api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=332c0fe8-fcfe-410a-a7bb-85c61fe285ff")
api=json.loads(api_request.content)
coins=[
    {
        "symbol":"BTC",
        "ammount_owned":2,
        "price_per_coin":3200
    },
    {
        "symbol":"ETH",
        "ammount_owned":100,
        "price_per_coin":2.05
    }
]
for i in range (0,5):
    for coin in coins :
        if api["data"][i]["symbol"]==coin["symbol"]:

            print(api["data"][i]["name"]+" --"+api["data"][i]["symbol"])
            print("{0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("--------------------")
