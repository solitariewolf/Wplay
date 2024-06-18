from discord.ext import commands
from pytube import YouTube
import os

class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='search', help='Baixa uma música do YouTube')
    async def search(self, ctx, *, search_terms):
        # A variável search_terms agora contém a URL fornecida pelo usuário
        url = search_terms

        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        download_path = stream.download(output_path='play')
        
        # Renomeia o arquivo para ter a extensão .mp3
        base, ext = os.path.splitext(download_path)
        new_file = base + '.mp3'
        os.rename(download_path, new_file)

        await ctx.send(f'Música baixada: {yt.title}')

async def setup(bot):
    await bot.add_cog(Search(bot))

