def two_transaction_profit(prices):

    if len(prices) < 2:
        return 0

    first_buy = float('inf')
    first_profit = 0
    second_buy = float('inf')
    second_profit = 0

    for price in prices:

        first_buy = min(first_buy, price)
        first_profit = max(first_profit, price - first_buy)
        second_buy = min(second_buy, price - first_profit)
        second_profit = max(second_profit, price - second_buy)

    return second_profit

prices = [3,3,5,0,0,3,1,4]
result = two_transaction_profit(prices)
print(result)
