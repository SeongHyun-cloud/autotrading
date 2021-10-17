rsi + circulation auto trade backtesting program. <br/>

This program is combine with rsi trading strategy and circulation scalping strategy. 

https://public.bnbstatic.com/image/cms/article/body/202106/0123551429dae7094a5ffc278443f88c.png

>Buy situation:<br/>
>>Buys at that price with 20% of money from the wallet if the "factor" reaches over 1. <br/>
>>The algorithm should not purchase share once it has traded within 1 min 
>>>if rsi is lower than 40, add buy_factor of 0.4<br/>
>>>if rsi is lower than 30, add buy_factor of 0.5<br/>
>>>if rsi is lower than 20, add buy_factor of 0.6<br/>
>>>if rsi is lower than 10, add buy_factor of 0.7<br/>
>>>if rsi is lower than 5, add buy_factor of 0.8<br/>
>>>if margin is -1.0%, add buy_factor of 0.2<br/>
>>>if margin is -2.5%, add buy_factor of 0.5<br/>
>>>if margin is -4.0%, add buy_factor of 0.8<br/>
>>>if margin is -5.0%, add buy_factor of 1<br/>

>Sell situation:<br/>
>>Strategy 1:<br/>
>>>Sell the whole share of coin<br/>
>>>if rsi is higher than 60, add sell_factor of 0.4<br/>
>>>if rsi is higher than 70, add sell_factor of 0.5<br/>
>>>if rsi is higher than 80, add sell_factor of 0.6<br/>
>>>if rsi is higher than 90, add sell_factor of 0.7<br/>
>>>if rsi is higher than 95, add sell_factor of 0.8<br/>
>>>if margin is +1.0%, add sell_factor of 0.2<br/>
>>>if margin is +2.5%, add sell_factor of 0.5<br/>
>>>if margin is +4.0%, add sell_factor of 0.8<br/>
>>>if margin is +5.0%, add sell_factor of 1<br/>
>>Strategy 2:<br/>
>>> use the same method above but sell 50% this time. 

