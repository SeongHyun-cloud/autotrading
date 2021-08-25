import pandas as pd
from collections import deque
from rsi_model import RSI
from datetime import datetime


SEQ_LEN = 60

df = pd.read_csv("crypto_data/BTC-USD.csv", names = ['time', 'low', 'high', 'open', 'close', 'volume'])
BITCOIN = "BTC"

reader = df
df.rename(columns={"close" : "BTC-close", "volume" : "BTC-volume"}, inplace = True)
df.set_index("time", inplace = True)
df = df[["BTC-close", "BTC-volume"]]

def test_by_60min(price_list, timestamp, deposit, coin_amount):
    #rsi calculation
    priceQ = deque(price_list[:60])

    rsi = RSI(4, 70, 30)
    rsi.rsi(priceQ)
    tradeCounter = 0

    #''' SHORT THE TIME
    price_list = half_list(price_list) 
    timestamp = half_list(timestamp)
    price_list = half_list(price_list) 
    timestamp = half_list(timestamp)
    price_list = half_list(price_list) 
    timestamp = half_list(timestamp)
    

    #to find average interest rate by day
    olddeposit = 1000
    daycount = 0
    rateSum = 0
    tradeCountByDay = 0
    tradeSum = 0
    taxSum = 0

    print("Start at ", datetime.fromtimestamp(int (timestamp[60])), "with the price of ", price_list[60])
    for i in range(60, len(price_list)):
        if deposit <= 1 and coin_amount <= 0:
            print("broke")
            break
            
        priceQ.append(price_list[i])
        priceQ.popleft()
        status = rsi.rsi(priceQ)
        
        if (int (timestamp[i])) % 81000 == 0:
            tradeSum += tradeCountByDay
            print("Day passed : ", datetime.fromtimestamp(int (timestamp[i])))
            temp = 0
            if coin_amount != 0: 
                temp = coin_amount * price_list[i]
            elif deposit != 0:
                temp = deposit
            print("\tFrom", olddeposit, "to", temp, "    ", "made ", temp/olddeposit*100 - 100,"%")
            rateSum += temp/olddeposit*100 - 100
            olddeposit = temp 
            daycount += 1
            tradeCountByDay = 0
            
            #254979755.06520534 70 30
            #664964629.2916512 70 35
            #2189450369.750374 70 40
            #3854357599.5721345 70 45
            #10578657698.21748 70 65

            # 610.4850583583163
        if status == "SELL":
            if (coin_amount != 0 and price_list[i] / rsi.buy_price > 0.99):
                #if price_list[i] > rsi.buy_price:
                #    print(price_list[i] - rsi.buy_price, price_list[i] / rsi.buy_price)
                rsi.sell_price = price_list[i]
                taxSum += coin_amount * price_list[i] *0.001
                deposit = coin_amount * price_list[i] - coin_amount * price_list[i] *0.0004
                #print("Selling at ", price_list[i], "last rsi is", rsi.last_rsi, "    ", deposit, " buy price: ", rsi.buy_price, "\n")
                coin_amount = 0
                tradeCounter+=1
                tradeCountByDay+=1
        elif status == "BUY":
            if (deposit != 0):
                #print("Buying at ", price_list[i],  "last rsi is", rsi.last_rsi, "    ", deposit, "\n")
                rsi.buy_price = price_list[i]
                taxSum += deposit*0.001
                deposit -= deposit*0.0004
                coin_amount = deposit * 1 / price_list[i]
                deposit = 0
                tradeCounter+=1
                tradeCountByDay+=1
        

    if coin_amount != 0: 
        print("coin", coin_amount, price_list[len(price_list) - 1])
        print(coin_amount * price_list[len(price_list) - 1])
    elif deposit != 0:
        print("only deposit:", deposit)
    print("Trader has traded: ", tradeCounter)

    print("end at ", datetime.fromtimestamp(int (timestamp[len(timestamp) - 1])), "with the price of ", price_list[len(price_list) - 1])
    print("Average interst rate by day : ", rateSum / daycount, "Average trade amount by day : ", tradeCounter / daycount, " TAX: ", taxSum)


def half_list(l):
    return l[int (len(l)/2):]
        
#testing
df_list = df["BTC-close"].tolist()


'''
from_2012_to_2020_df = pd.read_csv("crypto_data/BTC-USD-2012-2020.csv", names = ['time','open', 'high', 'low', 'close', 'volume', 'currency', 'weighted_price'])
from_2012_to_2020_df = from_2012_to_2020_df.dropna()


all_df = from_2012_to_2020_df[["close", "time"]][1:]
all_df_close = all_df["close"]
all_df_time = all_df["time"]


all_df_close = all_df_close.tolist()
all_df_time = all_df_time.tolist()


all_df_close = [float(i) for i in all_df_close]

test_by_60min(all_df_close, all_df_time, 1000, 0)
'''

#Latest bitcoin data
new_df = pd.read_csv("crypto_data/Bitstamp_BTCUSD_minute.csv", names = ['time', 'date', 'symbol','open', 'high', 'low', 'close', 'volume_usd',  'volume_btc'])
new_df = new_df[1:]
new_df = new_df[["close", "time"]]
new_df_close = new_df["close"].tolist()[1:]
new_df_close.reverse()
new_df_close = [float(i) for i in new_df_close]
new_df_time = new_df["time"].tolist()[1:]
new_df_time.reverse()
new_df_time = [int(i) for i in new_df_time]

test_by_60min(new_df_close, new_df_time, 1000, 0)

'''
(70, 50 0.95)
6799.14456213908
Trader has traded:  33351
Start at  2021-03-25 15:17:00 with the price of  53116.33
Average interst rate by day :  2.0500605463563972 Average trade amount by day :  326.97058823529414
'''
