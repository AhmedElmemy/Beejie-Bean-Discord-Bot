import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Ban(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    @client.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await ctx.send(f'{member.name} got banned for `{reason}`')
        await member.ban (reason=reason)

def setup(bot):
    bot.add_cog(Ban(bot))
