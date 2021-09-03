import websocket, json, pprint, talib, numpy

class RSI:
    RSI_PERIOD = 14
    RSI_95 = 95
    RSI_90 = 90
    RSI_80 = 80
    RSI_70 = 70
    RSI_60 = 60
    RSI_40 = 40
    RSI_30 = 30
    RSI_20 = 20
    RSI_10 = 10
    RSI_5 = 5
    RSI_OVERBOUGHT = 70
    RSI_OVERSOLD = 30
    last_rsi = 1
    buy_price = 4.39
    sell_price = 0

    def __init__(self, period, overbought, oversold):
        self.RSI_PERIOD = period
        self.RSI_OVERBOUGHT = overbought
        self.RSI_OVERSOLD = oversold
        self.last_rsi = 0

    
    def rsi(self, closed_prices):
        if len(closed_prices) > self.RSI_PERIOD:
            np_closes = numpy.array(closed_prices)
            rsi = talib.RSI(np_closes, self.RSI_PERIOD)
            self.last_rsi = rsi[-1]
            
            if self.last_rsi > self.RSI_95:
                return "OVERBOUGHT", 0.8
            elif self.last_rsi > self.RSI_90:
                return "OVERBOUGHT", 0.7
            elif self.last_rsi > self.RSI_80:
                return "OVERBOUGHT", 0.6
            elif self.last_rsi > self.RSI_70:
                return "OVERBOUGHT", 0.5
            elif self.last_rsi > self.RSI_60:
                return "OVERBOUGHT", 0.4
            elif self.last_rsi > self.RSI_40:
                return "NONE", 0.0
            elif self.last_rsi > self.RSI_30:
                return "OVERSOLD", 0.4
            elif self.last_rsi > self.RSI_20:
                return "OVERSOLD", 0.5
            elif self.last_rsi > self.RSI_10:
                return "OVERSOLD", 0.6
            elif self.last_rsi > self.RSI_5:
                return "OVERSOLD", 0.7
            elif self.last_rsi >= 0:
                return "OVERSOLD", 0.8


