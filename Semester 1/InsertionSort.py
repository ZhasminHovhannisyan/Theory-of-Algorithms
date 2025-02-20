def insertion_sort(arr, length):
    for i in range(1,length):
        j = i-1
        pointer = arr[i]
        while (j >=0 and arr[j] > pointer):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = pointer
    return arr

length = int(input("The number of elements: "))
some_list = [float(input( f"Element no {i+1}: ")) for i in range (length)]
print(insertion_sort(some_list, length))

