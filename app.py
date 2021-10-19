from flask import Flask, render_template, request, url_for
import requests
import sys
import json

app = Flask(__name__)

exchanges = ['Kraken', 'Binance', 'Bitstamp', 'Bitfinex', 'Coinbase-Pro', "FTX", "Bitbay"]
currencies = ['Bitcoin', 'Ethereum']
currencyToSymbol = {
    "Bitcoin": "btcusdt",
    "Ethereum": "ethusdt"
}

#landing point
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", exchanges=exchanges, currencies=currencies)

#launches when button is submitted for crypto choice
@app.route('/form', methods=['GET', 'POST'])
def form():
    currencyInfo = {}
    validExchanges = []
    #get response from dropdown menu
    if request.method == "POST":

        curr = request.form.get("currencySelect")

        for e in exchanges:
            req = requests.get("https://api.cryptowat.ch/markets/{}/{}/orderbook?limit=1".format(e.lower(), currencyToSymbol[curr]))
            req_json = req.json()

            #check if exchange+symbol pair has no market
            json_dict = json.loads(req.text)
            if "error" in json_dict:
                print("nonexistent market/symbol pair - {}".format(e), flush=True)
                continue
            validExchanges.append(e)
            currencyInfo[e] = req_json

        #print(curr, flush=True)

        #get recommended place tobuy/sell currency from all exchanges
        bestBuy = ""
        bestBuyPrice = 999999999
        bestSell = ""
        bestSellPrice = 0

        print(currencyInfo.keys(), flush=True)
        for i in currencyInfo.keys():
            if currencyInfo[i]["result"]["asks"][0][0] < bestBuyPrice:
                bestBuyPrice = currencyInfo[i]["result"]["asks"][0][0]
                bestBuy = i

            if currencyInfo[i]["result"]["bids"][0][0] > bestSellPrice:
                bestSellPrice = currencyInfo[i]["result"]["bids"][0][0]
                bestSell = i
    #re-render page with new information gotten
    return render_template("index.html", exchanges=validExchanges, currencies=currencies, curr=curr, currencyInfo=currencyInfo, bestBuy=bestBuy, bestSell=bestSell)

if __name__=='__main__':
    app.run(debug=True)