def quicksort (arr, start, end):
    if start >= end:
        return arr
        
    def partition(arr, start, end):
        pivot = arr[end]
        i = start - 1
        
        for j in range(start, end):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        i += 1
        arr[i], arr[end] = arr[end], arr[i]
        return i
    
    pivot = partition(arr, start, end)
    quicksort (arr, start, pivot-1)
    quicksort (arr, pivot + 1, end)
    return arr


array = [1,9,0,38,29,5,40,2,6]
result = quicksort(array, 0, len(array)-1)
print(result)