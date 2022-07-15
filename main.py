import speech_recognition as speechRecognition
import pyttsx3 
import datetime
import webbrowser
import pywhatkit
import bs4
import requests

recognizer = speechRecognition.Recognizer()
runRecognizer = True
speaker = pyttsx3.init()
speaker.setProperty("voice", [0])
speaker.setProperty("rate", 220)

def fetchData():
    response = requests.get("https://www.cnnbrasil.com.br/tudo-sobre/guerra-na-ucrania/")
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    datas = soup.find_all("a", {"class" : "home__list__tag"})
    return datas



def receiveCommands():
    
    try:
        with speechRecognition.Microphone() as source:
            print("Ouvindo...")
            audio = recognizer.listen(source)
            response = recognizer.recognize_google(audio, language="pt-br")
            command = response.upper()
            if "TOCAR" in command:
                song = command.replace("TOCAR", "").replace("POR FAVOR", "")
                speaker.say("Tocando" + song)
                pywhatkit.playonyt(song)
            elif "HORAS" in command:
                time = datetime.datetime.now().strftime("%H:%M")
                speaker.say("Agora é" + time)
            elif "DIA" in command and "COMECE" in command:
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
            elif "MEU" in command and "REPOSITÓRIO" in command:
                speaker.say("Abrindo seu git hub")
                webbrowser.open("https://github.com/Tiago-Salles")
            elif "TRADUTOR" in command and "PORTUGUÊS" in command:
                speaker.say("Abrindo o tradutor")
                webbrowser.open("https://translate.google.com.br/?hl=pt-BR&sl=pt&tl=en&op=translate")
            elif "TRADUTOR" in command and "INGLÊS" in command:
                speaker.say("Abrindo o tradutor")
                webbrowser.open("https://translate.google.com.br/?hl=pt-BR&sl=en&tl=pt&op=translate")
            elif "ROTINA" in command:
                routine = {}
            
                hasName = False
                while hasName != True:
                    #nome da rotina
                    speaker.say("Vamos lá! qual será o nome da rotina?")
                    speaker.runAndWait()
                    print("Ouvindo nome...")
                    audio = recognizer.listen(source)
                    response = recognizer.recognize_google(audio, language="pt-br")
                    command = response.upper()
                    print(command)
                    routine.update({"nome" : command.lower()})
                    hasName = True
                        
                hasDevice = False
                while hasDevice != True:
                    #aparelho
                    speaker.say("Qual aparelho usaremos?")
                    speaker.runAndWait()
                    print("Ouvindo aparelho...")
                    audio = recognizer.listen(source)
                    response = recognizer.recognize_google(audio, language="pt-br")
                    command = response.upper()
                    if "TV" in command:
                        print(command)
                        routine.update({"aparelho" : "TV " + command.replace("TV", "").lower()})
                        hasDevice = True
                    else:
                        routine.update({"aparelho" : command.lower()})
                        print(command)
                        hasDevice = True
                        
                hasAction = False
                while hasAction != True:
                    #ação - ligar / desligar
                    speaker.say("Ação de ligar ou desligar?")
                    speaker.runAndWait()
                    print("Ouvindo ação...")
                    audio = recognizer.listen(source)
                    response = recognizer.recognize_google(audio, language="pt-br")
                    command = response.upper()
                    print(command)
                    if "DESLIGAR" in command:
                        routine.update({"ação" : "desligar"})
                        hasAction = True
                    elif "LIGAR" in command:
                        routine.update({"ação" : "ligar"})
                        hasAction = True
                        
                hasVolume = False
                while hasVolume != True:
                    #volume - padrão / mudo
                    speaker.say("O volume será padrão ou mudo?")
                    speaker.runAndWait()
                    print("Ouvindo volume...")
                    audio = recognizer.listen(source)
                    response = recognizer.recognize_google(audio, language="pt-br")
                    command = response.upper()
                    print(command)
                    if "MUDO" in command:
                        routine.update({"volume" : "mudo"})
                        hasVolume = True
                    elif "PADRÃO" in command:
                        routine.update({"volume" : "padrão"})
                        hasVolume = True
                        
                hasChannel = False
                while hasChannel != True:
                    #canal - numero
                    speaker.say("Em qual canal vamos ligar?")
                    speaker.runAndWait()
                    print("Ouvindo canal...")
                    audio = recognizer.listen(source)
                    response = recognizer.recognize_google(audio, language="pt-br")
                    command = response.upper()
                    print(command)
                    if "5" in command:
                        routine.update({"canal" : "5"})
                        hasChannel = True
                    elif "4" in command:
                        routine.update({"canal" : "4"})
                        hasChannel = True
                        
                hasTime = False
                while hasTime != True:
                    #hora
                    speaker.say("Agora me diga o horário?")
                    speaker.runAndWait()
                    print("Ouvindo horário...")
                    audio = recognizer.listen(source)
                    response = recognizer.recognize_google(audio, language="pt-br")
                    command = response.upper()
                    print(command)
                    routine.update({"horário" : command.lower()})
                    hasTime = True
                    
                hasDays = False
                while hasDays != True:
                    #dias da semana 
                    speaker.say("Para finalizar, faremos isso em qual, ou quais dias?")
                    speaker.runAndWait()
                    print("Ouvindo dias...")
                    audio = recognizer.listen(source)
                    response = recognizer.recognize_google(audio, language="pt-br")
                    command = response.upper()
                    print(command)
                    if "TODOS" in command:
                        routine.update({"Recorrência" : "Todos os dias da semana"})
                        hasDays = True
                speaker.say("Muito bem! rotina criada, vamos aos detalhes")
                speaker.runAndWait()
                for element in routine:
                    speaker.say(element + routine[element])
                    speaker.runAndWait()
            elif "DAR" in command and "PERMISSÃO" in command and "CONVIDADO" in command:
                confirmedUser = False
                while confirmedUser != True:
                    #adicionar usuário 
                    speaker.say("Por favor, me digo o código do convidado?")
                    speaker.runAndWait()
                    print("Ouvindo código convidado...")
                    audio = recognizer.listen(source)
                    response = recognizer.recognize_google(audio, language="pt-br")
                    command = response.upper()
                    print(command)
                    guestCode = command
                    speaker.say("Confirmando, o código do convidado é " + guestCode)
                    speaker.runAndWait()
                    audio = recognizer.listen(source)
                    response = recognizer.recognize_google(audio, language="pt-br")
                    confirmation = response.upper()
                    if "SIM" in confirmation:
                        speaker.say("Convidado adicionado com sucesso")
                        speaker.runAndWait()
                        confirmedUser = True
            elif "NOTÍCIAS" in command and "GUERRA" in command:
                speaker.say("Buscando notícias sobre a guerra")
                speaker.setProperty("rate", 220)
                newsList = fetchData()
                for data in newsList:
                    speaker.say(data.text)
            elif "GOOGLE" in command:
                speaker.say("Abrindo o Google")
                webbrowser.open("https://www.google.com/")
            elif "OBRIGADO" in command:
                speaker.say("Estou aqui pra você!")
            elif "DESCULPA" in command or "DESCULPE" in command:
                speaker.say("Não se preocupe")
            elif "VOCÊ ESTÁ" in command or "POR AÍ" in command or "CADÊ VOCÊ" in command:
                speaker.say("Estou sempre aqui pra você!")
            elif "PODE DESCANSAR" in command:
                    speaker.say("Se precisar é só me chamar!")
                    speaker.runAndWait()
                    return False
            elif "ALEXA" in command and "O QUE" in command and "ACHA" in command:
                    speaker.say("Ela até funciona bem, mas é muito limitada, pede pra ela ligar o motor da piscina sem te fazer gastar muito, acho que não vai dar ka ka ka ka ka ka ka ka ka ka")
                    speaker.runAndWait()
            else:
                speaker.say("Me melhore, então saberei o que fazer")
                speaker.runAndWait()
                print(command)
                speaker.runAndWait()    
    except:
        pass

    
while runRecognizer != False:  
    runRecognizer = receiveCommands()