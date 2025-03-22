def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

some_array = [6,4,29,7,3,1,40,2,-1]
result = bubble_sort(some_array)
print(result)
            