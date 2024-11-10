#import speech_recognition as sr
#import os



rec = sr.Recognizer()

#print(sr.Microphone().list_microphone_names())

#mic = sr.Microphone()

with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)
    print('Pode falar que eu vou gravar!')
    audio = rec.listen(mic)
try:
    
    texto = rec.recognize_google(audio, language="pt-BR")

    if "adicionar cadastro" in texto:
        os.system("start inserir_cadastro")

    print(texto)

except sr.UnknownValueError():
    print("Não entendi.")

