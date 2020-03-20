import datetime
from finnhub import client as Finnhub
import requests
from .apikey import token
from flask import Flask, Blueprint, jsonify

quote_url = "https://finnhub.io/api/v1/quote"

client = Finnhub.Client(api_key=token())

quoter = Blueprint('quoter', __name__)

@quoter.route('/quote/<companyName>', methods=['GET'])
def quote(companyName):
    result = client.quote(symbol=companyName)
    timestamp = datetime.datetime.fromtimestamp(result["t"])

    return jsonify({'companyName' : companyName, 'currentPrice': result["c"], 'highPrice': result["h"], 'lowPrice': result["l"], 'openingPrice': result["o"],
    'timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S')}), 200

if __name__ == '__main__':
    client = Finnhub.Client(api_key=token())
    while 1:

        companyName = input('What company stock prices would you like to see (symbol) ? ')
        if companyName == 'quit':
            break
        result = client.quote(symbol=companyName)
        timestamp = datetime.datetime.fromtimestamp(result["t"])


        print('company name: {0}\ncurrent price: ${1}\nhigh price: ${2}\nlow price: ${3}\nopening price: ${4}\nprevious close price: ${5}\ntimestamp of current daily bar: {6}'.format(companyName, 
        result["c"], result["h"], result["l"], result["o"], result["pc"], timestamp.strftime('%Y-%m-%d %H:%M:%S')))