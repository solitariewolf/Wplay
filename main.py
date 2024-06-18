# Arquivo: main.py
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém o token do bot do arquivo .env
TOKEN = os.getenv('DISCORD_TOKEN')

# Define os intents
intents = discord.Intents.default()
intents.messages = True  # Habilita o intent para mensagens
intents.guilds = True  # Habilita o intent para servidores/guildas
intents.message_content = True  # Habilita o intent para conteúdo de mensagens

# Cria uma instância do bot com os intents definidos e um prefixo de comando
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    # Carrega a extensão com os comandos de voz dentro do evento on_ready
    await bot.load_extension('commands.connect')
    await bot.load_extension('commands.play')
    await bot.load_extension('commands.search')

# Inicia o bot com o token
bot.run(TOKEN)
