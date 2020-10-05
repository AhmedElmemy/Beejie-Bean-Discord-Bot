import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Slap(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def slap(self, ctx,member: discord.Member):
        slaps=[
"https://cdn.discordapp.com/attachments/700820356755095572/743782510164443176/tenor_6.gif",
"https://cdn.discordapp.com/attachments/700820356755095572/743782359379214386/tenor_5.gif",
"https://cdn.discordapp.com/attachments/700820356755095572/743782358989275266/tenor_7.gif",
"https://cdn.discordapp.com/attachments/700820356755095572/743782358620176424/tenor_8.gif",
"https://cdn.discordapp.com/attachments/700820356755095572/743782358305734716/tenor_9.gif"
]
        embed=discord.Embed(
            description=f"{ctx.author.name} **slapped** {member.name}",
            colour=0x12ba01
  )

        embed.set_image(url=f"{random.choice(slaps)}")
    
        await ctx.send(
            embed=embed
        )

def setup(bot):
    bot.add_cog(Slap(bot))
