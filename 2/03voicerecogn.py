import speech_recognition as sr


r = sr.Recognizer()

with sr.Microphone() as source:
    print('powiedz  cos:')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('powiedziales: {}', format(text))
    except:
        print('nie rozpznalem mowy')