# This will be where we collect the data stream from coinbase.com
# Read more here: https://docs.pro.coinbase.com/

class Coinbase:
    """ Coinbase object for accessing and trading on their platform """

    def authChannel(self):
        # Need to put API details here
        # API secret
        COINBASE_PRO_KEY = '4c026ad9c5076aa693785f35496e3609'
        COINBASE_PRO_SECRET = '/eFhoM4F7Y2ft+flBdjEyL0nKWJHO1ybyPwhWaPSWyMla+8t5TZ08OPOCEMPnDgzL7XOUAKjFCV9Iho5Vi8eSQ=='
        COINBASE_PRO_PASSPHRASE = 'm56ebfk3ny'

    def connect(self):
