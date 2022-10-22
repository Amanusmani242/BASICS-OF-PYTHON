#program to print the pattern n=3
#    ***
#    **
#    *

def pattern(n):
    for i in range(n):
     print("*"*(n - i))

ans = pattern(3)