import datetime
from finnhub import client as Finnhub
import requests
from .apikey import token
from flask import Flask, Blueprint, jsonify

quote_url = "https://finnhub.io/api/v1/quote"

client = Finnhub.Client(api_key=token())

quoter = Blueprint('quoter', __name__)

@quoter.route('/quote', defaults = {'companyName' : 'AMZN'})
@quoter.route('/quote/<companyName>', methods=['GET'])
def quote(companyName):
    result = client.quote(symbol=companyName)
    timestamp = datetime.datetime.fromtimestamp(result["t"])

    return jsonify({'company name' : companyName, 'current price': result["c"], 'high price': result["h"], 'low price': result["l"], 
    'timestamp of current daily bar': timestamp.strftime('%Y-%m-%d %H:%M:%S')}), 200

if __name__ == '__main__':
    client = Finnhub.Client(api_key=token())
    while 1:

        companyName = input('What company stock prices would you like to see (symbol) ? ')
        if companyName == 'quit':
            break
        result = client.quote(symbol=companyName)
        timestamp = datetime.datetime.fromtimestamp(result["t"])


        print('company name: ${0}\ncurrent price: ${1}\nhigh price: ${2}\nlow price: ${3}\nprevious close price: ${4}\ntimestamp of current daily bar: {5}'.format(result["c"], result["h"], 
        result["l"], result["o"], result["pc"], timestamp.strftime('%Y-%m-%d %H:%M:%S')))