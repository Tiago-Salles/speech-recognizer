import pywhatkit
import speech_recognition as speechRecognition
import pyttsx3 
import datetime
import webbrowser

recognizer = speechRecognition.Recognizer()
runRecognizer = True

def receiveCommands():
    speaker = pyttsx3.init()
    for voice in speaker.getProperty("voices"):
        if(voice.id == "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"):
            speaker.setProperty("voice", voice.id)
            speaker.setProperty("rate", 150)
    try:
        with speechRecognition.Microphone() as source:
            print("listening...")
            audio = recognizer.listen(source)
            response = recognizer.recognize_google(audio)
            command = response.upper()
            if "PLEASE" in command: 
                if "PLAY" in command:
                    song = command.replace("PLAY", "").replace("PLEASE", "")
                    speaker.say("Playing" + song)
                    pywhatkit.playonyt(song)
                    print(pywhatkit.__doc__)
                elif "TIME" in command:
                    time = datetime.datetime.now().strftime("%I:%M %p")
                    speaker.say("Now is" + time)
                elif "OUTLOOK" in command:
                    speaker.say("Opening outlook")
                    webbrowser.open("https://outlook.office.com/mail/")
                elif "GMAIL" in command:
                    speaker.say("Opening gmail")
                    webbrowser.open("https://mail.google.com/mail/u/0/")
                elif "GMAIL" in command:
                    speaker.say("Opening gmail")
                    webbrowser.open("https://mail.google.com/mail/u/0/")
                elif "NEW APP" in command:
                    speaker.say("Opening Azure in V2")
                    webbrowser.open("https://dev.azure.com/houseasy/_git/HouseasyFlutterAppV2/branches")
                elif "ACTUAL APP" in command:
                    speaker.say("Opening Azure in actual app")
                    webbrowser.open("https://dev.azure.com/houseasy/_git/HouseasyFlutterApp")
                elif "ACTUAL APP" in command:
                    speaker.say("Opening Azure in actual app")
                    webbrowser.open("https://dev.azure.com/houseasy/_git/HouseasyFlutterApp")
                elif "OFFICE" in command:
                    speaker.say("Opening the gather")
                    webbrowser.open("https://app.gather.town/app/qnYTErWAOgoz87Oi/antigoescritorio")
                elif "PIANO" in command:
                    speaker.say("Playing your piano album")
                    webbrowser.open("https://youtu.be/Jn09UdSb3aA")
                elif "GUITAR" in command:
                    speaker.say("Playing your classic guitar playlist")
                    webbrowser.open("https://www.youtube.com/watch?v=DsWKDfkEat8&list=RDDsWKDfkEat8&start_radio=1")
                elif "GITHUB" in command:
                    speaker.say("Opening your github")
                    webbrowser.open("https://github.com/Tiago-Salles")
                elif "TRANSLATOR PORTUGUESE" in command:
                    speaker.say("Opening translator")
                    webbrowser.open("https://translate.google.com.br/?hl=pt-BR&sl=pt&tl=en&op=translate")
                elif "TRANSLATOR ENGLISH" in command:
                    speaker.say("Opening translator")
                    webbrowser.open("https://translate.google.com.br/?hl=pt-BR&sl=en&tl=pt&op=translate")
                elif "GOOGLE" in command:
                    speaker.say("Opening google")
                    webbrowser.open("https://www.google.com/")
                else:
                    speaker.say("Improve me, and i will know what to do")
                    speaker.runAndWait()
            elif "THANK YOU" in command or "THANKS" in command:
                speaker.say("I am here for you!")
            elif "SORRY" in command:
                speaker.say("Dont worry")
            elif "ARE YOU" in command or "EASY ARE YOU" in command:
                speaker.say("I am aways here for you!")
            elif "FINISH" in command:
                    speaker.say("Good bye")
                    speaker.runAndWait()
                    return False
            else:
                speaker.say("Dont be rude, say please")
            print(command)
            speaker.runAndWait()
    except:
        pass

while runRecognizer != False:  
    runRecognizer = receiveCommands()