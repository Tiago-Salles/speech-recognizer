import speech_recognition as speechRecognition
import pyttsx3 
import datetime
import webbrowser

recognizer = speechRecognition.Recognizer()

def receiveCommands():
    speaker = pyttsx3.init()
    for voice in speaker.getProperty("voices"):
        if(voice.id == "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"):
            speaker.setProperty("voice", voice.id)
            speaker.setProperty("rate", 130)
    try:
        repeat = True
        with speechRecognition.Microphone() as source:
            while(repeat):
                print("listening...")
                audio = recognizer.listen(source)
                response = recognizer.recognize_google(audio)
                command = response.upper()
                if "PLEASE" in command: 
                    if "PLAY" in command:
                        speech = command.replace("play", "")
                        speaker.say("Playing" + speech.replace("easy", ""))
                    elif "TIME" in command:
                        time = datetime.datetime.now().strftime("%I:%M %p")
                        speaker.say("Now is" + time)
                    elif "OUTLOOK" in command:
                        speaker.say("Opening outlook")
                        webbrowser.open("https://outlook.office.com/mail/")
                    elif "GMAIL" in command.upper():
                        speaker.say("Opening gmail")
                        webbrowser.open("https://mail.google.com/mail/u/0/")
                    elif "FINISH" in command:
                        speaker.say("Good bye")
                        repeat = False
                else:
                    speaker.say("Dont be rude, say please")
                print(command)
                speaker.runAndWait()
    except:
        speaker.say("Did not understood, ending here, bye!")
        speaker.runAndWait()
    
receiveCommands()