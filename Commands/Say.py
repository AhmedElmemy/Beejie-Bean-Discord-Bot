import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Say(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    @client.has_permissions(manage_messages=True)
    async def say(self, ctx, *, arg):
      channel = self.bot.get_channel(271888640936902656)
      
      if arg:
        await channel.send(arg)
        await ctx.message.add_reaction("✅")
        print(ctx)
      else:
        await ctx.send("Baka! say something!")

def setup(bot):
    bot.add_cog(Say(bot))
