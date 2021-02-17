# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 13:35:39 2021

@author: Harrison
"""
from binanceklines import binance_klines
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from pandas import DataFrame as df
from RSI_calcs import StochRSI
import pandas as pd


klines = binance_klines()

#adds Stoch RSI to price dataframe using StochRSI() from RSI_Functions
def StochRSI_to_Dataframe(klines):
    daily = klines
    daily['open'] = daily['open'].astype(float)
    daily['high'] = daily['high'].astype(float)
    daily['low'] = daily['low'].astype(float)
    daily['close'] = daily['close'].astype(float)
    daily['volume'] = daily['volume'].astype(float)
    
    calcs = StochRSI(daily.close, period=14, smoothK=5, smoothD=5)
    calcs_list = list(calcs)
    calcs_df = df(calcs_list)
    calcsnew = calcs_df.transpose()
    calcsnew.head()
    calcsnew.rename(columns={calcsnew.columns[0]:'stochrsi', calcsnew.columns[1]:'stochrsi_K', calcsnew.columns[2]:'stochrsi_D'}, inplace=True)
    daily_rsi = daily.join(calcsnew)
    daily_rsi.columns = ['opentime', 'open', 'high', 'low', 'close', 'volume', 'closetime', 'quotevolume', 'numtrades', 'stochrsi', 'stochrsi_k', 'stochrsi_d']
    
    return daily_rsi

data = StochRSI_to_Dataframe(klines)
#data.to_csv('test42.csv') 
data['30line'] = 30
data['80line'] = 80

def buy_sell(data):
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1
    
    for i in range(len(data)):
        if data['stochrsi_k'][i] > data['stochrsi_d'][i]:
            if flag != 1:
                sigPriceBuy.append(data['close'][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                 sigPriceBuy.append(np.nan)
                 sigPriceSell.append(np.nan)
        elif data['stochrsi_k'][i] < data['stochrsi_d'][i]:
            if flag != 0:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(data['close'][i])
                flag=0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)
    return (sigPriceBuy, sigPriceSell)
                
buy_sell = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]

plt.figure(figsize=(12.6, 8.6))
plt.plot(data['close'], label = "close", alpha = 0.45)
#plt.plot(data['MA50'], label = "MA50", alpha = 0.45)
#plt.plot(data['MA200'], label = "MA200", alpha = 0.45)
plt.scatter(data.index, data['Buy_Signal_Price'], label = 'Buy', marker = '^', color = 'green')
plt.scatter(data.index, data['Sell_Signal_Price'], label = 'Sell', marker = 'v', color = 'red')
plt.title('Python Signals Beta')
plt.xlabel('Datetime')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.show()



data['buys_and_sells'] = pd.concat([data['Buy_Signal_Price'].dropna(), data['Sell_Signal_Price'].dropna()]).reindex_like(data)   
data['percent_change'] = (data.buys_and_sells.pct_change())
data['ammount']=(data['percent_change']+1).cumprod()*100



data.to_csv('stoch_cross_strat_results_15m.csv')

print(data['ammount'].iloc[-1])