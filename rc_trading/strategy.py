class RCstrategy:
    
    def __init__(self, priceQ, rsi, deposit, strategy):
        self.priceQ = priceQ
        self.coin = 0
        self.deposit = deposit
        self.rsi = rsi
        self.lastPrice = -1
        self.purchaseAmount = 0
        self.data = {}
        self.strategy_num = strategy
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
        leverage = 2
        fee_percent = 0.0002 * leverage


        if self.coin == 0 and status == "OVERSOLD" and factor >= 0.6 :
            #print("none Happens")
            self.purchaseAmount = self.deposit / percent_of_deposit
            self.coin = self.purchaseAmount / value
            fee = self.coin * value * fee_percent
            self.deposit = self.deposit - self.purchaseAmount - fee
            self.lastPrice = value
            return True

        #factor calculation Buying condition due to drammatic price drop
        if(self.lastPrice != -1) :
            profit_or_loss = value / self.lastPrice
            profit_or_loss = abs(profit_or_loss)
            if profit_or_loss >= 1.1:
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
                buy_factor += 0.5
            elif profit_or_loss > 0.91:
                buy_factor += 0.8
            elif profit_or_loss > 0.89:
                buy_factor += 1
            
        

        if status == "OVERSOLD" and self.deposit > 0 and buy_factor >= 1:
            if self.purchaseAmount >= self.deposit:
                #print("buy Happens1")
                #making average price
                acoin = self.deposit / value
                self.lastPrice = ((self.lastPrice * self.coin) + (value * acoin)) /(self.coin + acoin)
                self.coin += acoin
                fee = self.coin * value * fee_percent
                self.coin -= fee/value
                self.deposit = 0
                return True
            else:
                #print("buy Happens2")
                acoin = self.purchaseAmount / value
                self.lastPrice = ((self.lastPrice * self.coin) + (value * acoin)) /(self.coin + acoin)
                self.coin += acoin
                fee = self.coin * value * fee_percent
                self.deposit -= self.purchaseAmount - fee
                return True


        if self.strategy_num == 1:
            if status == "OVERBOUGHT" and self.coin > 0 and sell_factor >= 1.4:
                
                profit = self.coin * value - self.lastPrice * self.coin
                profit *= leverage
                fee = self.coin * value * fee_percent
                self.deposit += self.coin * self.lastPrice + profit - fee
                self.lastPrice = -1
                self.purchaseAmount = 0
                self.coin = 0
                return True
        elif self.strategy_num == 2:
            if status == "OVERBOUGHT" and self.coin > 0 and sell_factor >= 1.4:
                
                profit = self.coin * value - self.lastPrice * self.coin
                profit *= leverage
                fee = self.coin * value * fee_percent
                self.deposit += self.coin * self.lastPrice + profit - fee
                self.lastPrice = -1
                self.purchaseAmount = 0
                self.coin = 0
                return True
            elif status == "OVERBOUGHT" and self.coin > 0.0001 and sell_factor >= 1:
                
                sell_part = 2/3
                profit = (self.coin *value - self.lastPrice * self.coin) * sell_part
                profit *= leverage
                fee = self.coin*sell_part * value * fee_percent
                self.deposit += self.coin*sell_part * self.lastPrice + profit - fee
                self.coin = self.coin * (1 -sell_part)
                self.purchaseAmount = self.deposit / percent_of_deposit
                return True
        '''
        1/2 - 2657.62$
        2/3 - 2567.76
        3/4
        '''

        def liquidation_calculator():
            profit = self.coin * value - self.lastPrice * self.coin
            profit *= leverage
            total = self.deposit + self.coin*value - profit
            return total


        if liquidation_calculator() < 0 :
            input("LIQUIDAITON OCCURED")
        return False
        
        

        


    