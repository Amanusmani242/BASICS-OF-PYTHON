#write a list comprihension to print a list which contains the multiplication table of user
#entered number.
num = int(input("Enter the the no's:"))
multiplication = [i*num for i in range(1 , 11)]
print(multiplication)