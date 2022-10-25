import random

def game(random):
    randomNO = random.randint(0,3)
    return randomNO

userNO = int(input("guess a no:"))
attempt = 0
num = game(random)
while(True):

 if(userNO > num):
    userNO=int(input(f"you guessed no is {userNO} and computer no is {num}.you guessed no is higher try again:"))
    attempt += 1
 elif(userNO < num):
    userNO=int(input(f"you guessed no is {userNO} and computer no is {num}.you guessed no is lower try again:"))
    attempt += 1
 else:
    print(f"you guessed no is {userNO} and computer no is {num}.you guessed correct in {attempt} attempts")
    break





