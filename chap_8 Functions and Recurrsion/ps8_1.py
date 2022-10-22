#program using function to find greatest of three numbers.

def greatest(a,b,c):
    if(a > b):
        a1 = a
        return a1
    elif(c > a and b):
        c1 = c
        return c1
    else:
        a1 = b
        return a1


d = greatest(22,3,4)
print("the greatest no is:", d)

