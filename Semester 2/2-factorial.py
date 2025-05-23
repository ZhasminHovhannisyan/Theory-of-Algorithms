mylist = [1, 1]


def factorial(number):
    if number < len(mylist):
        return 
    else:
        for i in range(len(mylist), number+1):
            mylist.append(mylist[i-1] * i)
        
    return mylist

n = int(input("calculate factorial of "))
factorial(n)
print(mylist[-1])