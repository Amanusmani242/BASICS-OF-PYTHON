#program of game snake, water and gun.
import random
choice = ('s', 'w', 'g')
comp = random.randint(0, 2)
comp = choice[comp]
mine = input("choose either s,w or g:")

def swg(mine , comp):
    if(mine == comp):
      return None
    if(mine == 's' and comp == 'w' ):
        return True
    elif(mine == 'w' and comp == 'g' ):
        return True
    elif(mine == 'g' and comp == 's' ):
        return True
    else:
        return False

win = swg(mine , comp)
print(f"you chose {mine} and computer chose {comp}")
if win:
    print("you won")
elif(win is None):
    print("match draw play again")
else:
    print("you lose")




