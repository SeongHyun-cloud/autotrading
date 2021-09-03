rsi + circulation auto trade backtesting program.

This program is combine with rsi trading strategy and circulation scalping strategy. 

https://public.bnbstatic.com/image/cms/article/body/202106/0123551429dae7094a5ffc278443f88c.png

Buy situation:
    Buys at that price with 20% of money from the wallet if the "factor" reaches over 1. 
    if rsi is lower than 40, add buy_factor of 0.4
    if rsi is lower than 30, add buy_factor of 0.5
    if rsi is lower than 20, add buy_factor of 0.6
    if rsi is lower than 10, add buy_factor of 0.7
    if rsi is lower than 5, add buy_factor of 0.8
    if margin is -1.0%, add buy_factor of 0.2
    if margin is -2.5%, add buy_factor of 0.5
    if margin is -4.0%, add buy_factor of 0.8
    if margin is -5.0%, add buy_factor of 1

    if 
Sell situation:
    Strategy 1:
        Sell the whole share of coin
        if rsi is higher than 60, add sell_factor of 0.4
        if rsi is higher than 70, add sell_factor of 0.5
        if rsi is higher than 80, add sell_factor of 0.6
        if rsi is higher than 90, add sell_factor of 0.7
        if rsi is higher than 95, add sell_factor of 0.8
        if margin is +1.0%, add sell_factor of 0.2
        if margin is +2.5%, add sell_factor of 0.5
        if margin is +4.0%, add sell_factor of 0.8
        if margin is +5.0%, add sell_factor of 1
    
    Stratege 2:
        Sell the 20% of shares that I have

    