#program which find out wether a given name is present in a list  or not.
name = input("enter your name:").lower()
namelist = ['aman','maaz','sajeed']


if(name in namelist):
    print("your\t"+name+"\taccesses granted")
else:
    print("access denied!!!")

