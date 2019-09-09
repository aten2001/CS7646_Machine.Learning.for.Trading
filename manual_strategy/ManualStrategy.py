"""Project: Manual Strategy.                                                                                              
                                                                                              
Copyright 2018, Georgia Institute of Technology (Georgia Tech)                                                                                                
Atlanta, Georgia 30332                                                                                                
All Rights Reserved                                                                                               
                                                                                              
Template code for CS 4646/7646                                                                                                
                                                                                              
Georgia Tech asserts copyright ownership of this template and all derivative                                                                                              
works, including solutions to the projects assigned in this course. Students                                                                                              
and other users of this template code are advised not to share it with others                                                                                             
or to make it available on publicly viewable websites including repositories                                                                                              
such as github and gitlab.  This copyright statement should not be removed                                                                                                
or edited.                                                                                                
                                                                                              
We do grant permission to share solutions privately with non-students such                                                                                                
as potential employers. However, sharing with other current or future                                                                                             
students of CS 7646 is prohibited and subject to being investigated as a                                                                                              
GT honor code violation.                                                                                              
                                                                                              
-----do not edit anything above this line---                                                                
                                                                
  Student Name: ZHENG FU
  GT User ID: zfu66
  GT ID: 903369876                                                              
"""   

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib
import sys
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import util as ut
from util import get_data, plot_data
from marketsimcode import compute_portvals, compute_portvals_stats
from indicators import SMA, EMA, BollingerBands, Momentum

