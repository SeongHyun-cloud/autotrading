import pandas as pd
from collections import deque
from rsi_model import RSI
from datetime import datetime
from printing_data import PrintPrices

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
    rsi = RSI(4, 70, 30)
    rsi.rsi(valueQ)
    trade_count = 0

    PrintPrices(budget, START_TIME, close_value, close_time)

    




    return 0

print(datetime.fromtimestamp(new_df_time[len(new_df_close)-1]))
backtesting(new_df_close, new_df_time, 1000)

#[print(datetime.fromtimestamp(i)) for i in new_df_time]
