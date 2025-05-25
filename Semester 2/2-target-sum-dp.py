def find_target_sum_ways(nums, target):
    total = sum(nums)

    # if (total + target) is odd or the target is big, there are no possible solutions
    if (total + target) % 2 != 0 or abs(target) > total:
        return 0

    P = (total + target) // 2
    dp = [0] * (P + 1)
    dp[0] = 1

    for num in nums:
        for i in range(P, num - 1, -1):
            dp[i] += dp[i - num]

    return dp[P]


# usage examples
nums = [1,1,1,1,1]
target = 3
print(find_target_sum_ways(nums, target))  # output = 5

nums = [1, 2, 1, 1, 4, 3]
target = -6
print(find_target_sum_ways(nums, target))  # output = 5
