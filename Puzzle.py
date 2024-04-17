#Idris Sampson
#4/16/24
#function the begging of the end for our fearless acheologist

import random


def puzzle():
   key1 = 1
   key2 = 1
   key3 = 1
   question_counter = 1
   grade_list = []
   while True:

      # all the code below, randomizer that will pick wether you take a quiz path or secret-idris
      chooser = random.randint(1, 100)
      if chooser  == 55:
         from question1 import quiz_puzzle
         key1-=1
      if chooser == 2:# this picks out the question - idris
         from Rand import secrets
         if key1 == 1:
            from question1 import quiz_puzzle
            key1-=1
            key2 +=1

      if key2 == 2:
         from YunusPuzzles import puzzle1
         puzzle1()
         key2-=1


      if key1 + key2 == 0:
         import questionBank




