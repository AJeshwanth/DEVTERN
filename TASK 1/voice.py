import speech_recognition as sr
import pyttsx3
import data
while True:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        print("Processing...")
    try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            engine = pyttsx3.init()
            word=["play song", "play video", "photos", "images"]
            answer=""
            t=text.split(" ")
            a=t[0]+" " +t[1]
            s=t[0]
            print(a, s)
            if a not in word and s not in word:
                answer=data.getinfo(text)
                answer=answer.split("\n")[1]
                print(answer)
            else:
                if a == "play song":
                    data.playsong(''.join(text[9:]))
                elif a == "play video":
                    data.playvideo(text[10:])
                elif s == "photos" or s=="images":
                    data.showphotos(text)
            engine.say(answer)
            engine.runAndWait()
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
