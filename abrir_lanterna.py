import cv2
import numpy as np

def mostrar_tela_branca():
    # Cria uma imagem branca (500px de altura, 800px de largura)
    tela = np.ones((500, 800, 3), dtype=np.uint8) * 255

    cv2.namedWindow("Lanterna", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Lanterna", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        cv2.imshow("Lanterna", tela)
        if cv2.waitKey(1) == 27:  # Pressione ESC para fechar
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    mostrar_tela_branca()
