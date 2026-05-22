# Instagram Follower Scraper

Este projeto é uma ferramenta web para extrair informações detalhadas de seguidores de qualquer perfil do Instagram que você siga.

## Funcionalidades
- Interface web intuitiva.
- Login seguro com salvamento de sessão (evita logins repetidos).
- Coleta de 37 campos detalhados (Email, Telefone, Endereço, Biografia, etc).
- Sistema de Pausa e Retomada (salva o progresso automaticamente).
- Exportação direta para CSV.
- Protocolos de segurança com delays aleatórios para evitar bloqueios.

## Como usar

Se você não tem experiência com programação, por favor leia o nosso **[Guia para Iniciantes (INSTRUCOES.md)](INSTRUCOES.md)**.

Para usuários avançados:
1. **Instale as dependências:** `pip install -r requirements.txt`
2. **Inicie o programa:** `python app.py`
3. **Acesse a interface:** `http://localhost:5000`

## Notas de Segurança
- O script utiliza pausas de 15 a 30 segundos por usuário para imitar o comportamento humano.
- Evite extrair milhares de usuários em um único dia.
- O primeiro login pode exigir um código de verificação no seu aplicativo do Instagram.
