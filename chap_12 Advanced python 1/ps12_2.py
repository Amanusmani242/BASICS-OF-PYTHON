# Write a program to print third ,fifth and seventh element from a list using enumarate fuction,

l1 =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


for index, item in enumerate(l1):
 if(index+1 == 3 or index+1 == 5 or index+1 == 7):
      print(item)
