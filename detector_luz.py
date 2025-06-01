import cv2

def ambiente_escuro(limite=50):
    cap = cv2.VideoCapture(0)  # Usa a webcam padrão do dispositivo

    if not cap.isOpened():
        print("Erro ao acessar a câmera.")
        return False

    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Erro ao capturar imagem.")
        return False

    # Faz a conversão para a escala de cinza
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Faz o calculo do brilho médio
    media_brilho = cinza.mean()

    # Se a média for baixa, considera como escuro
    return media_brilho < limite




