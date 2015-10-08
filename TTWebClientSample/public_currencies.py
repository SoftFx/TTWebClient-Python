#!/usr/bin/python3
__author__ = 'ivan.shynkarenka'


import argparse
from TTWebClient.TickTraderWebClient import TickTraderWebClient


def main():
    parser = argparse.ArgumentParser(description='TickTrader Web API sample')
    parser.add_argument('web_api_address', help='TickTrader Web API address')
    args = parser.parse_args()

    # Create instance of the TickTrader Web API client
    client = TickTraderWebClient(args.web_api_address)

    # Public currencies
    currencies = client.get_public_all_currencies()
    for c in currencies:
        print('Currency: {0}'.format(c['Name']))

    currency = client.get_public_currency(currencies[0]['Name'])
    print("{0} currency precision: {1}".format(currency[0]['Name'], currency[0]['Precision']))


if __name__ == '__main__':
    main()