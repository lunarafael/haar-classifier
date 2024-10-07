# Projeto de Detecção de Gatos usando Classificador Haar

## Descrição do Projeto

Este projeto consiste na criação e utilização de um classificador Haar para detectar gatos em imagens. A equipe seguiu um fluxo de trabalho que envolveu o treinamento de um classificador Haar e o uso de um script em Python para testar a detecção. Apesar das tentativas iniciais sem sucesso, o classificador final foi gerado com o auxílio de um software de terceiros.

## Fluxo de Trabalho

### Tentativas Iniciais

1. **Primeira Tentativa**: Seguimos o tutorial disponível em [Creating a Cascade of Haar-like Classifiers](https://github.com/felipecbarelli/livro-visao-computacional/blob/master/tutoriais/creating-a-cascade-of-haar-like-classifiers.pdf) utilizando 100 imagens de cachorros (positivas) e 100 imagens negativas disponíveis no tutorial para o treinamento. Contudo, o resultado não foi satisfatório.
   
2. **Segunda Tentativa**: Aumentamos o número de imagens para 200 (positivas e negativas), trocando os exemplos para gatos positivamente e continuando com as imagens do tutorial negativamentes, mas novamente não obtivemos sucesso no treinamento do classificador.

3. **Terceira Tentativa**: Como sugestão do docente, tentamos utilizar o YOLOv5 para realizar a detecção de gatos e o desenho de bounding boxes. Apesar de uma boa parte da classificação estar correta nas bounding boxes, não foi possível gerar o XML do classificador Haar, pois a criação desse tipo de arquivo na biblioteca do OpenCV já é obsoleta e não encontramos outra forma de gerar o arquivo a partir das coordenadas positivas encontradas no conjunto de imagens.

4. **Comparação com treino pronto**: Utilizamos [um XML de classificador de gatos](https://github.com/haribaskar/CatDetection-HaarCascade) que foi encontrado no GitHub para comparação com as tentativas anteriores, que apresentou uma melhora em relação ao resultado da primeira e segunda tentativa.

### Solução Alternativa

Após as tentativas sem sucesso e a comparação, utilizamos o software [Cascade Trainer GUI](https://amin-ahmadi.com/cascade-trainer-gui/) para facilitar o processo de treinamento manual do classificador. Com ele, conseguimos treinar um classificador Haar utilizando:

- **150 imagens positivas (gatos)**.
- **150 imagens negativas (carros)**.

Essas imagens estão disponíveis em `src/training/p` e `src/training/n`, respectivamente. Também é possível encontrar os arquivos gerados pelo Cascade Trainer GUI em `src/training`. Caso deseje, os diretórios já estão organizados para serem utilizados no treinamento com essa ferramenta.
O treinamento foi realizado com essas imagens, configurado para ter 15 estágios, resultando em um arquivo XML que contém o classificador treinado.

### Teste de Detecção

Com um código Python, utilizamos o classificador Haar gerado para detectar a presença de gatos em imagens. O script carrega as imagens, aplica o classificador e exibe as imagens com os gatos detectados. Utilizamos 3 imagens de teste positivas e 3 negativas para verificar a eficácia do classificador.

### Fontes de Imagens

As imagens para o treinamento foram obtidas das seguintes fontes:

- **Imagens Positivas (gatos)**: [Kaggle Dataset - Cat and Dog](https://www.kaggle.com/datasets/tongpython/cat-and-dog?resource=download)
- **Imagens Negativas (carros)**: [Kaggle Dataset - Cars Image Dataset](https://www.kaggle.com/datasets/kshitij192/cars-image-dataset)

## Execução

O script de detecção foi executado utilizando o arquivo XML gerado. O código Python está disponível em `src/app/app.py` e utiliza o OpenCV para carregar as imagens, aplicar o classificador Haar, e detectar a presença de gatos nas imagens fornecidas.

## Instruções de Instalação e Execução

1. **Instale as dependências**:
   Certifique-se de ter o Python e as bibliotecas necessárias instaladas, especialmente o OpenCV e o Matplotlib. Para instalar as dependências, execute o seguinte comando:

   ```bash
   pip install opencv-python matplotlib
   ```

2. **Para executar**:
    ```bash
    cd src/app
    python app.py
    ```
