# Arquivo: commands/connect.py
from discord.ext import commands

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='connect', help='Conecta ao canal de voz do usuário')
    async def connect(self, ctx):
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("Você precisa estar em um canal de voz para usar este comando.")

    @commands.command(name='disconnect', help='Desconecta do canal de voz')
    async def disconnect(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("Desconectado do canal de voz.")
        else:
            await ctx.send("O bot não está conectado a um canal de voz.")

async def setup(bot):
    await bot.add_cog(Voice(bot))

