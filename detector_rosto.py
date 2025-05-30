import cv2
import mediapipe as mp

def rosto_detectado():
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erro ao acessar a câmera.")
        return False

    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Erro ao capturar imagem.")
        return False

    # Converte para RGB (MediaPipe exige)
    imagem_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Inicia o detector de rostos
    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.6) as detector:
        resultado = detector.process(imagem_rgb)

        if resultado.detections:
            return True
        else:
            return False
