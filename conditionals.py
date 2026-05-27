import random

hungerLvl = 2

while hungerLvl != 0:
    bananas = random.randint(0, 10)
    
    if bananas > 4:
        hungerLvl -= 1
        print("I have a bunch of bananas: {}. My hunger level is {}.".format(bananas, hungerLvl))
    elif bananas >= 1 and bananas <= 4:
        hungerLvl += 1
        print("I have a small bunch of bananas: {}. My hunger level is {}.".format(bananas, hungerLvl))
    else:
        hungerLvl += 2
        print("I have no bananas {}. My hunger level is {}.".format(bananas, hungerLvl))
    
    if hungerLvl > 10:
        print("I passed out!")
        break
    if hungerLvl == 0:
        print("I'm finally full!!")