import pandas as pd
from collections import deque
from rsi_model import RSI
from datetime import datetime

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
    MINUTE = 5
    priceQ = deque(pric_list[:100:MINUTE])
    rsi = RSI(4, 70, 30)
    rsi.rsi()
    trade_count = 0

    




    return 0
    
backtesting(new_df_close, new_df_time, 1000)

#[print(datetime.fromtimestamp(i)) for i in new_df_time]
