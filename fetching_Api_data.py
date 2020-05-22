import requests
import json
api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=332c0fe8-fcfe-410a-a7bb-85c61fe285ff")
api=json.loads(api_request.content)
print(api)
