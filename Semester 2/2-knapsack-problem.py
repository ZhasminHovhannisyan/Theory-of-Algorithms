def knapsack(capacity, weights, values):

    n = len(weights)

    # DP table of size (n+1) x (capacity+1),

    dp = [[0] * (capacity+1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w_i, v_i = weights[i - 1], values[i - 1]
        for w in range(1, capacity + 1):
            dp[i][w] = dp[i-1][w]

            if w >= w_i:
                dp[i][w] = max(dp[i][w], dp[i-1][w-w_i] + v_i)
    

    items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            items.append(i)
            w -= weights[i-1] 

    return dp[n][capacity], items


if __name__ == "__main__":
    capacity = 7
    values = [2, 2, 4, 5, 3]
    weights = [3, 1, 3, 4, 2]
    max_value, items = knapsack(capacity, weights, values)
    print(max_value)
    print(items)
