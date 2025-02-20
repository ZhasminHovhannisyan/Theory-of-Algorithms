def selection_sort(arr, len):
    for i in range(len):
        min_index = i
        for j in range(i+1, len):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

length = int(input("The number of elements: "))
initial_list  = [float(input(f"element no {i+1} is: ")) for i in range(length)]
new_list = selection_sort(initial_list, length)
print(new_list)