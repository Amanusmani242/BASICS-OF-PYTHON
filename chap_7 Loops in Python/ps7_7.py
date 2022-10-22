#program to find the multiplication table of a given no reverse.
n = int(input("Enter the no:"))

for i in range(0,10):
    j = 9-i+1
    print(f"{n}X{j}={n*(j)}")