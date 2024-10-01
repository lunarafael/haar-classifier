import cv2
import matplotlib.pyplot as plt

# Carregar o classificador treinado (substitua pelo caminho correto para o seu arquivo cascade.xml)
cat_cascade = cv2.CascadeClassifier('classifier/cascade.xml')

# Lista de imagens para teste (substitua pelos caminhos corretos para suas imagens)
image_paths = ['images/cat.jpg', 'images/cat2.jpg', 'images/cat3.jpg', 'images/car.jpg', 'images/car2.jpg', 'images/car3.jpg']

# Função para processar e exibir cada imagem
def process_image(image_path):
    # Ler a imagem
    img = cv2.imread(image_path)

    # Verificar se a imagem foi carregada corretamente
    if img is None:
        print(f"Erro ao carregar a imagem: {image_path}")
        return

    # Converter para escala de cinza (necessário para a detecção Haar)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detectar objetos (neste caso, gatos) usando o classificador Haar
    cats = cat_cascade.detectMultiScale(gray, 6.5, 10)

    # Desenhar retângulos ao redor dos gatos detectados
    for (x, y, w, h) in cats:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Exibir a imagem com as detecções
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Desativar os eixos
    plt.show()

# Iterar sobre a lista de imagens e processar cada uma
for image_path in image_paths:
    process_image(image_path)