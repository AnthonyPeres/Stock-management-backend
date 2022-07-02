import json

def getTickers():
    with open('tickers.json') as json_file:
        data = json.load(json_file)
        return data


def getTicker(ticker):
    print("Get : " + ticker)


def addTicker(ticker):
    print("POST : " + ticker)
    with open('tickers.json', "r+") as json_file:
        data = json.load(json_file)

        if not ticker in data['tickers']:
            data['tickers'].append(ticker)

            with open('tickers.json', "w+") as json_file:
                json.dump(data, json_file)
        else:
            print("Valeur déjà connue")


def removeTicker(ticker):
    print("DEL : " + ticker)

    with open('tickers.json', "r+") as json_file:
        data = json.load(json_file)

    try:
        index = data['tickers'].index(ticker)

        del data["tickers"][index]
    
        with open('tickers.json', "w+") as json_file:
            json.dump(data, json_file)

    except:
        print('Valeur non connue')
