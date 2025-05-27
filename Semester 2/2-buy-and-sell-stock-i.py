def profit(prices):

    if len(prices)<2:
        return 0
    
    max_profit = 0
    min_price = float('inf')

    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit

prices =[7,1,5,3,6,4]
result = profit(prices)
print(result)