# 💧 Hidro Monitor - Sistema de Monitoramento Hídrico

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Colorama](https://img.shields.io/badge/Library-Colorama-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge)
![License](https://img.shields.io/badge/Licen%C3%A7a-MIT-green?style=for-the-badge)

<p align="center">
  <b>Simulador de monitoramento de nível de reservatório via CLI, com alertas coloridos e feedback dinâmico.</b>
</p>

</div>

---

## 📌 Sobre o Projeto

O **Hidro Monitor** é uma aplicação desenvolvida em Python que é executada diretamente no terminal (CLI). Seu objetivo é simular a leitura de um sensor de nível hídrico, representando o nível de um reservatório.

O sistema classifica o nível em cinco estados operacionais e utiliza a biblioteca `colorama` para apresentar alertas visuais por meio de uma escala de cores intuitiva.

---

## 🚀 Funcionalidades

- 🎨 **Alertas visuais em cores:** identificação de cada estado do reservatório com cores específicas: vermelho, amarelo, verde, ciano e azul.
- ⏳ **Simulação de processamento em tempo real:** utilização do módulo `time` e da função `sleep()` para simular o intervalo entre as leituras do sensor.
- 🎲 **Geração aleatória de níveis:** utilização da função `randint()` para simular variações no nível do reservatório.
- 🔁 **Controle de leitura contínua:** interface interativa com laços `while`, permitindo realizar múltiplas medições sem reiniciar o programa.
- 🛡️ **Formatação do terminal:** restauração das configurações de estilo após a exibição dos alertas, utilizando os recursos da biblioteca `colorama`.

---

## 📊 Níveis do Reservatório

| Nível | Situação | Cor do alerta | Estado operacional |
|:---:|---|:---:|---|
| **1** | Muito baixo (crítico) | 🔴 Vermelho | Risco de desabastecimento |
| **2** | Baixo | 🟡 Amarelo | Atenção recomendada |
| **3** | Médio | 🟢 Verde | Operação normal |
| **4** | Alto | 🩵 Ciano | Volume elevado |
| **5** | Muito alto (alerta) | 🔵  Azul | Risco de transbordamento |

---

## 🛠️ Tecnologias Utilizadas

- **[Python 3](https://www.python.org/):** linguagem de programação utilizada no desenvolvimento do projeto.
- **[Colorama](https://pypi.org/project/colorama/):** biblioteca utilizada para aplicar cores e estilos ao texto exibido no terminal.
- **[Time](https://docs.python.org/3/library/time.html):** módulo nativo do Python utilizado para controlar intervalos de execução com a função `sleep()`.

---

## 🔧 Como Executar o Programa

Siga os passos abaixo para executar o **Hidro Monitor** em sua máquina.

### 1. Pré-requisitos

Certifique-se de ter o Python 3.8 ou superior instalado.

Para verificar a versão instalada, abra o terminal e execute:

```bash
python --version
```

Em alguns sistemas Linux, pode ser necessário utilizar:

```bash
python3 --version
```

### 2. Instalação das Dependências

O programa utiliza a biblioteca externa `colorama` para exibir cores no terminal.

Instale-a com o seguinte comando:

```bash
pip install colorama
```

Se necessário, no Linux, utilize:

```bash
python3 -m pip install colorama
```

### 3. Criar o Arquivo do Programa

Crie um arquivo chamado `main.py` na pasta de sua preferência e cole nele o código-fonte do programa.

### 4. Executar o Sistema

Abra o terminal, navegue até a pasta onde o arquivo `main.py` foi salvo e execute:

```bash
python main.py
```

No Linux, caso o comando anterior não funcione, utilize:

```bash
python3 main.py
```

Após a inicialização, o cabeçalho do Hidro Monitor será exibido no terminal. Você poderá interagir com o sistema digitando **S** para iniciar as leituras do reservatório ou **N** para encerrar, conforme as opções implementadas no programa.

