#!/usr/bin/python3
__author__ = 'ivan.shynkarenka'


import argparse
from TTWebClient.TickTraderWebClient import TickTraderWebClient


def main():
    parser = argparse.ArgumentParser(description='TickTrader Web API sample')
    parser.add_argument('web_api_address', help='TickTrader Web API address')
    parser.add_argument('web_api_id', default=None, help='TickTrader Web API Id')
    parser.add_argument('web_api_key', default=None, help='TickTrader Web API Key')
    parser.add_argument('web_api_secret', default=None, help='TickTrader Web API Secret')
    args = parser.parse_args()

    # Create instance of the TickTrader Web API client
    client = TickTraderWebClient(args.web_api_address, args.web_api_id, args.web_api_key, args.web_api_secret)

    # Account trades
    trades = client.get_all_trades()
    for t in trades:
        print('{0} trade with type {1} by symbol {2}: {3}'.format(t['Id'], t['Type'], t['Symbol'], t['Amount']))

    trade = client.get_trade(trades[0]['Id'])
    print('{0} trade with type {1} by symbol {2}: {3}'.format(trade['Id'],
                                                              trade['Type'],
                                                              trade['Symbol'],
                                                              trade['Amount']))


if __name__ == '__main__':
    main()