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

    iterations = 3
    request = {'TimestampTo':TickTraderWebClient.get_timestamp(), 'RequestDirection':'Backward', 'RequestPageSize':10}

    # Try to get trade history from now to the past. Request is limited to 30 records!
    while iterations > 0:
        report = client.get_trade_history(request)
        for record in report['Records']:
            print('TradeHistory record: Id={0}, TransactionType={1}, TransactionReason={2}, Symbol={3}, TradeId={4}'
                  .format(record.get('Id', ''),
                          record.get('TransactionType', ''),
                          record.get('TransactionReason', ''),
                          record.get('Symbol', ''),
                          record.get('TradeId', '')))
            request['RequestLastId'] = record['Id']
        # Stop for last report
        if report['IsLastReport']:
            break
        iterations -= 1


if __name__ == '__main__':
    main()