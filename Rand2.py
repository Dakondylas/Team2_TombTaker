#Idris Sampson
#4/16/24
#function the begging of the end for our fearless acheologist
import random
def specialevo2():
    while True:
        specail_event2 = random.randint(1, 150)
        if specail_event2 == 2:
            print("ou have encounterd one of the many enchantresses")
            print("she begins to pull you towards her you cant do anything about it though")
        with open("variables.txt", "r") as file:
            if len(file.read()) == 5:
                print("you are not effected by the enchanttress since you have the medalion")
                break
            else:
                print("you lack the necesarry power to stop her and you die")
                import  DefeatandVictory
                DefeatandVictory.deadscreen()
                quit()