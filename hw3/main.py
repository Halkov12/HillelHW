from http import HTTPStatus

from flask import Flask, request, send_file
from faker import Faker
import pandas as pd
import requests
import httpx
from webargs import fields, validate
from webargs.flaskparser import  use_kwargs

from hw3.getsymbols import get_symbols
from hw3.validator import generate_students_validator, bitcoin_value_validator

app = Flask(__name__)
@app.route("/generate_students")
@use_kwargs(
    generate_students_validator,
    location="query",
)
def generate_students(count):
    fake = Faker(locale='en_US')
    data = {
        'first_name': [],
        'last_name': [],
        'email': [],
        'password': [],
        'birthday': [],
    }

    for _ in range(count):
        data['first_name'].append(fake.first_name())
        data['last_name'].append(fake.last_name())
        data['email'].append(fake.email())
        data['password'].append(fake.password())
        data['birthday'].append(fake.date_of_birth(minimum_age=18, maximum_age=60))

    df = pd.DataFrame(data)
    df.to_csv('students.csv', index=False)
    return data


@app.route("/get_bitcoin_value")
@use_kwargs(
    bitcoin_value_validator,
    location="query",
)
def get_bitcoin_value(currency, convert):
    url = 'https://bitpay.com/api/rates/'
    response = requests.get(url + currency)

    if response.status_code != HTTPStatus.OK:
        return 'Something happened with https://bitpay.com/api'





    result = response.json()
    return f'{convert} Bitcoin is: {int(result['rate'] * convert)} {get_symbols(currency)} ({result['name']})'


if __name__ == "__main__":
    app.run(
        debug=True,
        host="localhost",
    )
