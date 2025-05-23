fib = [0,1]

def fibonacci(number):
    l = len(fib)
    if number < l:
        return
    else:
        for _ in range(l, number):
            fib.append(fib[-1] + fib[-2])

    return fib

n = int(input("fibonacci's element number "))
fibonacci(n)
print(fib[-1])
print(fib)