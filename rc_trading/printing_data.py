from datetime import datetime
from collections import deque
class PrintPrices:
    def __init__(self, deposit,close_value, close_time):
        self.deposit = deposit
        self.day_count = 0
        self.rate_sum = 0
        self.trade_count = 0
        self.tax_sum = 0
        self.close_value = close_value
        self.close_time = close_time
        print("Start at", datetime.fromtimestamp(close_time), "with the price of",close_value)

    def update(self, strategy):
        print("Curent ")

    def printCurrent(self, strat):
        print("Current", strat.deposit)


    