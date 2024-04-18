#
# Dillon Kondylas
# 04/18/2024
# This stores all the voice lines in a class
# for this to work properly you need to pip install playsound
# I had some errors come up while installing playsound that were fixed by doing pip uninstall wheel and pip install wheel
# then doing pip install playsound
# also you need to have all the mp3 files in a folder called VoiceLines in the same location as this file

import playsound


class Voicelines:

    AnswerMyQuestionsCorrectly = "VoiceLines\AnswerMyQuestionsCorrectly.mp3"
    CorrectLeftPressurePlate = "VoiceLines\CorrectLeftPressurePlate.mp3"
    CorrectMiddlePressurePlate = "VoiceLines\CorrectMiddlePressurePlate.mp3"
    CorrectRightPressurePlate = "VoiceLines\CorrectRightPressurePlate.mp3"
    EnchantressDialog1 = "VoiceLines\EnchantressDialog1.mp3"
    EnchanttressDialog2 = "VoiceLines\EnchanttressDialog2.mp3"
    EnchanttressDialog3 = "VoiceLines\EnchanttressDialog3.mp3"
    IntroTomb1 = "VoiceLines\IntroTomb1.mp3"
    IntroTomb2 = "VoiceLines\IntroTomb2.mp3"
    StinkyGucciBag = "VoiceLines\StinkyGucciBag.mp3"
    TurnBackNowMonster = "VoiceLines\TurnBackNowMonster.mp3"
    TurnBackNowOrIWillMessYouUpMF = "VoiceLines\TurnBackNowOrIWillMessYouUpMF.mp3"
    WrongDie = "VoiceLines\WrongDie.mp3"
    YeahNawIAintMessinWithThatShitVro = "VoiceLines\YeahNawIAintMessinWithThatShitVro.mp3"
    Music = "VoiceLines\Music.mp3"
    HeavenlySnake1 = "VoiceLines\HeavenlySnake1.mp3"
    HeavenlySnake2 = "VoiceLines\HeavenlySnake2.mp3"
    SnakeLeftPressurePlate = "VoiceLines\SnakeLeftPressurePlate.mp3"
    SnakeDie = "VoiceLines\SnakeDie.mp3"
    Secret2 = "VoiceLines\Secret2.mp3"
    Secret1 = "VoiceLines\Secret1.mp3"
    Secret = "VoiceLines\Secret.mp3"
    TombIntro4 = "VoiceLines\TombIntro4.mp3"
    Black1="VoiceLines\Black1.mp3"
    Black2="VoiceLines\Black2.mp3"
    Black3="VoiceLines\Black3.mp3"


    def __init__(self):
        pass

    def play(self, sound):
        playsound.playsound(sound)

# syntax: object.play(object, object.NameOfSound)
#x = Voicelines
#x.play(x, x.TurnBackNowMonster)
