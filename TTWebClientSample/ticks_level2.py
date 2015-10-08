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

    # Account feed ticks level2
    ticks_level2 = client.get_all_ticks_level2()
    for t in ticks_level2:
        print('{0} level2 book depth: {1}'.format(t['Symbol'], max(len(t['Bids']), len(t['Asks']))))

    tick_level2 = client.get_tick_level2(ticks_level2[0]['Symbol'])
    print("{0} level2 book depth: {1}".format(tick_level2[0]['Symbol'],
                                              max(len(tick_level2[0]['Bids']), len(tick_level2[0]['Asks']))))


if __name__ == '__main__':
    main()