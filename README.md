# TTWebClient-Python
Python Web API client for TickTrader

## Creating Web API client
```python
web_api_address = 'tpdemo.fxopen.com'
web_api_id = '8bd43d1f-39a4-45cd-a876-6acc0586533d'
web_api_key = 'qXhpBKFkndWWGYQ2'
web_api_secret = 'dSccqQmtaPc2xB68GD6A7KBgpfRhHJkFe5AchGShbDGzyn8H8ThjPspCq6Yh8cTz'

# Create instance of the TickTrader Web API client
client = TickTraderWebClient(web_api_address, web_api_id, web_api_key, web_api_secret)
```

## Access to public trade session information
```python
# Public trade session status
public_trade_session = client.get_public_trade_session()
print('TickTrader name: {0}'.format(public_trade_session['PlatformName']))
print('TickTrader company: {0}'.format(public_trade_session['PlatformCompany']))
print('TickTrader timezone offset: {0}'.format(public_trade_session['PlatformTimezoneOffset']))
print('TickTrader session status: {0}'.format(public_trade_session['SessionStatus']))
```

## Access to public currencies information
```python
# Public currencies                                                                 
currencies = client.get_public_all_currencies()                                     
for c in currencies:                                                                
    print('Currency: {0}'.format(c['Name']))                                        
                                                                                    
currency = client.get_public_currency(currencies[0]['Name'])                        
print("{0} currency precision: {1}".format(currency['Name'], currency['Precision']))

```

## Access to public symbols information
```python
# Public symbols                                                                
symbols = client.get_public_all_symbols()                                       
for s in symbols:                                                               
    print('Symbol: {0}'.format(s['Symbol']))                                    
                                                                                
symbol = client.get_public_symbol(symbols[0]['Symbol'])                         
print("{0} symbol precision: {1}".format(symbol['Symbol'], symbol['Precision']))

```

## Access to public feed ticks information
```python
# Public feed ticks                                                                             
ticks = client.get_public_all_ticks()                                                           
for t in ticks:                                                                                 
    print('{0} tick: {1} {2}'.format(t['Symbol'], t['BestBid']['Price'], t['BestAsk']['Price']))
                                                                                                
tick = client.get_public_tick(ticks[0]['Symbol'])                                               
print("{0} tick timestamp: {1}".format(tick['Symbol'], tick['Timestamp']))                      

```

## Access to public feed ticks level2 information
```python
# Public feed level2 ticks                                                                         
ticks_level2 = client.get_public_all_ticks_level2()                                                
for t in ticks_level2:                                                                             
    print('{0} level2 book depth: {1}'.format(t['Symbol'], max(len(t['Bids']), len(t['Asks']))))   
                                                                                                   
tick_level2 = client.get_public_tick_level2(ticks_level2[0]['Symbol'])                             
print("{0} level2 book depth: {1}".format(tick_level2['Symbol'],                                   
                                          max(len(tick_level2['Bids']), len(tick_level2['Asks']))))

```

## Access to account information
```python
# Account info                                      
account = client.get_account()                      
print('Account Id: {0}'.format(account['Id']))      
print('Account name: {0}'.format(account['Name']))  
print('Account group: {0}'.format(account['Group']))

```

## Access to account trade session information
```python
# Account trade session                                                  
trade_session = client.get_trade_session()                               
print('Trade session status: {0}'.format(trade_session['SessionStatus']))

```

## Access to account currencies information
```python
# Account currencies                                                                
currencies = client.get_all_currencies()                                            
for c in currencies:                                                                
    print('Currency: {0}'.format(c['Name']))                                        
                                                                                    
currency = client.get_currency(currencies[0]['Name'])                               
print("{0} currency precision: {1}".format(currency['Name'], currency['Precision']))

```

## Access to account symbols information
```python
# Account symbols                                                               
symbols = client.get_all_symbols()                                              
for s in symbols:                                                               
    print('Symbol: {0}'.format(s['Symbol']))                                    
                                                                                
symbol = client.get_symbol(symbols[0]['Symbol'])                                
print("{0} symbol precision: {1}".format(symbol['Symbol'], symbol['Precision']))

```

## Access to account feed ticks information
```python
# Account feed ticks                                                                            
ticks = client.get_all_ticks()                                                                  
for t in ticks:                                                                                 
    print('{0} tick: {1} {2}'.format(t['Symbol'], t['BestBid']['Price'], t['BestAsk']['Price']))
                                                                                                
tick = client.get_tick(ticks[0]['Symbol'])                                                      
print("{0} tick timestamp: {1}".format(tick['Symbol'], tick['Timestamp']))                      

```

## Access to account feed ticks level2 information
```python
# Account feed ticks level2                                                                        
ticks_level2 = client.get_all_ticks_level2()                                                       
for t in ticks_level2:                                                                             
    print('{0} level2 book depth: {1}'.format(t['Symbol'], max(len(t['Bids']), len(t['Asks']))))   
                                                                                                   
tick_level2 = client.get_tick_level2(ticks_level2[0]['Symbol'])                                    
print("{0} level2 book depth: {1}".format(tick_level2['Symbol'],                                   
                                          max(len(tick_level2['Bids']), len(tick_level2['Asks']))))

```

## Access to account assets information
Works only for cash accounts!
```python
# Account assets                                                  
account = client.get_account()                                    
if account['AccountingType'] == 'Cash':                           
    assets = client.get_all_assets()                              
    for a in assets:                                              
        print('{0} asset: {1}'.format(a['Currency'], a['Amount']))

```

## Access to account positions information
Works only for net accounts!
```python
# Account positions                                                                          
account = client.get_account()                                                               
if account['AccountingType'] == 'Net':                                                       
    positions = client.get_all_positions()                                                   
    for p in positions:                                                                      
        print('{0} position: {1} {2}'.format(p['Symbol'], p['LongAmount'], p['ShortAmount']))

```

## Access to account trades
```python
# Account trades                                                                                            
trades = client.get_all_trades()                                                                            
for t in trades:                                                                                            
    print('{0} trade with type {1} by symbol {2}: {3}'.format(t['Id'], t['Type'], t['Symbol'], t['Amount']))
                                                                                                            
trade = client.get_trade(trades[0]['Id'])                                                                   
print('{0} trade with type {1} by symbol {2}: {3}'.format(trade['Id'],                                      
                                                          trade['Type'],                                    
                                                          trade['Symbol'],                                  
                                                          trade['Amount']))                                 

```

## Access to account trade history
```python
iterations = 3
request = {'TimestampTo': TickTraderWebClient.get_timestamp(), 'RequestDirection': 'Backward', 'RequestPageSize':10}

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
```

## Create, modify and cancel limit order
```python
# Create, modify and cancel limit order                                                 
account = client.get_account()                                                          
if (account['AccountingType'] == 'Gross') or (account['AccountingType'] == 'Net'):      
                                                                                        
    # Create limit order                                                                
    limit = client.create_trade(                                                        
        {                                                                               
            'Type': 'Limit',                                                            
            'Side': 'Buy',                                                              
            'Symbol': 'EURUSD' if (account['AccountingType'] == 'Gross') else 'EUR/USD',
            'Amount': 10000,                                                            
            'Price': 1.0,                                                               
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

```
