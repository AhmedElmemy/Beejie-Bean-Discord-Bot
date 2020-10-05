import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Punch(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def punch(self, ctx,member: discord.Member):
        punches=[
"https://cdn.discordapp.com/attachments/468559236113235981/737328468592951346/tenor_1.gif",
"https://cdn.discordapp.com/attachments/601772394679500826/737327059327516732/tenor.gif",
"https://cdn.discordapp.com/attachments/601772394679500826/737327249468162118/tenor_3.gif",
"https://cdn.discordapp.com/attachments/601772394679500826/737327250118148297/tenor_4.gif"
]
        embed=discord.Embed(
            description=f"{ctx.author.name} **punched** {member.name}",
            colour=0x12ba01
  )

        embed.set_image(url=f"{random.choice(punches)}")
    
        await ctx.send(
            embed=embed
        )

def setup(bot):
    bot.add_cog(Punch(bot))
