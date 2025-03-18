import requests
from http import HTTPStatus

def get_symbols(currency_code):
    url = "https://bitpay.com/currencies"
    response = requests.get(url)

    if response.status_code != HTTPStatus.OK:
        return 'Something happened with https://bitpay.com'

    data = response.json()
    currencies = data.get("data", [])

    for currency in currencies:
        if currency["code"] == currency_code and not currency.get("crypto", False):
            return currency["symbol"]