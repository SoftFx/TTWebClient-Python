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

    # Account feed ticks
    ticks = client.get_all_ticks()
    for t in ticks:
        print('{0} tick: {1} {2}'.format(t['Symbol'], t['BestBid']['Price'], t['BestAsk']['Price']))

    tick = client.get_tick(ticks[0]['Symbol'])
    print("{0} tick timestamp: {1}".format(tick[0]['Symbol'], tick[0]['Timestamp']))


if __name__ == '__main__':
    main()