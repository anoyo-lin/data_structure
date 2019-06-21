#!/usr/bin/python3\
def rev(lst, target):
    left = 0
    right = len(lst) - 1
    while target in lst:
        middle = (left + right)//2
        if target > lst[middle]:
            left = middle + 1
        elif target < lst[middle]:
            right = middle -1
        else:
            return middle
    return None
print (rev([1,4,6,8,20,500], 6))
