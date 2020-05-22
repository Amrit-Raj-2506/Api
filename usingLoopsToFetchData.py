import requests
import json
api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=332c0fe8-fcfe-410a-a7bb-85c61fe285ff")
api=json.loads(api_request.content)
coins=("ESO","BCH")
for i in range (0,5):
    for coin in coins :
        if api["data"][i]["symbol"]==coin:

            print(api["data"][i]["symbol"])
            print("{0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("--------------------")
