import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Ping(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def ping(self, ctx):
        await ctx.send(f'Pong! 🏓  `{round(self.bot.latency * 1000)}ms`')

def setup(bot):
    bot.add_cog(Ping(bot))
