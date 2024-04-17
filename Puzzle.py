#Idris Sampson
#4/16/24
#main function the begging of the end for our fearless acheologist
import random
from Rand import *
from question1 import *

def puzzle():

   while True:
      chooser = random.randint(1, 100)
      if chooser  == 55:
         quiz_puzzle()

      if chooser == 2:
         secrets()
         quiz_puzzle()

      with open("variables.txt", "r") as file:
         if len(file.read()) !=2:
            print("heyyyyyiiiiiiiiiiiiiiiiiiiiiiiiiii")
            break
puzzle()


