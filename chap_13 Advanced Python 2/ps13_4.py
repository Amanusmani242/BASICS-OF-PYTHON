#write a program to find the maximum of the numbers in list using reduce Function.
from functools import reduce
def max(m,n):
    if(m>n):
        return m
    return n

a = [1,2,3,50]
maxNum = reduce(max ,a)
print(maxNum)