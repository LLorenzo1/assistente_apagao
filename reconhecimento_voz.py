import speech_recognition as sr

def escutar_comando():
    reconhecedor = sr.Recognizer()

    with sr.Microphone() as fonte:
        print("Ouvindo... Fale seu comando.")
        try:
            reconhecedor.adjust_for_ambient_noise(fonte, duration=1)
            audio = reconhecedor.listen(fonte, timeout=5)
            comando = reconhecedor.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {comando}")
            return comando.lower()
        except sr.WaitTimeoutError:
            print("Nenhum som detectado.")
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
        except sr.RequestError:
            print("Erro ao se conectar ao serviço de reconhecimento.")
        return None


if __name__ == "__main__":
    comando = escutar_comando()
    if comando:
        print(f"Comando reconhecido: {comando}")
    else:
        print("Nenhum comando foi entendido.")
