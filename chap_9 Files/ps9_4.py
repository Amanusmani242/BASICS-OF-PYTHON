#A file contains a word "Donkey" Multiple times you need to write a program which replaces with
# '#####' by updating the same file.

with open('ps9_4.txt', 'r') as f:
    text = f.read()

text = text.replace('Donkey','#####')

with open('ps9_4.txt','w') as f:
    f.write(text)
