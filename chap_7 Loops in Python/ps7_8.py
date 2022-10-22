#program to find the factorial of a given no using for loop.

n = int(input("Enter the no:"))
fact = 1
for i in range(1,n+1):
   fact = fact*i


print("factoral is",fact)