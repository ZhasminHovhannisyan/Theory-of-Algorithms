def several_profits(prices):

    if len(prices) < 2:
        return 0

    max_profit = 0

    for i in range(1, len(prices)):
        diff = prices[i] - prices[i - 1]
        if diff > 0:
            max_profit += diff

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
result = several_profits(prices)
print(result)

