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

    def get_accounts(self):
        return self.client().get_accounts()

    def get_account(self, account_number):
        return self.client().get_account(account_number)

    def buy(self):
        # Buy 0.01 BTC @ 100 USD
        self.client().buy(price='100.00', size='0.01', order_type='limit', product_id='BTC-USD')
        
    def sell(self):
        # Sell 0.01 BTC @ 200 USD
        self.client().sell(price='200.00', size='0.01', order_type='limit', product_id='BTC-USD')
