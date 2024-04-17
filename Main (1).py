#Idris Sampson
#4/16/24
#main function the begging of the end for our fearless acheologist
#get player input and desired race of choice made by idris
from Puzzle import *
print('You are a fearless archaeologist who begins his adventure  with his friends by venturing to Egypt to enter the tomb of King Ramesses.')
player = input("what is your name:")
race = input("choose race are you White or Black:")


print("As you guys further deeper into the tomb Todd begins to get hesitant due to the creepy event unfloding such as creepy noises and huge spider and this isnt Australia and dashes to the exit like a titan from AOT with his hands flailing left and right.")
trick_rooni = input("Would you like to leave with him (yes or no)")
if trick_rooni == 'yes':
    print("You grab onto Stephanie’s arm and also begin to make a mad dash to the exit then the door suddenly shuts right infront Todd almost crushing him, These events are almost like the entity doesn't want y'all to leave.")
    puzzle()
elif trick_rooni == 'no':
    print("As your narrarator I would have suggested running with Todd but now it is to late."'\n'"You decided not to run away with Todd so he was able to escape while you and Stephanie continued down the tomb."'\n'"Then yall remebered Todd had all the food so yall died")
    quit()

