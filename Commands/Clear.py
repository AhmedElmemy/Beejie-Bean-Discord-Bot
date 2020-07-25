import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Clear(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    @client.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=100):
        await ctx.channel.purge(limit=amount)

def setup(bot):
    bot.add_cog(Clear(bot))
