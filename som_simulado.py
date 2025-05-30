import numpy as np
import sounddevice as sd

def tocar_tom(frequencia=432, duracao=4, volume=0.4):
    amostra = 44100
    t = np.linspace(0, duracao, int(amostra * duracao), False)
    onda = volume * np.sin(2 * np.pi * frequencia * t)
    sd.play(onda, amostra)
    sd.wait()

if __name__ == "__main__":
    tocar_tom()
