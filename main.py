
import requests
import pprint
from DataStreams.Coinbase import Coinbase
from Console import coinbase_console
import os

# Sandbox keys
os.environ['COINBASE_PRO_KEY'] = 'c606224329f6a3a18d25a22436cea960'
os.environ['COINBASE_PRO_SECRET'] = 'p6Ne820xWPrGekpAd1cdtyF6MTmgT1V55DIotyCWENuSQj6IqseFdfBjyRoFdQ9FqrNgbSovaF3fw2SsoSjgzQ=='
os.environ['COINBASE_PRO_PASSPHRASE'] = 'lb3t6qfupvo'

# This will be where we combine all our functions and run them
def main():
    coinbaseAPI = Coinbase(os.environ['COINBASE_PRO_KEY'], os.environ['COINBASE_PRO_SECRET'], os.environ['COINBASE_PRO_PASSPHRASE'])
    pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(coinbaseAPI.get_account('270421d1-2caa-4444-97e4-5f6c53a442bf'))
    coinbase_console()

    # Looking to see different ways to play with this Data

    # a trail of 500 - last 500 hours of btc
    # request the last trade order

if __name__ == "__main__":
    main()
