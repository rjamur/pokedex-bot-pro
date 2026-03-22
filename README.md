# 🤖 Pokedex Bot - Projeto Python Pro

🔗 **Repositório Oficial no GitHub:** [Acesse o código-fonte aqui](https://github.com/rjamur/pokedex-bot-pro)

## 🎯 Objetivo Pedagógico
O intuito deste bot é retirar o aluno do ambiente estrito do terminal e demonstrar a aplicação do Python no mundo real, cobrindo os seguintes pilares da programação avançada:

1. **Programação Orientada a Objetos (POO):** O projeto utiliza classes, métodos construtores (`__init__`) e Herança (`commands.Cog` e `commands.Bot`) para estruturar o código de forma modular e profissional.

2. **Consumo de APIs e JSON:** Demonstra na   prática como fazer requisições web (HTTP GET), interpretar a resposta em formato JSON e manipular dicionários aninhados nativos do Python.

3. **Assincronismo:** Utiliza `async/await` e a biblioteca `aiohttp` para garantir que o consumo da API não bloqueie a thread principal do bot, introduzindo conceitos de concorrência.

4. **Segurança e Boas Práticas:** Implementa o uso de variáveis de ambiente (`.env`) para proteção de credenciais sensíveis.

## 🛠️ Tecnologias Utilizadas

* Python 3.12+
* `discord.py` (Interação com a API do Discord)
* `aiohttp` (Requisições HTTP assíncronas)
* `python-dotenv` (Gerenciamento de variáveis de ambiente)
* Docker (Containerização e Deploy)

---

## ⚙️ Guia de Configuração: Portal do Discord

Para rodar este projeto, você precisará criar uma "identidade" para o bot no Discord e adicioná-lo ao seu servidor de testes. O painel do Discord é em inglês, então siga os passos com atenção:

### Passo 1: Criando o Aplicativo e Pegando o Token

1. Acesse o [Discord Developer Portal](https://discord.com/developers/applications) e faça login.

2. No canto superior direito, clique no botão azul **"New Application" (Nova Aplicação)**, dê um nome ao seu bot e clique em **"Create" (Criar)**.

3. No menu lateral esquerdo, vá na aba **"Bot" (Robô)** e clique no botão **"Reset Token" (Redefinir Token)**.

4. Copie o Token gerado. **Atenção:** Mantenha este Token em absoluto segredo. Ele é a chave mestre do seu código.

### Passo 2: Liberando as Permissões (Intents)

Ainda na página **"Bot"**, role para baixo até a seção **"Privileged Gateway Intents" (Intenções Privilegiadas do Gateway)** e ative estas três chaves:

* **Presence Intent** (Intenção de Presença - *Permite ver quem está online*)

* **Server Members Intent** (Intenção de Membros do Servidor - *Permite ver a lista de usuários*)

* **Message Content Intent** (Intenção de Conteúdo da Mensagem - *Permite que o bot leia o que é digitado no chat*)

* *Finalize clicando no botão verde **"Save Changes" (Salvar Alterações)** no rodapé.*

### Passo 3: Adicionando ao seu Servidor

1. No menu lateral esquerdo, vá em **"OAuth2"** -> **"URL Generator" (Gerador de URL)**.

2. No quadro **"Scopes" (Escopos)**, marque as caixas `bot` e `applications.commands` (necessário para os comandos com a barra `/`).

3. No quadro **"Bot Permissions" (Permissões do Bot)** que aparecerá logo abaixo, marque:
   * `Send Messages` (Enviar Mensagens)
   * `Embed Links` (Inserir Links - *Vital para renderizar o card colorido da Pokédex*).

4. Role até o final da página, copie a URL gerada, cole em uma nova aba do seu navegador e autorize o bot no seu servidor.

---

## 🚀 Como Executar Localmente no Windows

Você pode rodar o projeto de duas formas: usando o ambiente Python padrão (via Prompt de Comando/PowerShell) ou via Docker.

### Opção A: Via Terminal (Ambiente Virtual)

1. **Abra o terminal (CMD ou PowerShell) na pasta do projeto e crie o ambiente virtual:**
   ```bash
   python -m venv venv

2. Ative o ambiente virtual:
   ```bash
   venv\Scripts\activate

3. Instale as dependências:
   pip install -r requirements.txt

4. Configure o Token (Variáveis de Ambiente):
   ```bash
   copy .env.example .env
   
   Importante: Abra o novo arquivo .env gerado (no VSCode ou Bloco de Notas) e substitua o texto de exemplo pelo seu Token real do Discord copiado no Passo 1.
   
5. Rode o bot:
   ```bash
   python main.py

### Opção B: Via Docker Compose (Recomendado para Deploy)

Utilizar o Docker Compose é a forma mais moderna e prática de rodar o bot, pois ele gerencia a construção e a execução do container automaticamente.

1. **Configuração:** Certifique-se de ter criado e configurado o arquivo `.env` com o seu token no passo anterior.
2. **Subir o bot:** No terminal, na raiz do projeto, execute o comando abaixo para construir a imagem e rodar o bot em segundo plano (detached mode):
   ```bash
   docker compose up -d --build
3. Acompanhar os logs: Para garantir que o bot está online e ver as mensagens em tempo real:
   ```bash
   docker compose logs -f
4. Parar o bot: Quando precisar desligar o container, basta rodar:
   ```bash
   docker compose down

☁️ Sugestão de Deploy (Custo Zero)
Para manter o bot online 24/7 sem custos de hospedagem, a imagem Docker gerada neste projeto pode ser facilmente implantada em instâncias gratuitas (Always Free) de serviços de cloud, como a máquina virtual e2-micro do Google Cloud Compute Engine.
