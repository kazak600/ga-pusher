import os
import logging
import random
import requests
from time import sleep

# Currency
CURRENCY_URL = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

# Google Measurement Protocol
GMP_URL = 'https://www.google-analytics.com/mp/collect'
MEASUREMENT_ID = os.getenv('MEASUREMENT_ID')
SECRET = os.getenv('SECRET')


def main():
    response = requests.get(url=CURRENCY_URL)
    data = response.json()
    currency_map = {item['cc']: item for item in data}
    usd_item = currency_map['USD']

    payload = {
        'client_id': '777-777',
        'events': [
            {
                'name': 'usd_rate',
                'params': {
                    'currency': 'USD',
                    'value': round(usd_item['rate'], 2),
                    'items': [{'item_id': str(random.randint(1, 10000))}]
                }
            }
        ]
    }
    ga_response = requests.post(
        url=f'{GMP_URL}?api_secret={SECRET}&measurement_id={MEASUREMENT_ID}',
        json=payload,
        headers={'Content-Type': 'application/json'}
    )
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(ga_response)


if __name__ == '__main__':
    while True:
        try:
            main()
            sleep(60)
        except KeyboardInterrupt:
            break
