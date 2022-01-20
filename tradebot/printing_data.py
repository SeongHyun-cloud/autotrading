from datetime import datetime
from collections import deque
import pandas as pd
import openpyxl

class PrintPrices:
    def __init__(self, deposit,close_value, close_time):
        self.deposit = deposit
        self.day_count = 0
        self.rate_sum = 0
        self.trade_count = 0
        self.tax_sum = 0
        self.close_value = close_value
        self.close_time = close_time

        self.df_excel = pd.DataFrame(columns=['Time', 'Size', 'balance', 'Wallet', 'Mark price', 'Entry price', 'status'])
        self.tfile = open("output.txt", "a")
        line = "Start at" + datetime.fromtimestamp(close_time).__str__() + "with the price of" + str(close_value) + "\n"
        self.tfile.write(line)
        line = '{0:7} {1:24} {2:10} {3:10} {4:10} {5:10} {6:10} {7:7} \n'.format('count','Time', 'Size', 'balance', 'Wallet', 'Mark price', 'Entry price', 'status')
        self.tfile.write(line)
        self.tfile.close()

    def result(self, strat):
        self.tfile.wrtie("At the end," + (int((strat.coin * strat.lastPrice + strat.deposit) * 100)) / 100 + "$")
        self.tfile.write("trade_count" + self.trade_count)

    def printCurrent(self, value, coin, deposit, time, lastPrice, traded):
        
        self.tfile = open("output.txt", 'a')
        balance = round( deposit + coin * value, 2)
        time = datetime.fromtimestamp(time).__str__()
        line = '{0:7} {1:24} {2:10} {3:10} {4:10} {5:10} {6:10} {7:7} \n'.format(self.trade_count,time, round(coin, 5), balance, round(deposit, 2), value, round(lastPrice,2), traded)
        self.tfile.write(line)
        self.tfile.close()