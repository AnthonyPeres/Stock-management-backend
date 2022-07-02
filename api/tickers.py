from distutils.log import debug

from utils.database import getTickers, getTicker, removeTicker, addTicker
from flask import Flask, request, Blueprint
from flask_cors import CORS, cross_origin
import json
from markupsafe import escape

tickers_manager = Blueprint('tickers_manager', __name__)

@tickers_manager.route('/api/tickers', methods=['GET'])
def get_tickers():
    tickers = getTickers()
    return tickers


@tickers_manager.route('/api/tickers/<ticker>', methods=['GET', 'POST', 'DELETE'])
def tickers(ticker):
    if request.method == 'POST':
        addTicker(""+escape(ticker))
        return f"Post ticker {escape(ticker)}"
    elif request.method == 'DELETE':
        removeTicker(""+escape(ticker))
        return f"Post ticker {escape(ticker)}"
    else:
        getTicker(""+escape(ticker))
        return f"Get ticker {escape(ticker)}"