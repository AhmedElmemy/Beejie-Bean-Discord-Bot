import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Test(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def test(self, ctx):
        await ctx.send(f"Working perfectly fine. <:Beejie:612618277650432001>")

def setup(bot):
    bot.add_cog(Test(bot))
