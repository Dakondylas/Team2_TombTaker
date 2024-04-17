#Idris Sampson
#4/16/24
#function the begging of the end for our fearless acheologist
import random
def specialevo2():
    while True:
        specail_event2 = random.randint(1, 15000)
        if specail_event2 == 2:
            print()
        with open("variables.txt", "r") as file:
            if len(file.read()) == 5:
                print("you are not effected by the enchanttress since you have the medalion")
                break