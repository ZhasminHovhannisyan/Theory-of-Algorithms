# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.


import random
# calculate random target for given array
def calc_targ(arr):
    el1 = random.choice(arr)
    el2 = random.choice(arr)
    while el1 == el2:
        el2 = random.choice(arr)
    return el1 + el2


# solution1: finds using two nested loops, time complexity O(n2)
def two_sum(list, targ):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if i != j and list[i]+list[j] == targ:
                return i, j



# solution2: mapping, time complexity O(n)
def two_sum_optimized(nums, target):
    visited = {}
    
    for i, num in enumerate(nums):
        remaining = target - num
        if remaining in visited:
            return [visited[remaining], i]
        visited[num] = i
    
    return None



list1 = [5, 6, 2, 10, 3, 21, 1, 17]
target = calc_targ(list1)
i1,  i2 = two_sum(list1, target)
i3, i4 = two_sum_optimized(list1, target)
print("Generated target is ",target)
print("solution1: ", i1, i2)
print("solution2: ", i3, i4)