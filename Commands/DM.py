import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Dm(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command(aliases=["DM"])
    @client.cooldown(1, 2, BucketType.user)
    @client.has_permissions(manage_messages=True)
    async def dm(self, ctx,user:discord.User,*,reason):
        await user.send(reason)
        await ctx.send(f'Message got dilivered.')

def setup(bot):
    bot.add_cog(Dm(bot))
