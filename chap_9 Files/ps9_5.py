# Write a program to rename a file to "renamed_by_python.txt".
import os

oldname = input("enter the file name you want to rename:")
newname = input("enter the new name:")

with open(oldname, 'r') as f:
    text = f.read()
with open(newname,'w')as f:
    f.write(text)
os.remove(oldname)


