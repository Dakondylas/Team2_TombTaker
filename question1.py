
def quiz_puzzle():
    print("You, Todd and Stephanie come across a long room, you can see a lever on the other end of the room and you look at the ground")
    print("Todd points out that those are definatly boobie traps and yall should proceed with cation then a ghostly figure of a snake decends from the heavens")
    print("Then the snake says in a heavenly voice \"Anwser my questions correctly and you get to move on\" ")
    print("Stephanie looks prepared and ready then yells \" bring it on you stinky gucci bag\" ")
    #this code ask the user for an awnser and if incorrrect put them though a loop only giving them 3 chances- idris
    x = 3
    while True:
        Q1 = input("Question 1) what part of the random module is inclusive:")

        if Q1.lower() == 'randint':
            print(" \"Corret move to the left pressure plate\", you walk to the left pressure plate and nothing happenes")
            break
        elif Q1.lower() !='randint':
            print(" \"incorrect\" the sly snake said")
            x -= 1
            print(f'you have {x} guesses left')
        if x == 0:
            print("you are all out of guesses then he hurls a  massive fire ball towards yall, you have died")
            quit()
quiz_puzzle()

