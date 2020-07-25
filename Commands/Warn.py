import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Warn(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    @client.has_permissions(manage_messages=True)
    async def warn(self, ctx, member : discord.Member, *, reason=None):
        await ctx.send(f'{member.name} got warned')
        await member.send(f"You have been warned in Beejie Bean's server. Because `{reason}` please read the rules to avoid getting kicked/banned after violating the rules again.")

def setup(bot):
    bot.add_cog(Warn(bot))
