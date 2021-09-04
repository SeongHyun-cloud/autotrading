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
        sell_factor = factor
        buy_factor = factor
        self.priceQ.popleft()

        percent_of_deposit = 4
        leverage = 10
        fee = 0.02

        if self.coin == 0 and status == "OVERSOLD" and factor >= 0.6 :
            print("none Happens")
            self.purchaseAmount = self.deposit / percent_of_deposit
            self.coin = self.purchaseAmount / value
            self.deposit = self.deposit - self.purchaseAmount
            self.lastPrice = value
            return True
    
        #factor calculation Buying condition due to drammatic price drop
        if(self.lastPrice != -1) :
            profit_or_loss = value / self.lastPrice
            profit_or_loss = abs(profit_or_loss)
            if profit_or_loss >= 1.05:
                sell_factor += 1
            elif profit_or_loss > 1.04:
                sell_factor += 0.8
            elif profit_or_loss > 1.025:
                sell_factor += 0.5
            elif profit_or_loss > 1.01:
                sell_factor += 0.2
            elif profit_or_loss > 0.98:
                buy_factor += 0.2
            elif profit_or_loss > 0.94:
                buy_factor += 0.6
            elif profit_or_loss > 0.91:
                buy_factor += 0.7
            elif profit_or_loss > 0.89:
                buy_factor += 1
            
        

        if status == "OVERSOLD" and self.deposit > 0 and buy_factor >= 1:
            if self.purchaseAmount >= self.deposit:
                print("buy Happens1")
                #making average price
                acoin = self.deposit / value
                self.lastPrice = ((self.lastPrice * self.coin) + (value * acoin)) /(self.coin + acoin)
                self.coin += acoin
                self.deposit = 0
                return True
            else:
                print("buy Happens2")
                acoin = self.purchaseAmount / value
                self.lastPrice = ((self.lastPrice * self.coin) + (value * acoin)) /(self.coin + acoin)
                self.coin += acoin
                self.deposit -= self.purchaseAmount
                return True


        if status == "OVERBOUGHT" and self.coin > 0 and sell_factor >= 1:
            print("soldhappens")
            profit = self.coin * value - self.lastPrice * self.coin
            profit *= leverage
            self.deposit += self.coin * self.lastPrice + profit
            self.lastPrice = -1
            self.purchaseAmount = 0
            self.coin = 0
            return True

        def liquidation_calculator(leverage, entering_price, coinamount, deposit):
            
        if self.deposit < 0 :
            print("PAUSE-------------------")
        return False
        
        

        


    