from binance.client import Client
from datetime import datetime
import config
import talib, numpy
import time

client = Client(config.apiKey, config.apiSecurity)
print('logged in')

symbol = 'ETHUSDT'

#extracts account information
account = client.futures_account()
#returns to the price of the symbol
#print(client.futures_account_balance()['balance'])
#client.create_test_order(symbol='ETHUSDT', side='BUY', type='MARKET', quantity=100)
print(account['totalUnrealizedProfit'])

old_time = ""

while True:
    kline = client.futures_klines(symbol=symbol, limit= 1000,interval=client.KLINE_INTERVAL_1MINUTE)


    file = open('result.txt','a')

    closed_price = []
    closed_time = []
    for i in kline:
        closed_price.append(float(i[4]))
        closed_time.append(int(i[0])/1000)

    np_closes = numpy.array(closed_price)
    rsi = talib.RSI(np_closes, timeperiod=6)

    print(datetime.fromtimestamp(round(closed_time[-1])))

    #print(datetime.fromtimestamp(round(closed_time[0])))
    #print("rsi :", rsi[-1], "time",datetime.fromtimestamp(round(closed_time[-1])))
    
    if old_time != datetime.fromtimestamp(round(closed_time[-1])):
        print("\n\n\n qweqwe qwe \n\n\n")
        input("not smae")
        file.write("X\n")
    else:
        input("hit enter")
        file.write("O\n")
    file.close()
    old_time = datetime.fromtimestamp(round(closed_time[-1]))
    
#print(closed_price, closed_time)
