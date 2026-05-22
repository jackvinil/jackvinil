# Guia Passo a Passo: Como usar o Extrator de Seguidores

Este guia foi feito para quem nunca usou um terminal ou programação. Siga cada passo com calma.

---

### Passo 1: Instalar o "Motor" (Python)
Para o programa funcionar, seu computador precisa do **Python**.

1. Acesse: [python.org](https://www.python.org/downloads/)
2. Clique no botão amarelo **Download Python**.
3. Ao abrir o instalador, **MUITO IMPORTANTE:** Marque a caixinha que diz **"Add Python to PATH"** (Adicionar Python ao PATH) antes de clicar em "Install Now".
4. Siga a instalação até o fim.

---

### Passo 2: Preparar os arquivos
1. Baixe os arquivos deste projeto (se você recebeu um arquivo .zip, extraia-o em uma pasta, por exemplo, na sua "Área de Trabalho").
2. Abra a pasta onde os arquivos estão (você verá arquivos como `app.py`, `scraper.py`, etc.).

---

### Passo 3: Abrir o "Terminal" na pasta certa
O terminal é aquela janelinha preta onde digitamos comandos.

**No Windows:**
1. Abra a pasta do projeto no Explorador de Arquivos.
2. Clique na barra de endereço lá no topo (onde aparece o caminho da pasta).
3. Apague tudo o que estiver escrito, digite `cmd` e aperte **Enter**.
4. Uma janela preta vai abrir exatamente na pasta do projeto.

---

### Passo 4: Instalar os complementos
Agora, vamos dizer ao Python tudo o que ele precisa baixar para rodar o programa.
Na janela preta, digite o seguinte comando e aperte **Enter**:

```bash
pip install -r requirements.txt
```

*Aguarde alguns minutos. Muitas letras vão aparecer, isso é normal. Quando parar de aparecer coisas e a linha de comando voltar, está pronto.*

---

### Passo 5: Iniciar o Programa
Ainda na janela preta, digite:

```bash
python app.py
```

*Se aparecer uma mensagem dizendo que o servidor está rodando em `http://127.0.0.1:5000`, parabéns! O programa está funcionando.*

---

### Passo 6: Usar a ferramenta no seu Navegador
1. Não feche a janela preta! Deixe ela aberta.
2. Abra o seu navegador (Chrome, Edge, etc.).
3. Na barra de endereços, digite: `http://localhost:5000` e aperte **Enter**.
4. Você verá a tela do programa.

---

### Dicas de Uso Importantes:

1. **Login:** Use o seu usuário e senha do Instagram. O programa salva uma "sessão", então ele não vai pedir login toda hora (isso protege sua conta).
2. **O Código de Verificação:** Se o seu Instagram tiver autenticação em dois fatores, pode aparecer um aviso na janela preta pedindo o código. Fique de olho nela na primeira vez que entrar.
3. **Paciência é Segurança:** O programa processa cada usuário devagar (cerca de 2 usuários por minuto). Isso é proposital para o Instagram não perceber que é um robô e não bloquear sua conta.
4. **Pausar e Continuar:** Se precisar desligar o computador, clique em **Pausar** e depois em **Parar e Salvar**. Quando você abrir o programa de novo para o mesmo perfil, ele vai saber de onde parou.
5. **Onde fica o arquivo final?** Assim que terminar, clique em **Baixar CSV**. O arquivo será aberto no Excel com todas as informações.

---

### Problemas Comuns:
- **"Comando python não encontrado":** Você provavelmente esqueceu de marcar a caixa "Add Python to PATH" no Passo 1. Desinstale o Python e instale novamente com a caixa marcada.
- **Janela fechou sozinha:** Se a janela preta fechar, o programa para. Você precisa repetir o **Passo 5** para ligar ele de novo.
