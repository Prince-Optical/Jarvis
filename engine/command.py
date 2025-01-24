import pyttsx3
import speech_recognition as sr
import eel
import time

# speak function 
def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing...')
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said{query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        #speak(query)
        #eel.ShowHood()
        
    except Exception as e:
        return ""

    return query.lower()

@eel.expose
def allCommand(message=1):
    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    try:
        

        if "open" in query:
            print(" I Run")
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)

        elif "send message" in query or "call" in query or "video call" in query:
            from engine.features import findContact, whatsApp, makeCall, sendMessage
            flag = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                speak("Which mode you want to use whatsapp or mobile")
                preferance = takecommand()
                print(preferance)
                if "mobile" in preferance:
                    if "send message" in query or "send sms" in query:
                        speak("what message to send")
                        message = takecommand()
                        sendMessage(message,contact_no, name)

                    elif "phone call" in query:
                        makeCall(name , contact_no)

                    else:
                        speak("please try again")

                elif "whatsapp" in query:


                    if "send message" in query:
                        flag = 'message'
                        speak("what message to send")
                        query = takecommand()
                        
                    elif "call" in query:
                        flag = 'call'
                    else:
                        flag = 'video call'
                        
                    whatsApp(contact_no, query, flag, name)

                else:
                    speak("please try again not in preferance")


        else:
            from engine.features import chatBot
            chatBot(query)
            #print("Don't run")
    
        eel.ShowHood()
    except:
        print("error")
        text = "error"
        speak(text)
        eel.DisplayMessage('Error')
        allCommand()
        

    
#text = takecommand()  

#speak(text)