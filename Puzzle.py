#Idris Sampson
#4/16/24
#function the begging of the end for our fearless acheologist
import random
from Rand import *


def puzzle():
   key1 = 1
   key2 = 1
   key3 = 1

   while True:
      # all the code below, randomizer that will pick wether you take a quiz path or secret
      chooser = random.randint(1, 100)
      if chooser  == 55:
         from question1 import quiz_puzzle
         key1-=1
      if chooser == 2:
         secrets()
         if key1 == 1:
            from question1 import quiz_puzzle

      if key1 == 0:
         print("placeholder for puzzle")
         break
      if key1 + key2 == 0:
         print()
         break


puzzle()


