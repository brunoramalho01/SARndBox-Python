# Caixa de Areia de Realidade Aumentada
Este projeto é uma Caixa de Areia de Realidade Aumentada que simula relevos e níveis de água, projetando visualizações em uma superfície de areia com base em dados de profundidade capturados por uma câmera (Kinect ou webcam).

## Índice

- Materiais Necessários
- Instalação
- Configuração
- Uso
- Funcionamento do Projeto
- Contribuição
- Licença

## Materiais Necessários

### Hardware

- **Caixa de areia:** Caixa de madeira ou plástico com areia, usada para projetar relevos.
- **Câmera Kinect (Kinect v1 ou Kinect v2) ou webcam:** Captura dados de profundidade (ou intensidade de luz, no caso da webcam).
- **Projetor digital:** Projeta a visualização gerada pelo software na superfície da areia.
- **Computador:** Processa os dados de profundidade e gera a visualização. Recomenda-se um computador com capacidade gráfica intermediária.

### Outros Equipamentos

- **Suporte para projetor e câmera:** Para posicionar o projetor e a câmera diretamente acima da caixa de areia, garantindo alinhamento e captura corretos.
- **Fonte de luz (caso esteja usando webcam):** Para simular profundidade com base na intensidade de luz refletida

## Instalação

### 1. Preparação do Ambiente
- **a) Linux (recomendado para Kinect)**

- **Drivers do Kinect:**

  - **Kinect v1: Instale o libfreenect com o comando:**
        
        sudo apt-get install freenect

- **Kinect v2:** Utilize o SDK do Kinect para Windows ou Linux, ou a biblioteca libfreenect2.

**b) Windows (compatível com Kinect e Webcam)**

**Drivers do Kinect:**

Baixe e instale o Kinect SDK para o seu modelo:
 - Kinect v1 SDK:

    https://www.microsoft.com/en-us/download/details.aspx?id=40278

 - Kinect v2 SDK:

    https://www.microsoft.com/en-us/download/details.aspx?id=44561

### 2. Instalação das Dependências

- Clone o repositório do projeto:

    ```
    git clone https://github.com/brunoramalho01/SARndBox-Python.git
    cd SARndBox-Python
- Instale as dependências do Python:
    ```
    pip install opencv-python numpy
- Para uso com Kinect v1, instale freenect:
    ```
    pip install freenect
 - Para uso com Kinect v2, instale pykinect2 (somente em Windows):
    ```
    pip install pykinect2

## Configuração

### Posicionamento do Equipamento

- **Caixa de Areia:** Coloque a caixa em uma superfície plana.
- **Projetor e Câmera:** Posicione ambos diretamente acima da caixa de areia, apontando para baixo. Alinhe a câmera e o projetor para cobrir toda a área da caixa.
- **Fonte de Luz (para webcam):** Posicione a fonte de luz diretamente acima da caixa para iluminar de forma uniforme.

## Ajuste do Código
- **Defina o dispositivo de captura no código:**

    - Para Kinect, ajuste a parte de captura para PyKinectRuntime (Kinect v2) ou freenect (Kinect v1).

    - Para webcam, use cv2.VideoCapture(0).

## Uso

**1. Execução do Código:**

- Execute o script principal para iniciar o sistema de projeção e visualização.
    ```
    python SARndbox-Webcam.py
    
    ou
    
    python SARndbox-Kinect.py
**2. Controles:**

- **Tecla 'w':** Aumenta o nível de água, simula alagamento.
- **Tecla 's':** Diminui o nível de água.
- **Tecla 'q':** Encerra o programa.

### Interação:

- Movimente a areia para criar diferentes elevações e depressões.
- Observe a projeção no projetor digital, que mostrará áreas mais altas com cores quentes e áreas baixas simulando água.

## Funcionamento do Projeto
**1. Captura de Profundidade:**

- **Com Kinect:** O sensor captura dados de profundidade em tempo real.
- **Com webcam:** A intensidade da luz refletida simula profundidade, com áreas mais claras representando elevações.

**2. Processamento de Imagem:**
- A profundidade ou intensidade de luz é normalizada e convertida em uma imagem colorida, simulando relevos com um mapa de cores.
- Contornos são desenhados para destacar as "curvas de nível".

**3. Simulação de Nível de Água:**
- Baseado em um valor ajustável (water_level), o sistema aplica uma máscara nas áreas de baixa elevação para simular água, com a cor azul representando inundações.

## Contribuição
- Fork o projeto e crie uma branch para suas alterações.
- Envie um Pull Request para contribuir com melhorias ou correções.
- Sinta-se à vontade para adicionar sugestões e abrir issues para discutir melhorias.

## Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.


