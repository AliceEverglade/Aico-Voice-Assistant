import speech_recognition as sr
sr.__version__
'3.8.1'


class Command:
    def __init__(self, command_input: [str], callback):
        self.command_input = command_input
        self.callback = callback

    def match(self, user_input: str):
        if user_input in self.command_input:
            return self.callback()


def command_recognition(command):
    triggers = []
#   print("Something has been said")


r = sr.Recognizer()
mic = sr.Microphone()


while True:
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        CommandActivation = r.recognize_google(audio)
        print(CommandActivation)
        command_recognition(CommandActivation)

    except sr.UnknownValueError:
        pass





