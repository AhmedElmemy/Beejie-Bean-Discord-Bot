import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Kick(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    @client.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await ctx.send(f'{member.name} got kicked for `{reason}`')
        await member.kick (reason=reason)

def setup(bot):
    bot.add_cog(Kick(bot))
