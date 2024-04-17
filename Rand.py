import random

def secrets():
   poison = 0
   madlion = 0
   while True:
      back = random.randint(1,200)
      specail_event= random.randrange(1, 1500)
      if specail_event == 4:
         print("As you further down the tomb, the ground caves from beneath you seperating you from your friends and"'\n'"making you decend about 30 feet. Once you reach the bottom you call out\"Todd, Stephanie\""'\n'"zero responce back  you look at your surrounding and see a long passage way leading to some where but you dont know where"'\n'"you follow this passage way all the way to the end to find a chest.You begin to open the chest then a giant snake pops")
         fight_flight= input("would you like to fight the the snake or run(F or R)")
         if fight_flight.lower() == 'f':
            print("you grab the knife from you boot socks and swing rapidly you where able to scrathc its eye but The snake succesfully dodged it"'\n'"you swing again but another miss then the snake lundges towards you then you stab it between its eyes successfully kiling it"'\n'"you see a shine in the chest but ensure of what it is you approach with cation you pear into the chest and see a golden madallion you put it on then clime up a rope your friends let down")
            madlion +=11
            break
         else:
            print("you made a mad dash for it returning to where you fell you see a rope and begin to climb up it with the snake is sharply on your tail slithering up the walls"'\n'"you climbed your way back up the wall with little to spare since you were bitten in the angle by the snake and you have now been poisoned")
            poison +=11
            break
      elif back == 200:
         break

   return poison, madlion

poison, madlion = secrets()

with open("variables.txt", "w") as file:
    file.write(f"Poison: {poison}\n")
    file.write(f"Madlion: {madlion}\n")