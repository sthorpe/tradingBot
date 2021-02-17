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
