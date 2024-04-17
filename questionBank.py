#
# Dillon Kondylas
# 04/16/2024
# Question bank with the question class and list of question objects, as well as a function that will ask the user
# a random question and then delete that question from the list and return true or false based on whether the user got
# the question right

import random
class Question:
    # pass type as 1 for T/F, pass 2 for multiple choice, pass 3 for fill in the blank
    # pass answer as a number 1-4 to corralate with option1-4
    # pass either "python" or "networking" into topic for the topic
    # pass the codeword "caseSensative" into option1 for a fill in the blank to make the answer case sensative
    def __init__(self, type, question, answer, topic, option1="", option2="", option3="", option4=""):
        self.type = str(type)
        self.question = str(question)
        self.option1 = str(option1)
        if self.type == "1":
            self.option1 = "True"
            self.option2 = "False"
        elif self.type == "2":
            self.option2 = str(option2)
            self.option3 = str(option3)
            self.option4 = str(option4)
        self.answer = str(answer)
        self.topic = str(topic)


    def askQuestion(self):

        # will return True if the player got the question right, False if incorrect
        print()
        print(self.question)
        if self.type == "3":
            print("\nFill in the blank: \n")
            choice = input("")
            print()
            if self.option1 == "caseSensative":
                if self.answer == choice:
                    print("Good Job, you got it correct!!")
                    return True
                else:
                    print("Sorry that's not right...")
                    return False
            else:
                if self.answer.lower() == choice.lower():
                    print("Good Job, you got it correct!!")
                    return True
                else:
                    print("Sorry that's not right...")
                    return False
            print()
        else:
            if self.type == "1":
                print("\nTrue or False:")
            else:
                print("\nMultiple Choice")
            print(f"\n1. {self.option1}\n2. {self.option2}")
            if self.type == "2":
                print(f"3. {self.option3}\n4. {self.option4}")
            print("\n")
            choice = input()
            print()
            if self.answer == "1":
                if choice == self.answer or choice.lower() == self.option1.lower():
                    print("Good Job, you got it correct!!")
                    return True
                else:
                    print("Sorry that's not right...")
                    return False
            elif self.answer == "2":
                if choice == self.answer or choice.lower() == self.option2.lower():
                    print("Good Job, you got it correct!!")
                    return True
                else:
                    print("Sorry that's not right...")
                    return False
            elif self.answer == "3":
                if choice == self.answer or choice.lower() == self.option3.lower():
                    print("Good Job, you got it correct!!")
                    return True
                else:
                    print("Sorry that's not right...")
                    return False
            elif self.answer == "4":
                if choice == self.answer or choice.lower() == self.option4.lower():
                    print("Good Job, you got it correct!!")
                    return True
                else:
                    print("Sorry that's not right...")
                    return False
            else:
                print("Sorry that's not right...")
                return False
            print()


    def __str__(self):
        print("Type: ", self.type)
        print("Topic: ", self.topic)
        print("Question: ", self.question)
        if self.type == "1":
            print("Options: ", "\n1. ", self.option1, "\n2. ", self.option2)
        if self.type == "2":
            if self.option1 !="":
                print("Options: ", "\n1. ", self.option1)
            if self.option2 != "":
                print("2. ", self.option2)
            if self.option3 != "":
                print("3. ", self.option3)
            if self.option4 != "":
                print("4. ", self.option4)
        elif self.type == "3":
            print("Options: (Fill in the blank)")
        print("Answer: ", self.answer)

