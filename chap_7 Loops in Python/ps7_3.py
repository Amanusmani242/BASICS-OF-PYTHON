#program to find wether a given no is prime or not.
num =int(input("Enter the no:"))

for i in range(2,num):
    if(num%i == 0):
          print(f"{num} is not a prime no ")
          break

else:
       print(f"{num} is prime no")