#program to find greatest of four numbers entered by the user.
a = int(input("Enter the no:"))
b = int(input("Enter the no:"))
c = int(input("Enter the no:"))
d = int(input("Enter the no:"))
if(a > b):
    maxnum = a
else:
    maxnum = b
if(c > d):
    maxnum1 = c
else:
    maxnum1 = d
if(maxnum > maxnum1):
    print('greater is:', maxnum)
else:
    print('greater is:', maxnum1)