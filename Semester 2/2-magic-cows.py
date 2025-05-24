import numpy as np

max_days = 50


def solve(max_cows, initial_farms, num_visits):

    initial_cows = [int(input(f"number of cows in farm {i + 1}: ")) for i in range(N)]

    queries = eval(input("which days will be the visits (input as a list): "))

    while len(queries) != num_visits:
        print("number of elements didn't match, input again")
        queries = eval(input("which days will be the visits (input as a list): "))
    
    for i in range(initial_farms):
        dp[0][initial_cows[i]] += 1

    for day in range(max_days):
        for i in range(max_cows+1):
            if i <= max_cows / 2:
                dp[day+1][2*i] += dp[day][i]
            else:
                dp[day+1][i] += 2 * dp[day][i]

    for i in range(num_visits):
        visiting_day = queries[i]
        print(sumrow(dp, visiting_day))


def sumrow(matrix, day):
    farms = 0
    for i in range(C+1):
        farms += matrix[day][i]
    return farms


C = int(input("max number of cows per farm: "))
N = int(input("initial number of farms: "))
M = int(input("Number of visits from the diary regulator: "))
dp = np.zeros((max_days + 1, C + 1), dtype=int)
solve(C, N, M)


# Usage example
# C, N, M = 9, 5, 3
# cows in farm 1, ..., 5 -> [4, 2, 5, 2, 1]
# visit days -> [2,4,5]   (input must be with square brackets)

# For each day number of cows will be [5, 6, 9, 17, 34, 68]
# So the output: 9, 34, 68