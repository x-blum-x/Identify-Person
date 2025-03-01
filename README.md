# Rastreamento de Pessoas em Tempo Real com YOLOv5 e Filtro de Kalman

Este projeto implementa um sistema de rastreamento de pessoas em tempo real utilizando a biblioteca YOLOv5 e um filtro de Kalman para suavizar o rastreamento. A aplicação captura vídeo da webcam, detecta pessoas e rastreia seus movimentos, exibindo os resultados na tela com caixas delimitadoras e IDs únicos.

## Funcionalidades

- Detecção de pessoas em tempo real usando YOLOv5.
- Rastreamento de pessoas com IDs únicos.
- Uso de filtro de Kalman para suavizar o rastreamento.
- Exibição do tempo de permanência de cada pessoa na tela.
- Suporte para execução em Windows e Linux.

## Requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)
- Webcam (para captura de vídeo em tempo real)

## Dependências

As seguintes bibliotecas Python são necessárias:

- `opencv-python`
- `numpy`
- `torch`
- `torchvision`
- `scipy`
- `requests`

## Instalação

### Windows

1. **Instale o Python**:
   - Baixe e instale o Python a partir do site oficial.
   - Certifique-se de marcar a opção "Add Python to PATH" durante a instalação.

2. **Crie e ative um ambiente virtual**:
   ```bash
   python -m venv nome_do_ambiente
   nome_do_ambiente\Scripts\activate

3. **Instale as dependências**:
    ```bash
    pip install opencv-python numpy torch torchvision scipy requests

### Linux

1. **Instale o Python**:
    - Use o gerenciador de pacotes da sua distribuição, exemplo:
    ```bash
    sudo apt update
    sudo apt install python3 python3-venv python3-pip

2. **Crie e ative um ambiente virtual**:
    ```bash
    python3 -m venv nome_do_ambiente
    source nome_do_ambiente/bin/activate

3. **Instale as dependências**:
    ```bash
    pip install opencv-python numpy torch torchvision scipy requests

## Execução

### Windows

1. **Ative o ambiente virtual (se ainda não estiver ativo)**:
    ```bash
    nome_do_ambiente\Scripts\activate

2. **Execute o script**:
    ```bash
    python caminho\para\seu\script\app.py

### Linux

1. **Ative o ambiente virtual (se ainda não estiver ativo)**:
    ```bash
    source nome_do_ambiente/bin/activate

2. **Execute o script**:
    ```bash
    python caminho\para\seu\script\app.py

### Estrutura do Projeto

- **person_tracker.py**: Script principal que implementa o rastreamento de pessoas.
- **kalman_filter.py**: Contém a classe Person e a lógica do filtro de Kalman.
- **tracker_utils.py**: Funções utilitárias para cálculo de distância e verificação de bounding boxes.
- **config.py**: Configurações globais, como limiares de distância e confiança.

### Problemas Conhecidos

- **Conflito de nomes com o módulo utils do YOLOv5**: Certifique-se de que o arquivo utilitário do projeto esteja nomeado como tracker_utils.py para evitar conflitos.
- **Aviso de depreciação**: Se você encontrar avisos relacionados ao NumPy, atualize o código conforme descrito na seção de solução de problemas.
- **Falta de bibliotecas**: Certifique-se de instalar todas as dependências listadas.

### Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests no repositório GitHub.

#### Observações

- O sistema pode ser ajustado para diferentes cenários modificando os parâmetros em config.py.
- Para melhorar a precisão do rastreamento, ajuste o filtro de Kalman e os limiares de distância e confiança.