
import requests
import pprint
from DataStreams.Coinbase import Coinbase

# This will be where we combine all our functions and run them
def main():
    COINBASE_PRO_KEY = 'c606224329f6a3a18d25a22436cea960'
    COINBASE_PRO_SECRET = 'p6Ne820xWPrGekpAd1cdtyF6MTmgT1V55DIotyCWENuSQj6IqseFdfBjyRoFdQ9FqrNgbSovaF3fw2SsoSjgzQ=='
    COINBASE_PRO_PASSPHRASE = 'lb3t6qfupvo'
    # api_url = 'https://api.pro.coinbase.com/'
    api_url = 'https://api-public.sandbox.pro.coinbase.com'
    auth = Coinbase(COINBASE_PRO_KEY, COINBASE_PRO_SECRET, COINBASE_PRO_PASSPHRASE)
    client = auth.client()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(client.get_accounts())

if __name__ == "__main__":
    main()
