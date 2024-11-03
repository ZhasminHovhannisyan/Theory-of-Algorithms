def bubble_sort(arr, len):
    for i in range(len):
        for j in range(len - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
    return arr

length = int(input("number of list elements: "))
input_list = [float(input(f"input element {i+1}: ")) for i in range(length)]
output_list = bubble_sort(input_list, length)
print (output_list)
