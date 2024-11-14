import numpy as np
import cv2

try:
    from pykinect2 import PyKinectRuntime
    from pykinect2.PyKinectV2 import *
except ImportError:
    import freenect  # Caso use o Kinect v1

# Configuração inicial do Kinect
kinect = None
if 'PyKinectRuntime' in globals():
    kinect = PyKinectRuntime.PyKinectRuntime(FrameSourceTypes_Depth)
else:
    # Kinect v1 setup
    def get_depth():
        depth, _ = freenect.sync_get_depth()
        depth = depth.astype(np.uint8)
        return depth

water_level = 50  # Nível inicial de água

def process_depth_frame(depth_frame, water_level):
    # Normaliza os dados de profundidade para visualização
    if kinect:
        # Kinect v2
        depth_frame = np.reshape(depth_frame, (424, 512))  # Resolução do Kinect v2
    else:
        # Kinect v1
        depth_frame = get_depth()

    # Aplica um mapa de cores para visualização de relevo
    depth_colored = cv2.applyColorMap(depth_frame, cv2.COLORMAP_JET)

    # Criação das curvas de nível
    contours, _ = cv2.findContours(depth_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(depth_colored, contours, -1, (0, 0, 0), 1)  # Preto para linhas de contorno

    # Simula "água" em áreas de intensidade baixa
    water_mask = cv2.inRange(depth_frame, 0, water_level)
    water = np.zeros_like(depth_colored)
    water[:, :] = (255, 0, 0)  # Azul para áreas de "água"
    combined = np.where(water_mask[:, :, np.newaxis] == 255, water, depth_colored)

    return combined

# Configuração da janela no projetor
cv2.namedWindow('Projection', cv2.WINDOW_NORMAL)
cv2.moveWindow('Projection', 1920, 0)  # Ajuste a posição para o projetor
cv2.setWindowProperty('Projection', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    if kinect:
        # Kinect v2
        if kinect.has_new_depth_frame():
            depth_frame = kinect.get_last_depth_frame()
            depth_visual = process_depth_frame(depth_frame, water_level)
    else:
        # Kinect v1
        depth_visual = process_depth_frame(None, water_level)

    # Adiciona um indicador de nível de água na tela de projeção
    cv2.putText(depth_visual, f'Water Level: {water_level}', (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Exibe a visualização de relevo com marcações de contorno no projetor
    cv2.imshow('Projection', depth_visual)

    # Controle do nível de água com teclas 'w' e 's'
    k = cv2.waitKey(1) & 0xFF
    if k == ord('w'):
        water_level = min(255, water_level + 10)  # Aumenta o nível de água
    elif k == ord('s'):
        water_level = max(0, water_level - 10)   # Diminui o nível de água
    elif k == ord('q'):
        break  # Sai do programa ao pressionar 'q'

cv2.destroyAllWindows()
if kinect:
    kinect.close()
