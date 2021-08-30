import pandas as pd
from collections import deque
from rsi_model import RSI
from datetime import datetime

SEQ_LEN = 60

df = pd.read_csv("crypto_data/BTC-USD.csv", names = ['time', 'low', 'high', 'open', 'close', 'volume'])
coin_type = "BTC"

reader = df
df.rename(columns={"close" : coin_type + "-close", "volume" : coin_type + "-volume"}, inplace = True)
df.set_index("time", inplace = True)
df = df[["BTC-close", "BTC-volume"]]
print(df.head())