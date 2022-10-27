#wtire a program to open three files 1.txt , 2.txt and 3txt. If any of the files are not
# present , a messeage  without exiting the program must be printed prompting the same.

try:
    with open('1.txt', 'r') as f:
        f.read()
    with open('2.txt', 'r') as f:
        f.read()
    with open('3.txt', 'r') as f:
        f.read()
except Exception as e:
    print(f"{e} file not present")



