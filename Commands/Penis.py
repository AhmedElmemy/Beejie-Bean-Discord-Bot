import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Psize(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def psize(self, ctx):
        responses = [
            "8D",
            "8=D", 
            "8==D",
            "8===D", 
            "8====D",
            "8=====D", 
            "8======D", 
            "8=======D", 
            "8========D", 
            "8=========D",
            "8==========D",
            "8===========D",
            "8============D",
            "8=============D", 
            "8==============D",
            "8===============D", 
            "8================D"
        ]
        await ctx.send(f"{random.choice(responses)}")

def setup(bot):
    bot.add_cog(Psize(bot))
