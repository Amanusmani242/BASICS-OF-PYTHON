#a list contains the multiplication table of 2 write a program to convert it to a vertical String
#of same numbers.
l = [i*2 for i in  range(1,11)]
st=''
for item in l:
 st += str(item)+'\n'

print(st)
