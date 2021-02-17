# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:58:20 2021

@author: Harrison
"""

#EVERYTHING for scott and stephen

import binance as client
from datetime import datetime
from pandas import DataFrame as df

#datetime is UTC-5 when binance datetime is UTC

def binance_klines():
    candles = client.klines('BTCUSDT', "15m", limit = 1000)
    
    candles_dataframe = df(candles)
    
    candles_dataframe_date = candles_dataframe['openTime']
    
    final_date = []
    
    for time in candles_dataframe_date.unique():
        readable = datetime.fromtimestamp(int(time/1000))
        final_date.append(readable)
        
        
    dataframe_finaldate = df(final_date)
    
    dataframe_finaldate.columns = ['date']
    
    final_dataframe = candles_dataframe.join(dataframe_finaldate)
    
    final_dataframe.set_index('date', inplace=True)
    
    return final_dataframe

print(binance_klines())

#https://www.tradingview.com/support/solutions/43000502338-relative-strength-index-rsi/

def AO_indi(klines):
    daily = klines
    daily['open'] = daily['open'].astype(float)
    daily['high'] = daily['high'].astype(float)
    daily['low'] = daily['low'].astype(float)
    daily['close'] = daily['close'].astype(float)
    daily['volume'] = daily['volume'].astype(float)
        
    daily['highpluslow'] = daily['high'] + daily['low']
    daily['midpoint'] = daily['highpluslow']/2
    daily['34_MA'] = daily.midpoint.rolling(window=34).mean()
    daily['5_MA'] = daily.midpoint.rolling(window=5).mean()
    daily['AO'] = daily['5_MA'] - daily['34_MA']
    daily['AO_Slope'] = daily.AO.diff(periods=1)
    daily['Slope_sign'] = np.sign( np.sign(daily['AO_Slope']).diff().fillna(0) )
    daily['AO_sign'] = np.sign( np.sign(daily['AO']).diff().fillna(0) )
    daily['Slope_sign_2'] = daily['Slope_sign'].replace(0, np.NaN).ffill()
    daily['AO_sign_2'] = daily['AO_sign'].replace(0, np.NaN).ffill()
    return daily

#test = AO_indi(binance_klines())
#test.to_csv('test50.csv')   

 
    
def AO_Cross(daily):
    daily['AO_sign'] = np.sign( np.sign(daily['AO']).diff().fillna(0) )
    daily['signal1'] = daily['AO_sign'] != 0
    return daily


from binanceklines import binance_klines
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

data = AO_indi(binance_klines())


def buy_sell(data):
    AoPivotLow = []
    AoPivotHigh = []
    flag = -1
    
    for i in range(len(data)):
        if data['Slope_sign'][i] == 1:
            if flag != 1:
                AoPivotLow.append(data['close'][i])
                AoPivotHigh.append(np.nan)
                flag = 1
            else:
                 AoPivotLow.append(np.nan)
                 AoPivotHigh.append(np.nan)
        elif data['Slope_sign'][i] == -1:
            if flag != 0:
                AoPivotLow.append(np.nan)
                AoPivotHigh.append(data['close'][i])
                flag=0
            else:
                AoPivotLow.append(np.nan)
                AoPivotHigh.append(np.nan)
        else:
            AoPivotLow.append(np.nan)
            AoPivotHigh.append(np.nan)
    return (AoPivotLow, AoPivotHigh)
                
buy_sell = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]

#data.to_csv('AOcross_1m_results.csv')

plt.figure(figsize=(20, 10))
plt.plot(data['close'], label = "close", alpha = 0.45)
#plt.plot(data['MA50'], label = "MA50", alpha = 0.45)
#plt.plot(data['MA200'], label = "MA200", alpha = 0.45)
plt.scatter(data.index, data['Buy_Signal_Price'], label = 'Buy', marker = '.', color = 'green')
plt.scatter(data.index, data['Sell_Signal_Price'], label = 'Sell', marker = '.', color = 'red')
plt.title('Python Signals Beta')
plt.xlabel('Datetime')
plt.ylabel('Price')
#plt.legend(loc='upper left')
plt.show()



data['buys_and_sells'] = pd.concat([data['Buy_Signal_Price'].dropna(), data['Sell_Signal_Price'].dropna()]).reindex_like(data)   
data['percent_change'] = (data.buys_and_sells.pct_change())
data['ammount']=(data['percent_change']+1).cumprod()*100



#data.to_csv('AO_Slope_results_1h.csv')

print(data['ammount'].iloc[-1])