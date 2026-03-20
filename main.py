import discord
from discord.ext import commands
import os
from dotenv import load_dotenv  # Importamos a biblioteca

# Carrega as variáveis do arquivo .env (se ele existir)
load_dotenv()

# 1. Configuração de Permissões (Intents)
intents = discord.Intents.default()

# 2. Herança: Criamos nossa própria classe de Bot herdando do discord.py
class KodlandBotPro(commands.Bot):
    def __init__(self):
        # Inicializa a classe mãe com um prefixo padrão e nossas permissões
        super().__init__(command_prefix="!", intents=intents)

    # Este método é chamado automaticamente antes do bot se conectar
    async def setup_hook(self):
        print("⚙️ Carregando módulos (Cogs)...")
        # Carrega o nosso arquivo pokedex.py que está dentro da pasta cogs
        await self.load_extension("cogs.pokedex")
        
        # Sincroniza os comandos de barra (/) com os servidores do Discord
        await self.tree.sync()
        print("✅ Módulos carregados e comandos de barra sincronizados!")

    # Evento disparado quando o bot entra online com sucesso
    async def on_ready(self):
        print(f'🚀 Bot online e operando como: {self.user}')

# 3. Instanciamos o nosso objeto Bot
bot = KodlandBotPro()

# 4. Puxamos o Token do ambiente (Segurança em primeiro lugar!)
TOKEN = os.getenv('DISCORD_TOKEN')

if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("🚨 ERRO CRÍTICO: Token do Discord não encontrado!")
        print("Dica: Exporte a variável no bash usando: export DISCORD_TOKEN='seu_token'")
