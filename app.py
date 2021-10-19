from flask import Flask, render_template, request, url_for
import requests
import sys

app = Flask(__name__)

exchanges = ['Kraken', 'Binance']
currencies = ['Bitcoin', 'Ethereum']
currencyToSymbol = {
    "Bitcoin": "btcusdt",
    "Ethereum": "ethusdt"
}

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", exchanges=exchanges, currencies=currencies)

@app.route('/form', methods=['GET', 'POST'])
def form():
    currencyInfo = {}
    if request.method == "POST":

        curr = request.form.get("currencySelect")

        for e in exchanges:
            req = requests.get("https://api.cryptowat.ch/markets/{}/{}/orderbook?limit=1".format(e.lower(), currencyToSymbol[curr]))
            req = req.json()
            currencyInfo[e] = req

        #print(curr, flush=True)

        bestBuy = ""
        bestBuyPrice = 999999999
        bestSell = ""
        bestSellPrice = 0

        for i in currencyInfo.keys():
            if currencyInfo[i]["result"]["asks"][0][0] < bestBuyPrice:
                bestBuyPrice = currencyInfo[i]["result"]["asks"][0][0]
                bestBuy = i

            if currencyInfo[i]["result"]["bids"][0][0] > bestSellPrice:
                bestSellPrice = currencyInfo[i]["result"]["bids"][0][0]
                bestSell = i

    return render_template("index.html", exchanges=exchanges, currencies=currencies, curr=curr, currencyInfo=currencyInfo, bestBuy=bestBuy, bestSell=bestSell)

if __name__=='__main__':
    app.run(debug=True)