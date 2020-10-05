import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Kiss(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def kiss(self, ctx,member: discord.Member):
        kisses=[
          "https://cdn.discordapp.com/attachments/700820356755095572/743785032174534696/tenor_13.gif",
          "https://cdn.discordapp.com/attachments/700820356755095572/743785030660259931/tenor_14.gif",
          "https://cdn.discordapp.com/attachments/700820356755095572/743784598915514419/tenor_10.gif",
          "https://cdn.discordapp.com/attachments/700820356755095572/743784598495821844/tenor_11.gif",
          "https://cdn.discordapp.com/attachments/700820356755095572/743784598177185882/tenor_12.gif"
               ]
        embed=discord.Embed(
            description=f"{ctx.author.name} **kissed** {member.name}",
            colour=0x12ba01
  )

        embed.set_image(url=f"{random.choice(kisses)}")
    
        await ctx.send(
            embed=embed
        )

def setup(bot):
    bot.add_cog(Kiss(bot))
