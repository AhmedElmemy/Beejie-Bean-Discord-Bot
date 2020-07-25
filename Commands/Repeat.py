import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Repeat(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    @client.has_permissions(manage_messages=True)
    async def repeat(self, ctx, *, arg):
        if arg:
            await ctx.delete()
            await ctx.send(arg)
            print(ctx)
        else:
            await ctx.send("Baka! say something!")

def setup(bot):
    bot.add_cog(Repeat(bot))
