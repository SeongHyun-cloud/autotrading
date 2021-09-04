import pandas as pd
from collections import deque
from rsi_model import RSI
from datetime import datetime
from printing_data import PrintPrices
from strategy import *

SEQ_LEN = 60

new_df = pd.read_csv("crypto_data/Bitstamp_BTCUSD_minute.csv", names = ['time', 'date', 'symbol','open', 'high', 'low', 'close', 'volume_usd',  'volume_btc'])
coin_type = "BTC"
new_df = new_df[1:]
new_df = new_df[["close", "time"]]
new_df_close = new_df["close"].tolist()[1:]
new_df_close.reverse()
new_df_close = [float(i) for i in new_df_close]
new_df_time = new_df["time"].tolist()[1:]
new_df_time.reverse()
new_df_time = [int(i) for i in new_df_time]



def backtesting(close_value, close_time, budget):
    def half_list(l):
        return l[int (len(l)/2):]
    close_value = half_list(close_value)
    close_time = half_list(close_time)
    
    #rsi calculation
    START_TIME = 100
    MINUTE = 5
    valueQ = deque(close_value[:START_TIME:MINUTE])
    rsi = RSI(14, 70, 30)
    rsi.rsi(valueQ)
    trade_count = 0
    #move list by the start time
    close_time = close_time[START_TIME:]
    close_value = close_value[START_TIME:]
    track_history = PrintPrices(budget, close_value[0], close_time[0])
    
    # looping 
    #change
    strat = RCstrategy(valueQ,rsi, budget)
    
    for i in range(0, len(close_value)):
        
        price = close_value[i]
        
        traded = strat.trade(price)
        #daily profit counter
        
        if traded:
            track_history.trade_count += 1
            track_history.printCurrent(strat.lastPrice, strat.coin, strat.deposit, close_time[i])
    
    track_history.result(strat)
    print(close_value[0])
    print(close_value[len(close_value)-1])
    return 0


backtesting(new_df_close, new_df_time, 1000)

#[print(datetime.fromtimestamp(i)) for i in new_df_time]
