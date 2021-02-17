
import requests
import pprint
from DataStreams.Coinbase import Coinbase

# This will be where we combine all our functions and run them
def main():
    COINBASE_PRO_KEY = '502ce326637d160c0bf98072d9955ca8'
    COINBASE_PRO_SECRET = '2seolrrwKZuGEwfhAFZELtmlbBKb4+IxkaP1EA5T2UT25NZMhzfYTCs0MBEru7hKALXCar053eMmvcsjUTnYiw=='
    COINBASE_PRO_PASSPHRASE = 'wca3m8ajt6p'
    # api_url = 'https://api.pro.coinbase.com/'
    api_url = 'https://api-public.sandbox.pro.coinbase.com'
    auth = Coinbase(COINBASE_PRO_KEY, COINBASE_PRO_SECRET, COINBASE_PRO_PASSPHRASE)
    client = auth.client()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(client.get_accounts())

if __name__ == "__main__":
    main()
