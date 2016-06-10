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

    # Create, modify and cancel limit order
    account = client.get_account()

    # Create limit order
    limit = client.create_trade(
        {
            'Type': 'Limit',
            'Side': 'Buy',
            'Symbol': 'BTCUSD',
            'Amount': 0.1,
            'Price': 200.0,
            'Comment': 'Buy limit from Web API sample'
        })

    # Modify limit order
    limit = client.modify_trade(
        {
            'Id': limit['Id'],
            'Comment': 'Modified limit from Web API sample'
        })

    # Cancel limit order
    client.cancel_trade(limit['Id'])


if __name__ == '__main__':
    main()