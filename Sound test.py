#
# Dillon Kondylas
# 04/18/2024
# This stores all the voice lines in a class
# for this to work properly you need to pip install playsound
# I had some errors come up while installing playsound that were fixed by doing pip uninstall wheel and pip install wheel
# then doing pip install playsound
# also you need to have all the mp3 files in a folder called VoiceLines in the same location as this file

from playsound import playsound


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

    def __init__(self):
        pass

    def play(self, sound):
        playsound(sound)

# syntax: object.play(object, object.NameOfSound)
x = Voicelines
x.play(x, x.YeahNawIAintMessinWithThatShitVro)