def testPolicy(symbol="JPM", sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,12,31), sv=100000):

    ############################
    #
    # Loading Data
    #
    ############################

    prices = get_data([symbol], pd.date_range(sd, ed), True)
    prices = prices.drop(['SPY'], axis=1)
    prices = prices.fillna(method='ffill')
    prices = prices.fillna(method='bfill')
    prices = prices / prices.ix[0,] 

    ############################
    #
    # Indicators
    #
    ############################
        
    SMA_20 = SMA(prices, symbol, 20)
    SMA_50 = SMA(prices, symbol, 50)
    EMA_20 = EMA(prices, symbol, 20)
    EMA_50 = EMA(prices, symbol, 50)
    [SMA_20, SMA_20_std, BB_upper_band, BB_lower_band, BB_value] = BollingerBands(prices, symbol, 20, 2)
    momentum_20 = Momentum(prices, symbol, 20)

    indicators_df = pd.DataFrame(index=prices.index, columns=['JPM', 'SMA_20days', 'SMA_50days', 'EMA_20days', 'EMA_50days', 'BB_upper_band', 'BB_lower_band', 'Momentum_20days'])
    indicators_df['JPM'] = prices[symbol]
    indicators_df['SMA_20days'] = SMA_20
    indicators_df['SMA_50days'] = SMA_50
    indicators_df['EMA_20days'] = EMA_20
    indicators_df['EMA_50days'] = EMA_50
    indicators_df['BB_upper_band'] = BB_upper_band
    indicators_df['BB_lower_band'] = BB_lower_band
    indicators_df['Momentum_20days'] = momentum_20
    indicators_df = indicators_df.fillna(method='bfill')

    #print indicators_df

    ############################
    #
    # Signal
    #
    ############################

    signal_df = pd.DataFrame(index=prices.index, columns=['SMA', 'BB', 'EMA'])

    signal_df.loc[signal_df.index[0], 'SMA'] = 0
    signal_df.loc[signal_df.index[0], 'BB'] = 0
    signal_df.loc[signal_df.index[0], 'EMA'] = 0

    row_counter = 1

    for i,row in indicators_df[1:].iterrows():

        current_price = row['JPM']
        current_SMA20 = row['SMA_20days']
        current_SMA50 = row['SMA_50days']
        current_EMA20 = row['EMA_20days']
        current_EMA50 = row['EMA_50days']
        current_BB_up = row['BB_upper_band'] 
        current_BB_down = row['BB_lower_band']
        current_momentum = row['Momentum_20days']

        previous_price = indicators_df['JPM'][row_counter-1]
        previous_SMA20 = indicators_df['SMA_20days'][row_counter-1]
        previous_SMA50 = indicators_df['SMA_50days'][row_counter-1]
        previous_EMA20 = indicators_df['EMA_20days'][row_counter-1]
        previous_EMA50 = indicators_df['EMA_50days'][row_counter-1]
        previous_BB_up = indicators_df['BB_upper_band'][row_counter-1]
        previous_BB_down = indicators_df['BB_lower_band'][row_counter-1]
        previous_momentum = indicators_df['Momentum_20days'][row_counter-1]

        row_counter += 1

        #print "Current: ", current_momentum 
        #print "Previous: ", previous_momentum

        ############################
        #
        # SMA
        #
        ############################

        if (previous_SMA50 > previous_SMA20) and (current_SMA50 < current_SMA20):
            signal_df.loc[i, 'SMA'] = 1
        elif (previous_SMA50 < previous_SMA20) and (current_SMA50 > current_SMA20):
            signal_df.loc[i, 'SMA'] = -1
        else:
            signal_df.loc[i, 'SMA'] = 0

        ############################
        #
        # BB
        #
        ############################

        if (previous_price < previous_BB_down) and (current_price > current_BB_down):
            signal_df.loc[i, 'BB'] = 1
        elif (previous_price > previous_BB_up) and (current_price < current_BB_up):
            signal_df.loc[i, 'BB'] = -1
        else:
            signal_df.loc[i, 'BB'] = 0

        ############################
        #
        # EMA
        #
        ############################

        if (previous_EMA50 > previous_EMA20) and (current_EMA50 < current_EMA20):
            signal_df.loc[i, 'EMA'] = 1
        elif (previous_EMA50 < previous_EMA20) and (current_EMA50 > current_EMA20):
            signal_df.loc[i, 'EMA'] = -1
        else:
            signal_df.loc[i, 'EMA'] = 0

        ############################
        #
        # Momentum
        #
        ############################

        #if (previous_momentum < 0) and (current_momentum >= 0):
        #    signal_df.loc[i, 'Momentum'] = 1
        #elif (previous_momentum >= 0) and (current_momentum < 0):
        #    signal_df.loc[i, 'Momentum'] = -1
        #else:
        #    signal_df.loc[i, 'Momentum'] = 0


    signal_df["SUM"] = signal_df.sum(axis=1)
    signal_df["Signal"] = signal_df["SUM"]

    signal_df.loc[signal_df["SUM"] <= -1, "Signal"] = -1
    signal_df.loc[signal_df["SUM"] >= 1,  "Signal"] = 1
    signal_df.loc[signal_df["SUM"] == 0,  "Signal"] = 0

    #print signal_df.head(10)

    signal_df.to_csv("signal.csv")

    df_trades = pd.DataFrame(index=signal_df.index, columns=[symbol])
    df_trades[symbol] = np.zeros(signal_df.shape[0])
    holding = 0
    indicators_df['Final_Signal'] = np.zeros(indicators_df.shape[0])
    
    # Trading Scheme 

    for i in df_trades.index:

        #print i

        if holding == 0:

            if signal_df.loc[i, "Signal"] == 1:
                df_trades.loc[i, symbol] = 1000
                holding = 1000
                indicators_df.loc[i, 'Final_Signal'] = 1
            elif signal_df.loc[i, "Signal"] == -1:
                df_trades.loc[i, symbol] = -1000
                holding = -1000
                indicators_df.loc[i, 'Final_Signal'] = -1
            else:
                df_trades.loc[i, symbol] = 0

        elif holding == 1000:

            if signal_df.loc[i, "Signal"] == -1:
                df_trades.loc[i, symbol] = -2000
                indicators_df.loc[i, 'Final_Signal'] = -1
                holding = -1000
        
        elif holding == -1000:

            if signal_df.loc[i, "Signal"] == 1:
                df_trades.loc[i, symbol] = 2000
                indicators_df.loc[i, 'Final_Signal'] = 1
                holding = 1000

    df_trades.to_csv("trades.csv")
                
    return (df_trades, indicators_df)


def Benchmark(symbol="JPM", sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,12,31), sv=100000):

    prices = get_data([symbol], pd.date_range(sd, ed), True)
    prices = prices.drop(['SPY'], axis=1)
    share = [1000,-1000]
    dates = [prices.index[0], prices.index[-1]]
    benchmark_df = pd.DataFrame(data = share, index = dates, columns = {symbol})
    return benchmark_df

def author():                                                               
    return 'zfu66' #Change this to your user ID    

if __name__ == "__main__":

   print "This is manual Strategy!"
