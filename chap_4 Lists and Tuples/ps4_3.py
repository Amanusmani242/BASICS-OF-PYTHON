#check that type cannot be changed in python
theTuple = (1,2,3,4,5,1,)
print(theTuple)
print(type(theTuple))
#theTuple[0] = 1 (the tuples cant be changed )
print(theTuple.count(1))