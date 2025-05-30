import cv2
import mediapipe as mp
from reconhecimento_voz import escutar_comando
from respostas import executar_comando
import pyttsx3

def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

falar("Assistente iniciado. Procurando por presença.")

cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(min_detection_confidence=0.6) as face_detection:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image_rgb)

        if results.detections:
            falar("Presença detectada. Você pode me dar os comandos, caso não saiba quais são, diga ajuda para eu te ajudar.")

            while True:
                comando = escutar_comando()
                print("Comando reconhecido:", comando)

                if comando.lower() in ["sair", "encerrar assistente", "parar", "desligar"]:
                    falar("Encerrando assistente. Até logo!")
                    break

                executar_comando(comando)
                falar("Pronto. Você pode dizer outro comando ou dizer 'sair' para encerrar.")

            break  # Encerra após o usuário sair

        cv2.imshow('Detecção de Presença', frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
