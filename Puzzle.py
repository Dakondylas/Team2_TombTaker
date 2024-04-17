#Idris Sampson
#4/16/24
#main function the begging of the end for our fearless acheologist
import random
from Rand import *

def puzzle():
   key1 = 1
   key2 = 1
   key3 = 1
   while True:
      chooser= random.randint(1, 100)
      if chooser  == 55:
         print("You, Todd and Stephanie come across a long room, you can see a lever on the other end of the room and you look at the ground")
         print("Todd points out that those are definatly boobie traps and yall should proceed with cation then a ghostly figure of a snake decends from the heavens")
         print("Then the snake says in a heavenly voice \"Anwser my questions correctly and you get to move on\" ")
         print("Stephanie looks prepared and ready then yells \" bring it on you stinky gucci bag\" ")
         Q1 = input("Question 1) what part of the random module is inclusive:")
         while True:
            x=3
            if Q1.lower() == 'randint':
               print(" \"Corret move to the left pressure plate\", you walk to the left pressure plate and nothing happenes")
               key1-=1
               break
            else:
               print(" \"incorrect\" the sly snake said")
               x-=1
               print(f'you have {x} guesses left')
               Q1 = input("Question 1) what part of the random module is inclusive:")
            if x == 0:
               print("you are all out of guesses then he hurls a  massive fire ball towards yall, you have died")
               quit()
      if key1 ==0:
         print("placeholder for puzzle")
         break

      if key1+key2 == 0:
         print()
         break

      if chooser == 2:
         secrets()
         chooser = 55
      with open("variables.txt", "r") as file:
         if len(file.read()) == 2:
            print("heyyyyyiiiiiiiiiiiiiiiiiiiiiiiiiii")
puzzle()


