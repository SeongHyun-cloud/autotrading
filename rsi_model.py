import websocket, json, pprint, talib, numpy

class RSI:
    RSI_PERIOD = 14
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
            if self.last_rsi > self.RSI_OVERBOUGHT:
                return "SELL"
            if self.last_rsi < self.RSI_OVERSOLD:
                return "BUY"

        return "NONE"

