
#RSI Calculation


from binanceklines_1h import binance_klines
import numpy as np
import pandas as pd


daily = binance_klines()

daily['open'] = daily['open'].astype(float)
daily['high'] = daily['high'].astype(float)
daily['low'] = daily['low'].astype(float)
daily['close'] = daily['close'].astype(float)
daily['volume'] = daily['volume'].astype(float)

prices = daily['close']

def rsiFunc (prices, n=14):
    deltas = np.diff(prices)
    seed = deltas[:n+1]
    up = seed[seed<=0].sum()/n
    down = -seed[seed<0].sum()/n
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100./(1.+rs)
    for i in range(n, len(prices)):
        delta = deltas[i-1]
        if delta > 0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta
        up = (up*(n-1) + upval)/n
        down = (down*(n-1) + downval)/n
        rs = up/down
        rsi[i] = 100. - 100./(1.+rs)
    return rsi

rsiFunc(prices, n=14)
