# Guia Passo a Passo: Extrator de Seguidores do Instagram

Este guia foi criado para quem nunca usou um terminal ou programação. Siga as instruções específicas para o seu sistema operacional.

---

## 💻 1. Instalação do Python (O "Motor")

O programa precisa do Python para rodar. Escolha o seu sistema:

### **Windows**
1. Acesse: [python.org/downloads](https://www.python.org/downloads/)
2. Clique no botão **Download Python**.
3. Abra o arquivo baixado.
4. **MUITO IMPORTANTE:** Marque a caixa **"Add Python to PATH"** antes de clicar em "Install Now".
5. Siga até o final.

### **Mac (macOS)**
1. Acesse: [python.org/downloads](https://www.python.org/downloads/)
2. Clique no botão **Download Python**.
3. Abra o arquivo `.pkg` e instale normalmente.
4. Após instalar, abra o buscador (Spotlight) e digite "Certificates". Clique em **"Install Certificates.command"** que está na pasta do Python (isso evita erros de conexão).

### **Linux (Ubuntu/Debian)**
1. Abra o seu terminal.
2. Digite: `sudo apt update && sudo apt install python3 python3-pip`

---

## 📂 2. Preparando os Arquivos

1. Baixe o projeto e extraia-o em uma pasta fácil de achar (ex: na sua Área de Trabalho).
2. O nome da pasta deve ser algo como `instagram-scraper`.

---

## ⌨️ 3. Abrindo o Terminal na Pasta do Projeto

### **Windows**
1. Abra a pasta do projeto no Explorador de Arquivos.
2. Clique na barra de endereço (onde fica o caminho da pasta) no topo da janela.
3. Apague tudo, digite `cmd` e aperte **Enter**.

### **Mac (macOS)**
1. Abra a pasta do projeto no Finder.
2. Clique com o botão direito na pasta (ou dentro dela).
3. Selecione **"Novo Terminal na Pasta"** (New Terminal at Folder).
   *Dica: Se não aparecer, vá em Ajustes do Sistema > Teclado > Atalhos > Serviços > Habilite "Novo Terminal na Pasta".*

### **Linux**
1. Abra a pasta do projeto.
2. Clique com o botão direito em um espaço vazio e selecione **"Abrir no Terminal"**.

---

## 🚀 4. Instalando e Rodando

Agora, com a janela preta (terminal) aberta na pasta correta, digite estes comandos um por um:

**Passo A: Instalar os complementos**
```bash
pip install -r requirements.txt
```
*(No Mac/Linux, se o comando acima falhar, tente: `pip3 install -r requirements.txt`)*

**Passo B: Ligar o programa**
```bash
python app.py
```
*(No Mac/Linux, se falhar, tente: `python3 app.py`)*

---

## 🌐 5. Usando a Ferramenta

1. **NÃO FECHE** a janela do terminal enquanto estiver usando.
2. Abra o seu navegador (Chrome, Safari, etc.).
3. Digite este endereço: `http://localhost:5000`
4. Você verá a interface do programa.

### **Como Extrair:**
1. **Login:** Entre com seu usuário e senha do Instagram.
2. **Perfil Alvo:** Digite o @ do perfil que você segue e quer baixar os seguidores.
3. **Paciência:** O programa é lento de propósito (15-30 segundos por pessoa) para o Instagram não bloquear sua conta. Deixe rodando ao fundo.
4. **Download:** Quando terminar (ou se você clicar em "Parar e Salvar"), clique no botão **Baixar CSV** para abrir os dados no Excel.

---

## ⚠️ Dicas de Segurança e Erros

- **2FA (Autenticação):** Se sua conta pede código por SMS/App, fique de olho na janela do terminal na primeira vez. Ele pode pedir para você digitar o código lá.
- **Sessão:** O programa salva um arquivo chamado `session.json`. Não delete ele, pois ele evita que você precise logar de novo, o que é mais seguro.
- **Erro de Conexão (Mac):** Se der erro de SSL, certifique-se de que executou o arquivo "Install Certificates.command" mencionado no Passo 1.
