import discord
from discord.ext import commands
from discord import app_commands
import aiohttp

# 1. Herança: Transformamos essa classe em um módulo (Cog) do Discord
class PokedexCog(commands.Cog):
    
    # 2. O famoso método construtor para inicializar a classe
    def __init__(self, bot):
        self.bot = bot

    # 3. Decorator (HOF) que transforma a função em um comando de barra (/)
    @app_commands.command(name="pokemon", description="Busca informações de um Pokémon na PokéAPI")
    async def buscar_pokemon(self, interaction: discord.Interaction, nome: str):
        
        # Log na atividade do usuário (útil para monitoramento e debugging)
        print(f"🔎 Log: Usuário {interaction.user} buscou pelo Pokémon: {nome}")

        # Diz para o Discord: "Espera um pouquinho que estou buscando os dados!"
        # Isso evita que o comando dê erro de timeout se a API demorar a responder.
        await interaction.response.defer()

        # Formatamos a URL (a PokéAPI exige que o nome seja minúsculo)
        url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
        
        # 4. Consumo Assíncrono da API (O grande diferencial do nível Pro)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                
                # Se o status for 200 (OK), achamos o Pokémon!
                if response.status == 200:
                    # O await aqui transforma o JSON da web em um Dicionário Python
                    dados = await response.json()
                    
                    # 5. Tratamento de Dados (Acessando chaves do Dicionário)
                    peso_kg = dados['weight'] / 10 
                    altura_m = dados['height'] / 10
                    imagem_url = dados['sprites']['front_default']
                    
                    # 6. Montando a interface visual bonita (Embed)
                    embed = discord.Embed(
                        title=f"🔎 Pokédex: {nome.capitalize()}",
                        color=discord.Color.red()
                    )
                    embed.set_thumbnail(url=imagem_url)
                    embed.add_field(name="Altura", value=f"{altura_m}m", inline=True)
                    embed.add_field(name="Peso", value=f"{peso_kg}kg", inline=True)
                    embed.set_footer(text="Dados fornecidos pela PokéAPI")
                    
                    # Envia o card montado de volta para o chat
                    await interaction.followup.send(embed=embed)
                
                # Se a API retornar erro 404 (Not Found)
                else:
                    await interaction.followup.send(f"❌ Poxa, não encontrei nenhum Pokémon chamado '{nome}'.")

# 7. Função essencial para o Discord carregar este arquivo
async def setup(bot):
    await bot.add_cog(PokedexCog(bot))
