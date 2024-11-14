import cv2
import numpy as np

# Inicializa a captura de vídeo pela webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro ao acessar a webcam!")
    exit()

# Definir o nível de água (intensidade para o nível mais baixo)
water_level = 50

# Configuração da janela no projetor
cv2.namedWindow('Projection', cv2.WINDOW_NORMAL)
cv2.moveWindow('Projection', 1920, 0)  # Ajuste a posição para o projetor
cv2.setWindowProperty('Projection', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Falha ao capturar frame")
        break

    # Converte o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplica o filtro Canny para detectar bordas
    edges = cv2.Canny(gray, 100, 200)

    # Aplica um mapa de cores baseado nas bordas
    color_map = cv2.applyColorMap(edges, cv2.COLORMAP_JET)

    # Criar uma máscara para as áreas abaixo do nível de água
    water_mask = cv2.inRange(gray, 0, water_level)

    # Criar uma imagem em tons de azul para simular a água
    water = np.zeros_like(frame)
    water[:, :] = (255, 0, 0)  # Azul em BGR

    # Combinar a água com o mapa de elevação
    combined = np.where(water_mask[:, :, np.newaxis] == 255, water, color_map)

    # Exibir a imagem combinada na tela normal
    cv2.imshow('Water Simulation', combined)

    # Exibir a imagem combinada no projetor
    cv2.imshow('Projection', combined)

    # Sai ao pressionar a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
