def jump_game(array):       # O(n^2) time complexity
    n = len(array)
    if n <= 1:
        return 0

    jumps = 0
    index = 0

    while index < n - 1:
        max_step = array[index]
        if max_step == 0:
            return -1

        # end is reachable from current position
        if index + max_step >= n - 1:
            jumps += 1
            break

        best_next = index + 1
        for i in range(index + 2, index + max_step + 1):
            if i < n and i + array[i] > best_next + array[best_next]:
                best_next = i

        index = best_next
        jumps += 1

    return jumps

print("---first algorithm---")
nums = [2,3,1,1,4]
res = jump_game(nums)
print(res)



def jump_game_optimal(array):               # O(n) time complexity
    n = len(array)
    if n <= 1:
        return 0

    jumps = 0
    max_reach = 0
    current_end = 0

    for i in range(n - 1):
        if i > max_reach:
            return -1

        max_reach = max(max_reach, i + array[i])

        if i == current_end:
            jumps += 1
            current_end = max_reach

            if current_end >= n - 1:
                break

    return jumps



print("---second algorithm---")
nums = [2,3,1,1,4]
res = jump_game_optimal(nums)
print(res)
