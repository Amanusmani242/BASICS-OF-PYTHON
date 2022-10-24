#write a program to read the text from given file 'poems.txt' and find out wether it contains the word 'twinkle'.
with open('poem.txt','r') as f:
 if('twinkle' in f.read()):
    print("yes present")
 else:
     print("not present")