question_bank = [
    Question("1", "IPv6 addresses are shorter than IPv4.", "1", "networking"),
    Question("3", "The _______ method in Python can be used to split a string into a list of substrings based on a delimiter.", "split()", "python", "caseSensative"),
    Question("2", "Which of the following is used to define a function in python", "2", "python", "func", "def", "define", "function"),
    Question("1", "The HTTP protocol operates at the application layer of the OSI model.", "2", "networking"),
    Question("1", "In Python, a set cannot contain duplicate elements.", "1", "python"),
    Question("2", "Which of the following operators in Python is used for exponentiation?", "4",  "python", "%", "^", "X", "**"),
    Question("1", "In Python, a class can inherit from multiple parent classes.", "1", "python"),
    Question("3", "The _______ method in Python is used to remove an element from a list by its value.", "remove()", "python", "caseSensative"),
    Question("2", "Which of the following is a valid way to comment out multiple lines of code in Python?", "3", "python", "Using // at the beginning of each line","Enclosing the lines within /* and */", "using triple quotes", "Enclosing the lines within <!-- and -->"),
    Question("3", "In Python, the _______ function is used to find the length of a string.", "len()", "python"),
    Question("1", "WiFi can be used to connect wireless headphones to a computer?", "2", "networking"),
    Question("2", "Which device is an intermediary device?", "2", "networking", "Wifi Cable", "firewall", "server", "PC"),
    Question("3", "_____ is a network device with the primary function of providing information to other devices?", "server", "networking"),
    Question("2", "What is a common media used in networks?", "1", "networking", "copper", "wood", "air", "fire"),
    Question("3", "_____ carries data encoded into impulses of light?", "fiber", "networking"),
    Question("2", "What is the purpose of using twisted pairs of wires in an Ethernet cable?", "1", "networking", "to reduce interference", "to provide higher bandwidth", "to identify paths of data flow", "to ensure that the transmission of electrical signals is extended over a longer distance"),
    Question("1", "255.255.255.255 is the address used in an ARP request frame", "2", "networking"),
    Question("3", "a _____ address refers to the unique physical device", "mac", "networking")
]

# appends PT if they got a python question right, PF for python question wrong, NT for NEtwork question right, NF for network question wrong
grade_list = []

def story():
    if len(grade_list) == 0:
        print("\nSuddenly the sand in front of you swirls and gathers into a small storm, you and your friends cover your eyes as\n"
              "everyone is blasted with sand. When you open your eyes again there stands a shiny demon... in the middle... of the road...\n"
              "AND HE SAYS!!! \n𝖆𝖓𝖘𝖜𝖊𝖗 𝖒𝖞 𝖖𝖚𝖊𝖘𝖙𝖎𝖔𝖓𝖘 𝖆𝖓𝖉 𝖞𝖔𝖚 𝖘𝖍𝖆𝖑𝖑 𝖕𝖆𝖘𝖘...")
        input("(Press enter to continue)")
        

def getQuestion():
    x = random.choice(question_bank)
    question_bank.remove(x)
    question_topic = x.topic
    question_right = x.askQuestion()
    if question_right:
        if question_topic == "python":
            grade_list.append("PT")
        else:
            grade_list.append("NT")
    else:
        if question_topic == "python":
            grade_list.append("PF")
        else:
            grade_list.append("NF")


for x in range(10):
    story()
    print("\n\n", x+1)
    getQuestion()
def final_grading():
    print("Congrats you got a:")
    final_score = int(((grade_list.count("PT") + grade_list.count("NT"))/len(grade_list)) * 100)
    python_score = int(grade_list.count("PT")/(grade_list.count("PT") + grade_list.count("PF"))*100)
    network_score = int(grade_list.count("NT") / (grade_list.count("NT") + grade_list.count("NF")) * 100)
    print(f"Final Score:  {final_score}%")
    print(f"Python Score:  {python_score}%")
    print(f"Network Score:  {network_score}%")
    if 90 <= final_score <= 100:
        print("A")
        print("You Passed!")
        import DefeatandVictory
        DefeatandVictory.vicScreen()
        quit()
    elif 80 <= final_score < 90:
        print("B")
        print("You Passed!")
        import DefeatandVictory
        DefeatandVictory.vicScreen()
        quit()
    elif 70 <= final_score < 80:
        print("C")
        print("You Passed!")
        import DefeatandVictory
        DefeatandVictory.vicScreen()
        quit()
    elif 60 <= final_score < 70:
        print("D")
        print("You Failed!")
        import DefeatandVictory
        DefeatandVictory.deadscreen()
        quit()
    else:
        print("F")
        print("You Failed!")
        import DefeatandVictory
        DefeatandVictory.deadscreen()
        quit()

final_grading()
