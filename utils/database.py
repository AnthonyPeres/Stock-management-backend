import json

def getTickers():
    with open('tickers.json') as json_file:
        data = json.load(json_file)
        return data


def getTicker(ticker):
    print("Get : " + ticker)

def addTicker(ticker):
    print("POST : " + ticker)
    # with open('tickers.json', "r+") as json_file:
    #     data = json.load(json_file)
    #     data['tickers'].append(ticker)
    #     json.dump(data, json_file)


def removeTicker(ticker):
    print("DEL : " + ticker)

