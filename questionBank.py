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
    # pass the codeword "caseSensative" into option1 to make the answer case sensative
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
    Question("1", "print(hello world)\nWill this print out \"Hello World\"?", "2", "python"),
    Question("3", "_____ will print \"Hello World\"", "print(\"Hello World\")", "python", "caseSensative"),
    Question("2", "print(hello world) will print \"Hello World\"", "2", "python"),
]

def getQuestion():
    x = random.choice(question_bank)
    question_bank.remove(x)
    return x.askQuestion()

for x in range(len(question_bank)):
    getQuestion()