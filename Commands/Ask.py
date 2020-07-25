import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Ask(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def ask(self, ctx):
        Responses = [
            "Of course!",
            "Yes yes!",
            "Beejie aprooves!",
            "No...",
            "Bad! Bad! Bad!",
            "Beejie doesn't agree..",
            "I have no idea.",
            "Not now.. I'm too drunk.",
            "Gay.",
            "Nah man"
        ]
        await ctx.send(f'{random.choice(Responses)}')

def setup(bot):
    bot.add_cog(Ask(bot))
