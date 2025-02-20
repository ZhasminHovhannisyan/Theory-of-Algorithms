def insertion_sort(arr):
    iterations = 0
    movements = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        iterations += 1
        while j >= 0 and key < arr[j]:
            movements += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return iterations, movements, arr

# # նաև համեմատությունների քանակը հաշվել



def merge_sort(arr):
    iterations = 0

    def merge(arr, l, m, r):
        nonlocal iterations
        n1 = m - l + 1
        n2 = r - m

        L = [0] * n1
        R = [0] * n2

        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        i = j = 0
        k = l

        while i < n1 and j < n2:
            iterations += 1
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort_helper(arr, l, r):
        nonlocal iterations
        if l < r:
            m = (l + (r - 1)) // 2
            merge_sort_helper(arr, l, m)
            merge_sort_helper(arr, m + 1, r)
            merge(arr, l, m, r)

    merge_sort_helper(arr, 0, len(arr) - 1)
    return iterations, None, arr



def selection_sort(arr):
    iterations = 0
    movements = 0
    comparison = 0
    n = len(arr)
    for i in range(n-1):
        min_index = i
        iterations += 1
        for j in range(i+1, n):
            comparison += 1
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            movements += 1
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return iterations, movements, comparison, arr


def main():
    n = int(input ("Մուտքագրեք զանգվածի չափը: "))
    arr = [float(input(f"մուտքագրեք էլեմենտ {i+1}: ")) for i in range(n)]
    
    print (f"\n Սկզբնական զանգվածը՝ {arr} \n")

    merge_iter, _ , arr2 = merge_sort(arr.copy())
    print ("Սորտավորման ալգորիթմ՝ merge sort", arr2)
    print(f"Իտերացիաներ: {merge_iter},  տեղափոխումներ չի իրականացնում \n")
    
    insertion_iter, insertion_move, arr1 = insertion_sort(arr.copy())
    print ("Սորտավորման ալգորիթմ՝ insertion sort", arr1)
    print(f"Իտերացիաներ: {insertion_iter},  տեղափոխումներ: {insertion_move} \n")

    selection_iter, selection_move, selection_comparison, arr3 = selection_sort(arr.copy())
    print ("Սորտավորման ալգորիթմ՝ selection sort", arr3)
    print(f"Իտերացիաներ։ {selection_iter},  տեղափոխումներ։ {selection_move}, համեմատումներ։ {selection_comparison} \n")
    
    if min(insertion_iter, merge_iter, selection_iter) == insertion_iter: 
        print("Ամենաքիչ իտերացիաների քանակն ունի insertion sort")
    elif merge_iter < selection_iter:
        print("Ամենաքիչ իտերացիաների քանակն ունի merge sort")
    else:
        print("Ամենաքիչ իտերացիաների քանակն ունի selection sort ")
        
    if insertion_move < selection_move:
        print("Ամենաքիչ տեղափոխումներն ունի insertion sort")
    else:
        print("Ամենաքիչ տեղափոխումներն ունի selection sort")
    
        
if __name__ == "__main__":
    main()
