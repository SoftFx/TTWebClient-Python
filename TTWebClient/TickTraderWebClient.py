__author__ = 'ivan.shynkarenka'


import base64
import datetime
import gzip
import hashlib
import hmac
import http.client
import io
import json
import ssl
import urllib.parse
import zlib


class TickTraderWebClient:
    def __init__(self, web_api_address, web_api_id=None, web_api_key=None, web_api_secret=None):
        if web_api_address is None:
            raise ValueError('Web API address is None!')

        self.__web_api_address = web_api_address
        self.__web_api_id = web_api_id
        self.__web_api_key = web_api_key
        self.__web_api_secret = web_api_secret

    def get_public_trade_session(self):
        """
        Get public trade session information
        """
        client = self.__create_http_client()
        client.request('GET', '/api/v1/public/tradesession', None, self.__get_http_public_headers())
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_public_all_currencies(self):
        """
        Get list of all available public currencies
        """
        client = self.__create_http_client()
        client.request('GET', '/api/v1/public/currency', None, self.__get_http_public_headers())
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_public_currency(self, currency):
        """
        Get public currency by name

        Keyword arguments:
        currency -- currency name
        """
        currency = urllib.parse.quote_plus(urllib.parse.quote_plus(currency))
        client = self.__create_http_client()
        client.request('GET', '/api/v1/public/currency/{0}'.format(currency), None, self.__get_http_public_headers())
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_public_all_symbols(self):
        """
        Get list of all available public symbols
        """
        client = self.__create_http_client()
        client.request('GET', '/api/v1/public/symbol', None, self.__get_http_public_headers())
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_public_symbol(self, symbol):
        """
        Get public symbol by name

        Keyword arguments:
        symbol -- symbol name
        """
        symbol = urllib.parse.quote_plus(urllib.parse.quote_plus(symbol))
        client = self.__create_http_client()
        client.request('GET', '/api/v1/public/symbol/{0}'.format(symbol), None, self.__get_http_public_headers())
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_public_all_ticks(self):
        """
        Get list of all available public feed ticks
        """
        client = self.__create_http_client()
        client.request('GET', '/api/v1/public/tick', None, self.__get_http_public_headers())
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_public_tick(self, symbol):
        """
        Get public feed tick by name

        Keyword arguments:
        symbol -- symbol name
        """
        symbol = urllib.parse.quote_plus(urllib.parse.quote_plus(symbol))
        client = self.__create_http_client()
        client.request('GET', '/api/v1/public/tick/{0}'.format(symbol), None, self.__get_http_public_headers())
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_public_all_ticks_level2(self):
        """
        Get list of all available public feed level2 ticks
        """
        client = self.__create_http_client()
        client.request('GET', '/api/v1/public/level2', None, self.__get_http_public_headers())
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_public_tick_level2(self, symbol):
        """
        Get public feed level2 tick by name

        Keyword arguments:
        symbol -- symbol name
        """
        symbol = urllib.parse.quote_plus(urllib.parse.quote_plus(symbol))
        client = self.__create_http_client()
        client.request('GET', '/api/v1/public/level2/{0}'.format(symbol), None, self.__get_http_public_headers())
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_public_all_tickers(self):
        """
        Get list of all available public symbol statistics
        """
        client = self.__create_http_client()
        client.request('GET', '/api/v1/public/ticker', None, self.__get_http_public_headers())
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_public_ticker(self, symbol):
        """
        Get public symbol statistics

        Keyword arguments:
        symbol -- symbol name
        """
        symbol = urllib.parse.quote_plus(urllib.parse.quote_plus(symbol))
        client = self.__create_http_client()
        client.request('GET', '/api/v1/public/ticker/{0}'.format(symbol), None, self.__get_http_public_headers())
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_account(self):
        """
        Get account information
        """
        client = self.__create_http_client()
        method = 'GET'
        url_relative = '/api/v1/account'
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_trade_session(self):
        """
        Get trade session information
        """
        client = self.__create_http_client()
        method = 'GET'
        url_relative = '/api/v1/tradesession'
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_all_currencies(self):
        """
        Get list of all available currencies
        """
        client = self.__create_http_client()
        method = 'GET'
        url_relative = '/api/v1/currency'
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_currency(self, currency):
        """
        Get currency by name

        Keyword arguments:
        currency -- currency name
        """
        currency = urllib.parse.quote_plus(urllib.parse.quote_plus(currency))
        client = self.__create_http_client()
        method = 'GET'
        url_relative = '/api/v1/currency/{0}'.format(currency)
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_all_symbols(self):
        """
        Get list of all available symbols
        """
        client = self.__create_http_client()
        method = 'GET'
        url_relative = '/api/v1/symbol'
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_symbol(self, symbol):
        """
        Get symbol by name

        Keyword arguments:
        symbol -- symbol name
        """
        symbol = urllib.parse.quote_plus(urllib.parse.quote_plus(symbol))
        client = self.__create_http_client()
        method = 'GET'
        url_relative = '/api/v1/symbol/{0}'.format(symbol)
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_all_ticks(self):
        """
        Get list of all available feed ticks
        """
        client = self.__create_http_client()
        method = 'GET'
        url_relative = '/api/v1/tick'
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_tick(self, symbol):
        """
        Get feed tick by name

        Keyword arguments:
        symbol -- symbol name
        """
        symbol = urllib.parse.quote_plus(urllib.parse.quote_plus(symbol))
        client = self.__create_http_client()
        method = 'GET'
        url_relative = '/api/v1/tick/{0}'.format(symbol)
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_all_ticks_level2(self):
        """
        Get list of all available feed level2 ticks
        """
        client = self.__create_http_client()
        method = 'GET'
        url_relative = '/api/v1/level2'
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_tick_level2(self, symbol):
        """
        Get feed level2 tick by name

        Keyword arguments:
        symbol -- symbol name
        """
        symbol = urllib.parse.quote_plus(urllib.parse.quote_plus(symbol))
        client = self.__create_http_client()
        method = 'GET'
        url_relative = '/api/v1/level2/{0}'.format(symbol)
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_all_assets(self):
        """
        Get list of all cash account assets (currency with amount)

        Works only for cash accounts!
        """
        client = self.__create_http_client()
        method = 'GET'
        url_relative = '/api/v1/asset'
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_asset(self, currency):
        """
        Get cash account asset (currency with amount) by the given currency name

        Works only for cash accounts!

        Keyword arguments:
        currency -- currency name
        """
        currency = urllib.parse.quote_plus(urllib.parse.quote_plus(currency))
        client = self.__create_http_client()
        method = 'GET'
        url_relative = '/api/v1/asset/{0}'.format(currency)
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_all_positions(self):
        """
        Get list of all available positions

        Works only for net accounts!
        """
        client = self.__create_http_client()
        method = 'GET'
        url_relative = '/api/v1/position'
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_position(self, symbol):
        """
        Get position by Id or symbol name

        Works only for net accounts!

        Keyword arguments:
        id -- position Id or symbol name
        """
        symbol = urllib.parse.quote_plus(urllib.parse.quote_plus(pos_id))
        client = self.__create_http_client()
        method = 'GET'
        url_relative = '/api/v1/position/{0}'.format(pos_id)
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_all_trades(self):
        """
        Get list of all available trades
        """
        client = self.__create_http_client()
        method = 'GET'
        url_relative = '/api/v1/trade'
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_trade(self, trade_id):
        """
        Get trade by symbol

        Keyword arguments:
        trade_id -- trade Id
        """
        client = self.__create_http_client()
        method = 'GET'
        url_relative = '/api/v1/trade/{0}'.format(trade_id)
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def create_trade(self, trade):
        """
        Create new trade

        New trade request is described by the filling following fields:
        - ClientId (optional) - Client trade Id
        - Type (required) - Type of trade. Possible values: "Market", "Limit", "Stop"
        - Side (required) - Side of trade. Possible values: "Buy", "Sell"
        - Symbol (required) - Trade symbol (e.g. "EURUSD")
        - Price (optional) - Price of the "Limit" / "Stop" trades (for Market trades price field is ignored)
        - Amount (required) - Trade amount
        - StopLoss (optional) - Stop loss price
        - TakeProfit (optional) - Take profit price
        - ExpiredTimestamp (optional) - Expiration date and time for pending trades ("Limit", "Stop")
        - ImmediateOrCancel (optional) - "Immediate or cancel" flag (works only for "Limit" trades)
        - Comment (optional) - Client comment

        Keyword arguments:
        trade -- create trade request
        """
        client = self.__create_http_client()
        method = 'POST'
        url_relative = '/api/v1/trade'
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        body = json.dumps(trade)
        client.request(method, url_relative, body.encode(), self.__get_http_hmac_headers(method, url_absolute, body))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def modify_trade(self, trade):
        """
        Modify existing trade

        Modify trade request is described by the filling following fields:
        - Id (required) - Trade Id
        - Price (optional) - New price of the Limit / Stop trades (price of Market trades cannot be changed)
        - StopLoss (optional) - Stop loss price
        - TakeProfit (optional) - Take profit price
        - ExpiredTimestamp (optional) - Expiration date and time for pending trades (Limit, Stop)
        - Comment (optional) - Client comment

        Keyword arguments:
        trade -- modify trade request
        """
        client = self.__create_http_client()
        method = 'PUT'
        url_relative = '/api/v1/trade'
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        body = json.dumps(trade)
        client.request(method, url_relative, body.encode(), self.__get_http_hmac_headers(method, url_absolute, body))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def cancel_trade(self, trade_id):
        """
        Cancel existing pending trade

        Return values:
            204 Ok. No content.
            400 Bad Request. The request could not be understood by the server due to malformed syntax.
            401 Unauthorized. The request requires user authentication.
            402 Payment Required. Not enough money for the operation.
            403 Forbidden. The request is forbidden due to limited access rights.
            404 Not Found. Required trade was not found.
            410 Gone. Off quotes or dealer reject.
            500 Internal Server Error. The server encountered an unexpected condition which prevented it from fulfilling the request.

        Keyword arguments:
        trade_id -- trade Id to cancel
        """
        client = self.__create_http_client()
        method = 'DELETE'
        url_relative = '/api/v1/trade?type=Cancel&id={0}'.format(trade_id)
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        return client.getresponse().status

    def close_trade(self, trade_id, amount=None):
        """
        Close existing market trade

        Return values:
            204 Ok. No content.
            400 Bad Request. The request could not be understood by the server due to malformed syntax.
            401 Unauthorized. The request requires user authentication.
            402 Payment Required. Not enough money for the operation.
            403 Forbidden. The request is forbidden due to limited access rights.
            404 Not Found. Required trade was not found.
            410 Gone. Off quotes or dealer reject.
            500 Internal Server Error. The server encountered an unexpected condition which prevented it from fulfilling the request.

        Keyword arguments:
        trade_id -- trade Id to close
        amount -- amount to close (optional)
        """
        client = self.__create_http_client()
        method = 'DELETE'
        if amount is None:
            url_relative = '/api/v1/trade?type=Close&id={0}'.format(trade_id)
        else:
            url_relative = '/api/v1/trade?type=Close&id={0}&amount={1}'.format(trade_id, amount)
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        return client.getresponse().status

    def close_by_trade(self, trade_id, by_trade_id):
        """
        Close existing market trade by another one

        Return values:
            204 Ok. No content.
            400 Bad Request. The request could not be understood by the server due to malformed syntax.
            401 Unauthorized. The request requires user authentication.
            402 Payment Required. Not enough money for the operation.
            403 Forbidden. The request is forbidden due to limited access rights.
            404 Not Found. Required trade was not found.
            410 Gone. Off quotes or dealer reject.
            500 Internal Server Error. The server encountered an unexpected condition which prevented it from fulfilling the request.

        Keyword arguments:
        trade_id -- trade Id to close
        by_trade_id -- by trade Id
        """
        client = self.__create_http_client()
        method = 'DELETE'
        url_relative = '/api/v1/trade?type=CloseBy&id={0}&byid={1}'.format(trade_id, by_trade_id)
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        client.request(method, url_relative, None, self.__get_http_hmac_headers(method, url_absolute, None))
        return client.getresponse().status

    def get_trade_history(self, request):
        """
        Get account trade history

        New trade history request is described by the filling following fields:
        - **TimestampFrom** (optional) - Lower timestamp bound of the trade history request
        - **TimestampTo** (optional) - Upper timestamp bound of the trade history request
        - **RequestDirection** (optional) - Request paging direction ("Forward" or "Backward"). Default is "Forward".
        - **RequestFromId** (optional) - Request paging from Id

        If timestamps fields are not set trade history will be requests from the begin or from the current timestamp
        depending on **RequestDirection** value.

        Trade history is returned by chunks by paging size (default is 100). You can provide timestamp bounds (from, to)
        and direction of access (forward or backward). After the first request you'll get a list of trade history
        records with Ids. The next request should contain **RequestFromId** with the Id of the last processed trade
        history record. As the result you'll get the next chunk of trade history records. If the last page was reached
        response flag **IsLastReport** will be set.

        Keyword arguments:
        request -- trade history request
        """
        client = self.__create_http_client()
        method = 'POST'
        url_relative = '/api/v1/tradehistory'
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        body = json.dumps(request)
        client.request(method, url_relative, body.encode(), self.__get_http_hmac_headers(method, url_absolute, body))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    def get_trade_history_by_id(self, trade_id, request):
        """
        Get account trade history for the given trade Id

        New trade history request is described by the filling following fields:
        - **TimestampFrom** (optional) - Lower timestamp bound of the trade history request
        - **TimestampTo** (optional) - Upper timestamp bound of the trade history request
        - **RequestDirection** (optional) - Request paging direction ("Forward" or "Backward"). Default is "Forward".
        - **RequestFromId** (optional) - Request paging from Id

        If timestamps fields are not set trade history will be requests from the begin or from the current timestamp
        depending on **RequestDirection** value.

        Trade history is returned by chunks by paging size (default is 100). You can provide timestamp bounds (from, to)
        and direction of access (forward or backward). After the first request you'll get a list of trade history
        records with Ids. The next request should contain **RequestFromId** with the Id of the last processed trade
        history record. As the result you'll get the next chunk of trade history records. If the last page was reached
        response flag **IsLastReport** will be set.

        Keyword arguments:
        trade_id -- trade Id
        request -- trade history request
        """
        client = self.__create_http_client()
        method = 'POST'
        url_relative = '/api/v1/tradehistory/{0}'.format(trade_id)
        url_absolute = 'https://{0}{1}'.format(self.__web_api_address, url_relative)
        body = json.dumps(request)
        client.request(method, url_relative, body.encode(), self.__get_http_hmac_headers(method, url_absolute, body))
        response = json.loads(self.__decode_response(client.getresponse()))
        return response

    @staticmethod
    def get_timestamp():
        time = (datetime.datetime.now(datetime.timezone.utc) -
                datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc))
        timestamp = time.days * 24 * 60 * 60 * 1000
        timestamp += time.seconds * 1000
        timestamp += time.microseconds / 1000
        return int(timestamp)

    def __create_http_client(self):
        client = http.client.HTTPSConnection(self.__web_api_address, context=ssl._create_unverified_context())
        return client

    @staticmethod
    def __get_http_public_headers():
        return {'Accept-Encoding': 'gzip, deflate', 'Content-type': 'application/json'}

    def __get_http_hmac_headers(self, method, url, body):
        headers = self.__get_http_public_headers()
        timestamp = self.get_timestamp()
        body = '' if body is None else body
        signature = str(timestamp) + self.__web_api_id + self.__web_api_key + method + url + body
        hash_value = self.__calculate_hmac_with_sha256(signature)
        auth_value = 'HMAC {0}:{1}:{2}:{3}'.format(self.__web_api_id, self.__web_api_key, timestamp, hash_value)
        headers['Authorization'] = auth_value
        return headers

    def __calculate_hmac_with_sha256(self, signature):
        digest_value = hmac.new(self.__web_api_secret.encode(),
                                msg=signature.encode(),
                                digestmod=hashlib.sha256).digest()
        hash_value = base64.b64encode(digest_value)
        return hash_value.decode()

    @staticmethod
    def __decode_response(response):
        encoding = response.info().get("Content-Encoding")
        if encoding in ('gzip', 'x-gzip', 'deflate'):
            content = response.read()
            if encoding == 'deflate':
                data = zlib.decompress(content)
            else:
                data = gzip.GzipFile('', 'rb', 9, io.BytesIO(content))
            return data.read().decode()
        else:
            return response.read().decode()
