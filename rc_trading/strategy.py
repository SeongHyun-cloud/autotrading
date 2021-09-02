class RCstrategy:
    
    def __init__(self, priceQ, rsi, deposit):
        self.priceQ = priceQ
        self.coin = 0
        self.deposit = deposit
        self.rsi = rsi
        self.lastPrice = -1
        self.purchaseAmount = 0
    ##
    # def myStrategy
    #   taking current price of coin buys if it is reasonable
    #   price to buy or sells in the same manner
    def trade(self, value):
        factor = 0
        self.priceQ.append(value)
        status, factor = self.rsi.rsi(self.priceQ)
        self.priceQ.popleft()
        if self.coin == 0 and status == "OVERBOUGHT" and factor >= 0.6 :
            
            self.purchaseAmount = self.deposit / 5
            self.coin = self.purchaseAmount / value
            self.deposit = self.deposit * (0.8)
            self.lastPrice = value
            print(self.deposit)
    
        #factor calculation Buying condition due to drammatic price drop
        if(self.lastPrice != -1) :
            profit_or_loss = value / self.lastPrice
            print(profit_or_loss, value, self.lastPrice, factor)


        if status == "OVERBOUGHT" and factor >= 1:
            if self.purchaseAmount >= self.deposit:
                #making average price
                acoin = self.deposit / value
                self.lastPrice = ((self.lastPrice * self.coin) / (value * acoin)) /(self.coin + acoin)
                self.coin = self.deposit * value
                self.deposit = 0
                self.purchaseAmount = value
                return True


        if status == "OVRESOLD" and factor >= 1:
            self.deposit = self.coin * value
            return True


        return False
        
        

        


    