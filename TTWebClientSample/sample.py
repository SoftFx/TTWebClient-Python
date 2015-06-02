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

    print('--- Public Web API methods ---')

    # Public trade session status
    public_trade_session = client.get_public_trade_session_status()
    print('TickTrader name: {0}'.format(public_trade_session['PlatformName']))
    print('TickTrader company: {0}'.format(public_trade_session['PlatformCompany']))
    print('TickTrader timezone offset: {0}'.format(public_trade_session['PlatformTimezoneOffset']))
    print('TickTrader session status: {0}'.format(public_trade_session['SessionStatus']))

    # Public currencies
    currencies = client.get_public_all_currencies()
    for c in currencies:
        print('Currency: {0}'.format(c['Name']))

    currency = client.get_public_currency(currencies[0]['Name'])
    print("{0} currency precision: {1}".format(currency['Name'], currency['Precision']))

    # Public symbols
    symbols = client.get_public_all_symbols()
    for s in symbols:
        print('Symbol: {0}'.format(s['Symbol']))

    symbol = client.get_public_symbol(symbols[0]['Symbol'])
    print("{0} symbol precision: {1}".format(symbol['Symbol'], symbol['Precision']))

    # Public feed ticks
    ticks = client.get_public_all_ticks()
    for t in ticks:
        print('{0} tick: {1} {2}'.format(t['Symbol'], t['BestBid']['Price'], t['BestAsk']['Price']))

    tick = client.get_public_tick(ticks[0]['Symbol'])
    print("{0} tick timestamp: {1}".format(tick['Symbol'], tick['Timestamp']))

    # Public feed level2 ticks
    ticks_level2 = client.get_public_all_ticks_level2()
    for t in ticks_level2:
        print('{0} level2 book depth: {1}'.format(t['Symbol'], max(len(t['Bids']), len(t['Asks']))))

    tick_level2 = client.get_public_tick_level2(ticks_level2[0]['Symbol'])
    print("{0} level2 book depth: {1}".format(tick_level2['Symbol'],
                                              max(len(tick_level2['Bids']), len(tick_level2['Asks']))))

    print('--- Web API client methods ---')

    # Currencies
    currencies = client.get_all_currencies()
    for c in currencies:
        print('Currency: {0}'.format(c['Name']))

    currency = client.get_currency(currencies[0]['Name'])
    print("{0} currency precision: {1}".format(currency['Name'], currency['Precision']))

    # Symbols
    symbols = client.get_all_symbols()
    for s in symbols:
        print('Symbol: {0}'.format(s['Symbol']))

    symbol = client.get_symbol(symbols[0]['Symbol'])
    print("{0} symbol precision: {1}".format(symbol['Symbol'], symbol['Precision']))

    # Feed ticks
    ticks = client.get_all_ticks()
    for t in ticks:
        print('{0} tick: {1} {2}'.format(t['Symbol'], t['BestBid']['Price'], t['BestAsk']['Price']))

    tick = client.get_tick(ticks[0]['Symbol'])
    print("{0} tick timestamp: {1}".format(tick['Symbol'], tick['Timestamp']))

    # Feed level2 ticks
    ticks_level2 = client.get_all_ticks_level2()
    for t in ticks_level2:
        print('{0} level2 book depth: {1}'.format(t['Symbol'], max(len(t['Bids']), len(t['Asks']))))

    tick_level2 = client.get_tick_level2(ticks_level2[0]['Symbol'])
    print("{0} level2 book depth: {1}".format(tick_level2['Symbol'],
                                              max(len(tick_level2['Bids']), len(tick_level2['Asks']))))

    # Trade session status
    trade_session = client.get_trade_session_status()
    print('Trade session status: {0}'.format(trade_session['SessionStatus']))

    # Account info
    account = client.get_account()
    print('Account Id: {0}'.format(account['Id']))
    print('Account name: {0}'.format(account['Name']))
    print('Account group: {0}'.format(account['Group']))

    # Account assets
    if account['AccountingType'] == 'Cash':
        assets = client.get_all_assets()
        for a in assets:
            print('{0} asset: {1}'.format(a['Currency'], a['Amount']))

    # Account positions
    if account['AccountingType'] == 'Net':
        positions = client.get_all_positions()
        for p in positions:
            print('{0} position: {1} {2}'.format(p['Symbol'], p['LongAmount'], p['ShortAmount']))

    # Account trades
    trades = client.get_all_trades()
    for t in trades:
        print('{0} trade with type {1} by symbol {2}: {3}'.format(t['Id'], t['Type'], t['Symbol'], t['Amount']))

    trade = client.get_trade(trades[0]['Id'])
    print('{0} trade with type {1} by symbol {2}: {3}'.format(trade['Id'],
                                                              trade['Type'],
                                                              trade['Symbol'],
                                                              trade['Amount']))

    # Create limit order
    if (account['AccountingType'] == 'Gross') or (account['AccountingType'] == 'Net'):
        limit = client.create_trade(
            {
                'Type': 'Limit',
                'Side': 'Buy',
                'Symbol': 'EURUSD' if (account['AccountingType'] == 'Gross') else 'EUR/USD',
                'Amount': 10000,
                'Price': 1.0,
                'Comment': 'Buy limit from Web API sample'
            })

        limit = client.modify_trade(
            {
                'Id': limit['Id'],
                'Comment': 'Modified limit from Web API sample'
            })

        client.cancel_trade(limit['Id'])


if __name__ == '__main__':
    main()