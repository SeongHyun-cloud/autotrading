from datetime import datetime
from collections import deque

class PrintPrices:
    def __init__(self, deposit, start_day, close_value, close_time):
        self.deposit = deposit
        self.start_day = start_day
        self.day_count = 0
        self.rate_sum = 0
        self.trade_sum = 0
        self.trade_count = 0
        self.tax_sum = 0
        self.close_value = close_value
        self.close_time = close_time
        print("Start at ", datetime.fromtimestamp(close_time[start_day]), "with the price of ",close_value[start_day])



    