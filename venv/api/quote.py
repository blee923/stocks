import datetime
from finnhub import client as Finnhub
import requests
import apikey

quote_url = "https://finnhub.io/api/v1/quote"

client = Finnhub.Client(api_key=token)



if __name__ == '__main__':
    client = Finnhub.Client(api_key=token)
    while 1:

        companyName = input('What company stock prices would you like to see (symbol) ? ')
        if companyName == 'quit':
            break
        result = client.quote(symbol=companyName)
        timestamp = datetime.datetime.fromtimestamp(result["t"])


        print('company name: ${0}\ncurrent price: ${1}\nhigh price: ${2}\nlow price: ${3}\nprevious close price: ${4}\ntimestamp of current daily bar: {5}'.format(result["c"], result["h"], 
        result["l"], result["o"], result["pc"], timestamp.strftime('%Y-%m-%d %H:%M:%S')))