#write a program to display a/b where a and b are the integers. if b=0, display infinite by handling the ZeroDivision error.

try:
    a = int(input("Enter the a integer:"))
    b = int(input("Enter the b integer:"))
    print(a/b)

except ZeroDivisionError:
 print("division by zero error:")