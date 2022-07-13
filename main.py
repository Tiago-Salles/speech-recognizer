import speech_recognition as speechRecognition
import pyttsx3 

recognizer = speechRecognition.Recognizer()

def recognize():
    try:
        with speechRecognition.Microphone() as source:
            speaker = pyttsx3.init()
            print("listening...")
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            for voice in speaker.getProperty("voices"):
                if(voice.id == "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"):
                    speaker.setProperty("voice", voice.id)
            speaker.say(command)
            print(command)
            speaker.runAndWait()
            
    except:
       pass

recognize()
