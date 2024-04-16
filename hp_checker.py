#This code if froom a diffrent project
hp = 100
def hp_checker(hp,bandage):
    if hp <= 2 and bandage >= 1:
        print("you start are feeling the affects of all your injuries.")
        hp_input = input("would you like to use bandages?(yes or no)")
        if hp_input == 'yes':
            hp = 10
            bandage -= 1
            print(f'currect hp after healing {hp}')
        elif hp_input == 'no':
            print("womp womp you dumb arnt you")
    elif hp <= 2:
        print("you are feeling the affects of all your injuries better find bandages")
    if hp <= 0:
        print("you have parished at the hands of unknown forces, guess you were not good enough")
        quit()

