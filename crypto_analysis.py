import requests

cryptos = ["BTCUSDT","SOLUSDT","XRPUSDT","ETHUSDT"]

for coin in cryptos:
    url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={coin}"
    data = requests.get(url).json()
    price = float(data["lastPrice"])
    change = float(data["priceChangePercent"])
    print(f"#####################  {coin} Analysis ############################")
    print(f"*****live  {coin} price = {price}    *****")
    if change > 0:
        print(f"+{change}")
    elif change < 0 :
        print(change)


