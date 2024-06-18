from discord.ext import commands
import discord
import os
import asyncio

class Play(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.current_song = None

    @commands.command(name='play', help='Reproduz um arquivo de música')
    async def play(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                channel = ctx.author.voice.channel
                await channel.connect()
            else:
                await ctx.send("Você precisa estar em um canal de voz para usar este comando.")
                return
        
        songs = [song for song in os.listdir('play') if song.endswith('.mp3')]
        
        for song in songs:
            source = discord.FFmpegPCMAudio(os.path.join('play', song))
            ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
            await ctx.send(f"Reproduzindo: {song}")
            
            # Aguarda a música atual terminar antes de passar para a próxima
            while ctx.voice_client.is_playing():
                await asyncio.sleep(1)
            
            # Após a música terminar, deleta o arquivo
            os.remove(os.path.join('play', song))

async def setup(bot):
    await bot.add_cog(Play(bot))
