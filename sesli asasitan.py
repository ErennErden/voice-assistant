from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time

#reco sesi analiz etmek ve algılamak için
#playsound ses dosyasını oynatmaya yarar
#gtts gogle nin ses oluşturucusu


#ses tanıma moturunu değişkene tanımladık
r =sr.Recognizer()



#sesi hangi kaynaktan alacağımızı belirledik
def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        #gogle atıyor ve anlayamazsa unkunow eror veriyor
        try:
            voice = r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError:
            print("asistan: anlayamadım")
            #gogle yada internet ile ilgili bir sorun olunca bu hatayı veriyo
        except sr.RequestError:
            print("asistan: sistem çalışmıyor")
        return voice

#fonksiyona verilen stringi ses olarak kaydeder söyler ve ses kaydını siler
def speak(yazı):
    tts = gTTS(text=yazı, lang="tr" , )
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("Sizi dinliyorum")

while True:
    voice = record()
    if voice != "":
        voice = voice.lower()
        print(voice)
