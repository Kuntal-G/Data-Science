#Stock Price Buy Sell--Leetcode

def max_profit(prices):
    
    min_value = float('inf')
    res = 0
    for price in prices:
        if price < min_value:
            min_value = price
        else:
            if  price - min_value > res:
                res = price - min_value
    return res




#Stock Price Buy Sell with K transaction --Leetcode

def max_profit_any_transaction(prices):
     
    maximumProfit=0
     
    for i in range(len(prices)-1):
        maximumProfit+=max(prices[i+1]-prices[i],0)
    
    return maximumProfit
         
#Stock Price Buy Sell with K transaction and cooldown--Leetcode
import sys
def maxProfit_cool(prices):
    sell = 0
    prev_sell = 0
    buy = -sys.maxsize
    prev_buy=0
    for price in prices:
        prev_buy = buy
        buy = max(prev_sell - price, prev_buy)
        prev_sell = sell
        sell = max(prev_buy + price, prev_sell)

    return sell
       
        



prices=[12, 14, 17, 10, 14, 13, 12, 15]
print(max_profit(prices))
print(max_profit_any_transaction(prices))
print(maxProfit_cool(prices))