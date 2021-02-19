# This will be where we collect the data stream from coinbase.com
# Read more here: https://docs.pro.coinbase.com/

import cbpro

class Coinbase():
    """ Coinbase object for accessing and trading on their platform """

    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def client(self):
        auth_client = cbpro.AuthenticatedClient(self.api_key, self.secret_key, self.passphrase, api_url="https://api-public.sandbox.pro.coinbase.com")
        return auth_client

    # Public API
    def public_client(self):
        public_client = cbpro.PublicClient()
        return public_client

    def get_products(self):
        return self.public_client().get_products()

    # Authenticated API
    def get_accounts(self):
        return self.client().get_accounts()

    def get_account(self, account_number):
        return self.client().get_account(account_number=account_number)

    def buy(self):
        # Buy 0.01 BTC @ 100 USD
        return self.client().buy(price='100.00', size='0.01', order_type='limit', product_id='BTC-USD')

    def sell(self):
        # Sell 0.01 BTC @ 200 USD
        return self.client().sell(price='200.00', size='0.01', order_type='limit', product_id='BTC-USD')

    def get_account_history(self, account_number):
        return self.client().get_account_history(account_number=account_number)

    # Limit order-specific method
    def place_limit_order(self):
        return self.client().place_limit_order(product_id='BTC-USD', side='buy', price='200.00', size='0.01')

    def place_market_order(self):
        return self.client().place_market_order(product_id='BTC-USD', side='buy', funds='100.00')

    def place_stop_order(self):
        return self.client().place_stop_order(product_id='BTC-USD', stop_type='loss', price='200.00', size='0.01')

    def cancel_order(self, order_id):
        return self.client().cancel_order(order_id=order_id)

    # product_id = 'BTC-USD'
    def cancel_all(self, product_id):
        return self.client().cancel_all(product_id=product_id)

    def get_orders(self):
        return self.client().get_orders()

    def get_order(self, order_id):
        return self.client().get_order(order_id=order_id)

    def get_fills(self, order_id="", product_id=""):
        if order_id:
            return self.client().get_fills(order_id=order_id)
        elif product_id:
            return self.client().get_fills(product_id=product_id)
        else:
            return self.client().get_fills()

    def deposit(self, amount="", coinbase_account_id=""):
        depositParams = {
            'amount': '25.00', # Currency determined by account specified
            'coinbase_account_id': '60680c98bfe96c2601f27e9c'
        }
        return self.client().deposit(depositParams)

    def withdraw(self):
        withdrawParams = {
            'amount': '1.00', # Currency determined by account specified
            'coinbase_account_id': '536a541fa9393bb3c7000023'
        }
        return self.client().withdraw(withdrawParams)

    def websocket_client(self):
        wsClient = cbpro.WebsocketClient(url="wss://ws-feed-public.sandbox.pro.coinbase.com", products="BTC-USD", channels=["ticker"])
        wsClient.start()
        #wsClient.close()

    def realtime_order_book(self):
        order_book = cbpro.OrderBook(product_id='BTC-USD')
        order_book.start()
        time.sleep(10)
        order_book.close()
