#program to accept marks of 6 studens and display them i a sorted manner
marksofS1 = int(input("Enter the marks:"))
marksofS2 = int(input("Enter the marks:"))
marksofS3 = int(input("Enter the marks:"))
marksofS4 = int(input("Enter the marks:"))
marksofS5 = int(input("Enter the marks:"))
marksofS6 = int(input("Enter the marks:"))
listofmarks =[marksofS1,marksofS2,marksofS3,marksofS4,marksofS5,marksofS6]
print(listofmarks)
listofmarks.sort()
print("the sorted list is:", listofmarks)