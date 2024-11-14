import numpy as np
import cv2

# Define o nível inicial de água fora do loop
water_level = 50  # Nível inicial de água

def process_depth_frame(frame, water_level):
    # Converte para escala de cinza para simular profundidade
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Normaliza a imagem em escala de cinza para simular diferentes elevações
    normalized_frame = cv2.normalize(gray_frame, None, 0, 255, cv2.NORM_MINMAX)

    # Define intervalos para simular elevações específicas (faixas de relevo)
    intervals = [50, 100, 150, 200, 250]  # Defina os níveis de contorno

    # Criação da imagem colorida para simular relevo
    depth_colored = cv2.applyColorMap(normalized_frame, cv2.COLORMAP_JET)

    # Desenha as curvas de nível em intervalos específicos
    for level in intervals:
        # Cria uma máscara para o nível atual
        _, contour_mask = cv2.threshold(normalized_frame, level, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(contour_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Desenha os contornos sobre a imagem colorida
        cv2.drawContours(depth_colored, contours, -1, (0, 0, 0), 1)  # Preto para as linhas de contorno

    # Simula "água" em áreas de intensidade baixa
    water_mask = cv2.inRange(normalized_frame, 0, water_level)
    water = np.zeros_like(depth_colored)
    water[:, :] = (255, 0, 0)  # Azul para áreas de "água"
    combined = np.where(water_mask[:, :, np.newaxis] == 255, water, depth_colored)

    return combined

# Inicializa a captura de vídeo pela webcam
cap = cv2.VideoCapture(0)

# Configuração da janela no projetor
cv2.namedWindow('Projection', cv2.WINDOW_NORMAL)
cv2.moveWindow('Projection', 1920, 0)  # Ajuste a posição para o projetor (assumindo que o projetor é a segunda tela)
cv2.setWindowProperty('Projection', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    # Captura o frame da webcam
    ret, frame = cap.read()
    if not ret:
        print("Falha ao capturar frame")
        break

    # Processa o frame para simular profundidade e contornos na projeção
    depth_visual = process_depth_frame(frame, water_level)

    # Adiciona um indicador de nível de água na tela da projeção
    cv2.putText(depth_visual, f'Water Level: {water_level}', (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Exibe a visualização do projeto com linhas de contorno e simulação de relevo no projetor
    cv2.imshow('Projection', depth_visual)

    # Exibe a imagem da câmera no monitor principal (em cores ou escala de cinza)
    gray_display = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Converte para escala de cinza
    cv2.imshow('Camera Feed', frame)  # Alternar entre `frame` (imagem normal) ou `gray_display` para escala de cinza

    # Controle do nível de água com teclas 'w' e 's'
    k = cv2.waitKey(1) & 0xFF
    if k == ord('w'):
        water_level = min(255, water_level + 10)  # Aumenta o nível de água
    elif k == ord('s'):
        water_level = max(0, water_level - 10)   # Diminui o nível de água
    elif k == ord('q'):
        break  # Sai do programa ao pressionar 'q'

cap.release()
cv2.destroyAllWindows()
