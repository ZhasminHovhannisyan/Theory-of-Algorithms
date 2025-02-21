# տրված է չկրկնվող անդամներով զանգված
# ու մի հատ target, որը հաստատ զանգվածից որևէ երկու թվերի գումար է ներկայացնում
# գտնել էտ երկու թվերի ինդեքսները


import random


# solution1: finds using two nested loops, so the time complexity is O(n2)

def function(list, targ):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if i != j and list[i]+list[j] == targ:
                return i, j


def calc_targ(arr):
    el1 = random.choice(arr)
    el2 = random.choice(arr)
    while el1 == el2:
        el2 = random.choice(arr)
    return el1 + el2


N = int(input("enter number of elements: "))
list1 = []
for i in range(N):
    list1.append(int(input(f"enter element {i}: ")))
target = calc_targ(list1)
i1,  i2 = function(list1, target)
print("Generated target is ",target)
print("The indexes are ", i1, i2)
