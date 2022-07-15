import speech_recognition as speechRecognition
import pyttsx3 
import datetime
import webbrowser
import pywhatkit
import bs4
import requests

recognizer = speechRecognition.Recognizer()
runRecognizer = True

def fetchData():
    response = requests.get("https://www.cnnbrasil.com.br/tudo-sobre/guerra-na-ucrania/")
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    datas = soup.findChildren("a", {"class" : "home__list__tag"})
    return datas



def receiveCommands():
    speaker = pyttsx3.init()
    speaker.setProperty("voice", [0])
    speaker.setProperty("rate", 220)
    try:
        with speechRecognition.Microphone() as source:
            print("Ouvindo...")
            audio = recognizer.listen(source)
            response = recognizer.recognize_google(audio, language="pt-br")
            command = response.upper()
            if "POR FAVOR" in command: 
                if "TOCAR" in command:
                    song = command.replace("TOCAR", "").replace("POR FAVOR", "")
                    speaker.say("Tocando" + song)
                    pywhatkit.playonyt(song)
                    print(pywhatkit.__doc__)
                elif "HORAS" in command:
                    time = datetime.datetime.now().strftime("%H:%M")
                    speaker.say("Agora é" + time)
                elif "COMECE MEU DIA" in command:
                    webbrowser.open("https://outlook.office.com/mail/")
                    webbrowser.open("https://mail.google.com/mail/u/0/")
                    speaker.say("Tenha um bom dia, que você adquira muito conhecimento hoje")
                elif "EMAIL EMPRESARIAL" in command:
                    speaker.say("Abrindo email empresarial")
                    webbrowser.open("https://outlook.office.com/mail/")
                elif "EMAIL PESSOAL" in command:
                    speaker.say("Abrindo email pessoal")
                    webbrowser.open("https://mail.google.com/mail/u/0/")
                elif "NOVO APP" in command:
                    speaker.say("Abrindo repositório do V2")
                    webbrowser.open("https://dev.azure.com/houseasy/_git/HouseasyFlutterAppV2/branches")
                elif "APP ATUAL" in command:
                    speaker.say("Abrindo repositório do atual")
                    webbrowser.open("https://dev.azure.com/houseasy/_git/HouseasyFlutterApp")
                elif "ESCRITÓRIO" in command:
                    speaker.say("Abrindo o escritório")
                    webbrowser.open("https://app.gather.town/app/qnYTErWAOgoz87Oi/antigoescritorio")
                elif "PIANO" in command:
                    speaker.say("Tocando um albúm que você gosta")
                    webbrowser.open("https://youtu.be/Jn09UdSb3aA")
                elif "VIOLÃO CLÁSSICO" in command:
                    speaker.say("Tocando um albúm que você gosta")
                    webbrowser.open("https://www.youtube.com/watch?v=DsWKDfkEat8&list=RDDsWKDfkEat8&start_radio=1")
                elif "GIT HUB" in command:
                    speaker.say("Abrindo seu git hub")
                    webbrowser.open("https://github.com/Tiago-Salles")
                elif "TRADUTOR PARA PORTUGUES" in command:
                    speaker.say("Abrindo o tradutor")
                    webbrowser.open("https://translate.google.com.br/?hl=pt-BR&sl=pt&tl=en&op=translate")
                elif "TRADUTOR PARA INGLÊS" in command:
                    speaker.say("Abrindo o tradutor")
                    webbrowser.open("https://translate.google.com.br/?hl=pt-BR&sl=en&tl=pt&op=translate")
                elif "NOTÍCIAS" in command:
                    speaker.say("Buscando notícias")
                    speaker.setProperty("rate", 220)
                    news = fetchData()
                    speaker.say(news)
                elif "GOOGLE" in command:
                    speaker.say("Abrindo o Google")
                    webbrowser.open("https://www.google.com/")
                else:
                    speaker.say("Me melhore, então saberei o que fazer")
                    speaker.runAndWait()
            elif "OBRIGADO" in command:
                speaker.say("Estou aqui pra você!")
            elif "DESCULPA" in command:
                speaker.say("Não se preocupe")
            elif "VOCÊ ESTÁ" in command or "POR AI" in command or "CADE VOCÊ" in command:
                speaker.say("Estou sempre aqui pra você!")
            elif "PODE DESCANSAR" in command:
                    speaker.say("Se precisar é só me chamar!")
                    speaker.runAndWait()
                    return False
            else:
                speaker.say("Não seja grosseiro, diga por favor!")
            print(command)
            speaker.runAndWait()
    except:
        pass

while runRecognizer != False:  
    runRecognizer = receiveCommands()