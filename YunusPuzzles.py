# Team 2 Project - " Tomb Taker"
# By Dillon, Idris and Yunus
# 4/19/2024
# Puzzles made by Yunus for the main and moving text
import time #  Importing time module
def moving_text(text):  # This function allows text to print at a reading pace
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.02)
        
def puzzle1():  # First puzzle
# True or false question
    moving_text("""You notice a tablet asking you [true or false question]""")  # Receiving input from question
    moving_text("Is it true? [1], or false?[2]?")
    Choice = input()
    Choice.lower()
    if Choice == "1":  #Checking if correct
        moving_text("correct")
    else:
        print("wrong")
 # Calls puzzle1

# Puzzle2
# True or false question
def puzzle2():
    var = input("A voice from below asks you [question] is this true? [1] Yes [2] No: ").lower() # Asks question and gets input
    while var != "1":
        if var == "2":
            break
        moving_text("Please input 1 or 2: ") # Checks answer
        if var == "1":
            print("correct")
            break
        if var == "2":
            print("wrong")
def puzzle3():
    # Puzzle 3
        #Simplest puzzle for MVP
    var = input("[question]? [1] Yes [2] No: ").lower()  # Asking question
    if var == "1": # Checking user input
        print("correct")
    if var == "2":
        print("wrong")