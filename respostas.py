import pyttsx3
import os

def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def executar_comando(comando):
    if "lanterna" in comando or "ligar lanterna" in comando:
        falar("Ligando a lanterna.")
        os.system("python abrir_lanterna.py")

    elif "dica" in comando or "dizer dica" in comando:
        falar("Evite abrir a geladeira durante o apagão.")

    elif "tempo" in comando or "quanto tempo sem luz" in comando:
        falar("Você está sem energia há aproximadamente 10 minutos.")

    elif "som" in comando or "ligar som" in comando:
        falar("Reproduzindo som ambiente.")
        os.system("python som_simulado.py")

    elif "ajuda" in comando:
        falar("Você pode dizer: ligar lanterna, ligar som, dizer dica, perguntar quanto tempo sem luz, ou ajuda.")

    else:
        falar("Desculpe, não entendi o comando.")
