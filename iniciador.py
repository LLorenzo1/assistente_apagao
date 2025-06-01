import cv2
import numpy as np
import time
import subprocess

def ambiente_escuro(frame, limite=60):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brilho_medio = np.mean(gray)
    return brilho_medio < limite

cap = cv2.VideoCapture(0)

print("Monitorando luminosidade... (Ctrl+C para parar)")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        if ambiente_escuro(frame):
            print("Ambiente escuro detectado. Iniciando assistente.")
            subprocess.call(["python", "main.py"])
            break  # Encerra o loop após iniciar o assistente

        time.sleep(2)  # Espera 2 segundos antes de checar de novo

except KeyboardInterrupt:
    print("\nMonitoramento foi interrompido pelo usuário.")

finally:
    cap.release()
