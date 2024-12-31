# Projeto de Reconhecimento Facial

Este projeto realiza o reconhecimento de rostos em imagens utilizando a biblioteca `face_recognition` em conjunto com `OpenCV`. O objetivo é identificar personagens a partir de suas imagens e gerar uma imagem anotada com os rostos detectados e seus respectivos nomes.

## Funcionalidade

- O projeto carrega imagens de personagens conhecidos e gera codificações de rostos a partir dessas imagens.
- Ele então reconhece os rostos presentes em uma imagem de entrada e os compara com os rostos conhecidos.
- A imagem de entrada é anotada com caixas delimitadoras e os nomes dos personagens reconhecidos.
- O sistema também conta quantos rostos foram reconhecidos e quantos foram classificados como "Desconhecidos".

## Requisitos

Certifique-se de que o Python está instalado no seu ambiente. Este projeto depende das seguintes bibliotecas:

- `face_recognition`: Para reconhecimento facial.
- `face_recognition_models`: Modelos pré-treinados para reconhecimento facial.
- `opencv-python`: Para manipulação de imagens.
- `numpy`: Para manipulação de arrays.

### Instalando as Dependências

Se você ainda não tem as dependências instaladas, pode instalar todas as bibliotecas necessárias com o seguinte comando:

```bash
pip install -r requirements.txt
```

## Estrutura do Projeto

```
/seu-projeto
│
├── assets
│   └── images
│       ├── personagem1.jpg
│       ├── personagem2.jpg
│       └── ... (imagens dos personagens)
│
├── input
│   └── image.jpg  # Imagem para reconhecimento
│
├── output
│   └── recognized_faces_out.jpg  # Imagem de saída com as anotações
│
├── requirements.txt  # Dependências do projeto
└── recognition.py  # Código principal do projeto
```

## Como Usar

1. **Preparar Imagens dos Personagens**:
   Coloque as imagens dos personagens conhecidos na pasta `assets/images`. O nome de cada imagem deve corresponder ao nome do personagem (sem a 
   extensão). Exemplo: `Harry.jpg`, `Ron.jpg`, etc.

2. **Adicionar Imagem de Entrada**:
   Coloque a imagem onde você deseja realizar o reconhecimento na pasta `input` (por exemplo, `elenco.jpg`).

3. **Executar o Script**:
   Execute o script Python para realizar o reconhecimento de rostos:

   ```bash
   python recognition.py
   ```

   O script irá processar a imagem de entrada e gerar uma imagem de saída com as caixas delimitadoras e os nomes dos rostos detectados. A imagem anotada será salva na pasta `output` como `recognized_faces_out.jpg`.

4. **Estatísticas**:
   O script também exibirá as seguintes estatísticas no terminal:
    - Quantos rostos foram reconhecidos.
    - Quantos rostos foram classificados como "Desconhecidos".

### Exemplo de Saída

Ao executar o script, você verá uma saída como:

```bash
Rostos reconhecidos: 4
Rostos desconhecidos: 2
Imagem anotada salva em: output/recognized_faces_out.jpg
```

Isso significa que 4 rostos foram reconhecidos como personagens conhecidos e 2 rostos foram classificados como desconhecidos.


## Contribuições

Este é um projeto de código aberto! Fique à vontade para contribuir, corrigir bugs ou melhorar a funcionalidade. Se você deseja contribuir, crie um fork do repositório, faça suas alterações e envie um pull request.
