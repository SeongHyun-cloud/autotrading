import pandas as pd
from collections import deque
from rsi_model import RSI
from datetime import datetime
from printing_data import PrintPrices
from strategy import *

from binance.client import Client
from datetime import datetime
import config
import talib, numpy
import time

client = Client(config.apiKey, config.apiSecurity)
symbol = 'ETHUSDT'
account = client.futures_account()
client.futures_change_leverage(symbol=symbol, leverage=2)
def backtesting(budget):    
    kline = client.futures_klines(symbol=symbol, limit= 1000,interval=client.KLINE_INTERVAL_1MINUTE)
    closed_price = []
    closed_time = []
    for i in kline:
        closed_price.append(float(i[4]))
        closed_time.append(int(i[0])/1000)
    closed_price = deque((closed_price))
    strat = RCstrategy(closed_price, budget, 1)
    print_history = PrintPrices(budget, closed_price[-1], closed_time[-1])
    
    recent_trade_time = ""
    while True:
        kline = client.futures_klines(symbol=symbol, limit= 1000,interval=client.KLINE_INTERVAL_1MINUTE)
        closed_price = []
        closed_time = []
        for i in kline:
            closed_price.append(float(i[4]))
            closed_time.append(int(i[0])/1000)
        
        price = closed_price[-1]
        if recent_trade_time != closed_time[-1]:
            traded = strat.trade(price)

        if traded:
            recent_trade_time = closed_time[-1]
            print_history.trade_count += 1
            print_history.printCurrent(price, strat.coin, strat.deposit, closed_time[-1], strat.lastPrice, strat.trade_status)
            time.sleep(30)

        time.sleep(1)
    return 0

backtesting(1000)


