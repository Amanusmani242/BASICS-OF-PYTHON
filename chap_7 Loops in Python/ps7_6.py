#print this * using for loop take input from the user>
#           **
#           ***
n = int(input("Enter the n:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end="")
    print("\n",end="")
