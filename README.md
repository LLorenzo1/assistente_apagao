# 💡 Assistente de Apagão com Detecção de Presença e Voz

Este projeto foi desenvolvido como parte da disciplina de Engenharia de Software na FIAP (5º semestre), com o objetivo de criar uma solução prática para situações de falta de energia elétrica.

## ⚙️ Tecnologias utilizadas

- 🐍 Python 3.10  
- 🎙️ SpeechRecognition (com Google API)  
- 🧠 MediaPipe (para detecção de rosto)  
- 🔊 pyttsx3 (resposta por voz)  
- 🖥️ OpenCV (captura de vídeo)  
- 💡 Simulação de lanterna e sons  

## 🎯 Objetivo

Desenvolver um assistente inteligente que:

- Detecta automaticamente **falta de luz** no ambiente.  
- Usa a **webcam** para identificar a **presença de uma pessoa**.  
- Escuta comandos por **voz** e responde com **fala**.  
- Realiza ações úteis durante apagões.

## 🧠 Como funciona

1. O script `iniciador.py` monitora constantemente a **luminosidade do ambiente**.  
2. Ao detectar que está escuro, ele executa automaticamente o `main.py`.  
3. O `main.py` inicia a **detecção de rosto**.  
4. Quando um rosto é detectado, o assistente diz: *"Estou ouvindo, diga seu comando."*  
5. O usuário pode falar comandos como:

   - **"ligar lanterna"** → Simula iluminação na tela  
   - **"ligar som"** → Emite um som ambiente  
   - **"dizer dica"** → Informa uma dica útil no escuro  
   - **"quanto tempo"** → Responde um tempo estimado do apagão  
   - **"ajuda"** → Informa todos os comandos disponíveis  

## 🖥️ Execução do projeto

### 1. Clone o repositório

```bash
git clone
cd assistente_apagao
```

### 2. Crie e ative o ambiente virtual

```bash
python3.10 -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
.\venv\Scripts\activate  # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

#### Ou manualmente:

```bash
pip install opencv-python
pip install mediapipe
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio
```

> No macOS, pode ser necessário:
> ```bash
> brew install portaudio
> ```

### 4. Inicie o sistema

Execute o monitor de luminosidade (ele iniciará o assistente automaticamente quando detectar escuridão):

```bash
python iniciador.py
```

## 📂 Estrutura do projeto

```
assistente_apagao/
├── main.py                 # Lógica principal de detecção de rosto e comandos
├── iniciador.py            # Verifica luminosidade e executa o assistente
├── reconhecimento_voz.py   # Reconhecimento de fala com SpeechRecognition
├── respostas.py            # Ações e falas do assistente
├── abrir_lanterna.py       # Simula uma tela branca como lanterna
├── som_simulado.py         # Emite som ambiente sem precisar de arquivos .mp3
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação
```

## 👨‍💻 Desenvolvedores

**Nomes:** Lorenzo, André, Felipe  
**Curso:** Engenharia de Software – FIAP  
**Semestre:** 5º
