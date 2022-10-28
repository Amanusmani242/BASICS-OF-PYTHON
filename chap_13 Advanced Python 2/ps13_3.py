#write a program to filter a list of numbers which are divisible by 5
def isDivisibleby5(n):
    if(n%5==0):
        return True
    return False

l =[5,4,10,11,13,15,20]
print(list(filter(isDivisibleby5,l)))