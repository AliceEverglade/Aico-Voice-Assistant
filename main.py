import time

import speech_recognition as sr
import pyautogui


# "Aico please close this application"
# "Aico please google why are bananas so hot"
#listen to voice /////
#check for [Aico] <-
#check for command after Aico
#check what command
#activate command

def command_google(google: str):
    pyautogui.keyDown("alt")
    pyautogui.press("space")
    pyautogui.keyUp("alt")
    pyautogui.typewrite("www.google.com")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.typewrite(google)
    pyautogui.press("enter")


class Command:
    def __init__(self, command_input: [str], callback):
        self.command_input = command_input
        self.callback = callback

    def match(self, user_input: str):
        for command in self.command_input:

            if user_input.startswith(command):
                return self.callback(user_input[len(command):])

        return False


def command_recognition(command: str):
#   storing versions the speech
    aico = ["ico", "i go", "aiko", "aico"]
    command_list = [
        Command(command_input=["please google"], callback=command_google()),
        ]
    command_input = command.lower().split(" ")
#   check where Aico is in the string
    for pos, com in enumerate(command):
        if com in aico:
#           check for what command is being called

            for command_class in command_list:
                if result := command_class.match(command_input):
#                    command_class.callback


    #command_1 = Command([])


r = sr.Recognizer()
mic = sr.Microphone()


while True:
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        CommandActivation = r.recognize_google(audio)
        print(CommandActivation)
        command_google(CommandActivation)

    except sr.UnknownValueError:
        pass





