import websocket, json, pprint, talib, numpy
#import config
from binance.client import Client
#from binance.enums import *


SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"

close_value = []

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = ''
TRADE_QUANTITY = 0.05

own_coin = False

def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    print('received message')
    json_message = json.loads(message)
    #pprint.pprint(json_message)

    candle = json_message['k']

    is_candle_closed = candle['x']
    close = candle['c']

    #closed candle
    if is_candle_closed:
        print("candle closed at {}".format(close))
        close_value.append(float(close))
        if len(close_value) > RSI_PERIOD:
            np_closes = numpy.array(close_value)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            last_rsi = rsi[-1]

            if last_rsi > RSI_OVERBOUGHT:
                print("RSI Overbought, you might want to sell")
            if last_rsi < RSI_OVERSOLD:
                print("RSI Oversold, you might want to buy")

            
close_value.append(float(close))
    if len(close_value) > RSI_PERIOD:
        np_closes = numpy.array(close_value)
        rsi = talib.RSI(np_closes, RSI_PERIOD)
        last_rsi = rsi[-1]



        
    


#ws = websocket.WebSocketApp(SOCKET, on_open = on_open, on_close = on_close, on_message = on_message)
#ws.run_forever()

