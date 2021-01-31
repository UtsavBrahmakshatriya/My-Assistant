import speech_recognition as sr
import pyttsx3

stt_engine = sr.Recognizer()
tts_engine = pyttsx3.init()
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice',voices[1].id)
try:
    with sr.Microphone() as speech:
        tts_engine.say("Hey there, I am your personal assistant Jasper. Would you like to give me a pet-name?")
        tts_engine.runAndWait()
        print("listening...")
        voice = stt_engine.listen(speech)
        text = stt_engine.recognize_google(voice,language="en-IN")
        text = text.lower()
        if text.startswith("no") or text.startswith("nope"):
            tts_engine.say("Okay.")
            tts_engine.runAndWait()
        elif text.startswith("yes") or text.startswith("yupp") or text.startswith("yup") or text.startswith("yeah"):
            tts_engine.say("Okay. So what should be my name?")
            tts_engine.runAndWait()
            name_voice = stt_engine.listen(speech)
            name = stt_engine.recognize_google(name_voice, language="en-IN")
            name = name.lower()
            print(name)
            tts_engine.say(name + ", that is a really good name. I liked it. Thanks.")
            tts_engine.runAndWait()
        # if text.startswith("jasper"):
        #     tts_engine.say(text)
        #     tts_engine.runAndWait()
        #     print(text)
except:
    pass
