#program to find wether a given username contains less than 10 charcters or not.
username = input("enter the username:")

if(len(username) < 10):
    print("user name conatain less then 10 characters")
else:
    print("user name contain more then 10 characters")