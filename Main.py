#Idris Sampson
#4/16/24
#main function the begging of the end for our fearless acheologist
#get player input and desired race of choice made by idris
print('You are a fearless archaeologist who begins his adventure by venturing to Egypt to enter the tomb of King Ramesses.')
player = input("what is your name:")
race = input("what race are you White, Black, Asian or Hispanic")
while True:
    if race.lower() == 'white':
        print()
        break
    elif race.lower() == 'black':
        print("You and your friends Jamar and Tyrone bust open the door to the tomb, as you guys fully open the tomb a huge gust of wind carrying a s**t ton of sand and"'\n'"dust comes flying out from the inside of the tomb, and from the bowels of it you hear “Turn back now or I will f**k you up” *in an echoing taunt*"'\n'"")
        break
    elif race.lower() == 'asain':
        print()
        break
    elif race.lower() == 'hispanic':
        print()
        break
    else:
        print("must be White, Black, Asian or Hispanic")
        race = input("what race are you White, Black, Asian or Hispanic:")