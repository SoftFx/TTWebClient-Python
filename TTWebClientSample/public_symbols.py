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

    # Public symbols
    symbols = client.get_public_all_symbols()
    for s in symbols:
        print('Symbol: {0}'.format(s['Symbol']))

    symbol = client.get_public_symbol(symbols[0]['Symbol'])
    print("{0} symbol precision: {1}".format(symbol['Symbol'], symbol['Precision']))


if __name__ == '__main__':
    main()