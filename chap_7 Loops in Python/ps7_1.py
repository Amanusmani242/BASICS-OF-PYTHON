#program to print multiplication table of a givennumber using for loop.
num = int(input("Enter the no you want multiplication table of:"))
for i in range(0,10):
   # i = 9-i+1
    print(f"{num}X{1+i}={num*(i+1)}")
