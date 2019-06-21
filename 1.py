#!/usr/bin/python3
target=8979
maximum=10000

def gen_seq(start, end):
	lst=list()
	while start <= end:
		lst.append(start)
		start=start+1
	return lst
lst=gen_seq(1, maximum) 
def find(target, lst):
	if target in lst:
		if target > lst[len(lst)//2]:
                    
                    after_lst = gen_seq(lst[0]+len(lst)//2, lst[-1])
                    return find(target, after_lst)
		elif target < lst[len(lst)//2]:
                    before_lst = gen_seq(lst[0], lst[0]+len(lst)//2-1)
                    return find(target, before_lst)
		else:
		    print("find it {0}".format(target))
	else:
	    print("not find it {0}".format(target))
#find(target, lst)
#TypeError: unsupported operand type(s) for -: 'list' and 'list'
#i dont understand why [0,1,2,3,4,5] can not - [0,1,2,3]
def query(target, lst):
    left = 0
    right = len(lst) - 1
    while target in lst:
        mid = (left + right) // 2
        if target > lst[mid]:
            left = mid + 1
        elif target < lst[mid]:
            right = mid - 1
        else:
            return mid
    return None
#do not generate a new list, just use the index of list to generate a new virtual list


def query1(target, lst):
    left = 0
    right = len(lst-1)
    while target in lst:
        mid= (left + right) // 2
        if target > lst[mid]:
            left = mid + 1
        elif target < lst[mid]:
            right = mid - 1
        else:
            return mid
    return None
def prt(N):
    i = 1
    while i <= N:
        print(i)
        i=i+1
def prt2(N):
    if N != 0:
        prt(N-1)
        print(N)
#prt2(100000) 
n=29
a=list(n for n in range(n,-1,-1))
x=0.343
def multiple(n, a, x):
    i=0
    result=0
    while i <= n:
        result = result + a[i]*(x**i)
        i=i+1
    return result
#f(x) = a0 + x(a1 +x(...(an-1+x(an))...))
import datetime
s1 = datetime.datetime.now()
print(multiple(n, a, x))    
e1 = datetime.datetime.now()
print ((e1-s1).total_seconds())
def rev_multi(n, a, x):
    i=n
    result=a[n]
    while n>0:
        result=a[n-1] + x*result
        n=n-1
    return result
def rev_multi2(n, a, x):
    result = a[n]
    while n > 0:
        result=(a[n-1] + x*result/n)
        n = n - 1
    return result+1
    

s2 = datetime.datetime.now()
print(rev_multi(n, a, x))
e2 = datetime.datetime.now()
print ((e2-s2).total_seconds())
s3 = datetime.datetime.now()
print(rev_multi2(n, a, x))
e3 = datetime.datetime.now()
print ((e3-s3).total_seconds())
