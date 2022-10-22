#write a python function to remove a given word from a list and strip it at same time.

def process(l,word):
    word = word.strip()
    l.remove(word)
    return l


l1= [ 'aman','maaz','sajeed']

l1= process(l1,'aman')
print(l1)



