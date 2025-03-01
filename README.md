# Detecção de Objetos em Tempo Real com YOLOv5

Este projeto implementa um sistema de detecção de objetos em tempo real utilizando a biblioteca YOLOv5 e Python. A aplicação captura vídeo da webcam e identifica objetos presentes na imagem, exibindo os resultados na tela.

## Funcionalidades

- Detecção de objetos em tempo real usando YOLOv5.
- Exibição dos objetos detectados com caixas delimitadoras e rótulos.
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
- `pandas`
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
    pip install opencv-python numpy torch torchvision pandas requests

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
    pip install opencv-python numpy torch torchvision pandas requests

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

### Problemas Conhecidos

- Aviso de depreciação: Se você encontrar um aviso sobre torch.cuda.amp.autocast, atualize o código conforme descrito na seção de solução de problemas.
- Falta de bibliotecas: Certifique-se de instalar todas as dependências listadas.

### Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests no repositório GitHub.