import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Pat(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command(aliases=["headpat"])
    @client.cooldown(1, 2, BucketType.user)
    async def pat(self, ctx,member: discord.Member):
        pats=[
"https://cdn.weeb.sh/images/B1D9J1tvZ.gif",
"https://cdn.weeb.sh/images/r12R1kYPZ.gif",
"https://cdn.weeb.sh/images/rkTC896_f.gif",
"https://cdn.weeb.sh/images/S1ja11KD-.gif",
"https://cdn.weeb.sh/images/rJavp1KVM.gif",
"https://cdn.weeb.sh/images/BkaRWA4CZ.gif",
"https://cdn.weeb.sh/images/rkSN7g91M.gif",
"https://i.some-random-api.ml/UCCywoQmQs.gif",
"https://cdn.weeb.sh/images/rkBZkRttW.gif",
"https://cdn.weeb.sh/images/ByOc1ktv-.gif",
"https://cdn.weeb.sh/images/B1SOzCV0W.gif",
"https://cdn.weeb.sh/images/H1jnJktPb.gif",
"http://i.imgur.com/fvgSWgw.gif",
"https://cdn.weeb.sh/images/HyG2kJKD-.gif",
"https://cdn.weeb.sh/images/rJ1WlyKPZ.gif",
"https://cdn.weeb.sh/images/B1PnJJYP-.gif",
"https://cdn.weeb.sh/images/B1TQcTNCZ.gif",
"https://cdn.weeb.sh/images/HyxG31ktDb.gif",
"https://cdn.weeb.sh/images/r1Y5L6NCZ.gif",
"https://cdn.weeb.sh/images/H1s5hx0Bf.gif",
"https://cdn.weeb.sh/images/H1Vc1yYwW.gif",
"https://cdn.weeb.sh/images/H1jgekFwZ.gif",
"https://cdn.weeb.sh/images/ry1tlj2AW.gif",
"https://cdn.weeb.sh/images/Hkccqp4A-.gif",
"https://cdn.weeb.sh/images/ryXj1JKDb.gif",
"https://cdn.weeb.sh/images/BJp1lyYD-.gif",
"https://cdn.weeb.sh/images/ryV2k1tP-.gif",
"https://cdn.weeb.sh/images/rJMskkFvb.gif",
"https://cdn.weeb.sh/images/SJva1kFv-.gif",
"https://cdn.weeb.sh/images/rkADh0sqM.gif",
"https://cdn.weeb.sh/images/HyqTkyFvb.gif",
"https://cdn.weeb.sh/images/rybs1yFDb.gif",
"https://cdn.weeb.sh/images/SkVNXac-G.gif",
"https://cdn.weeb.sh/images/SktIxo20b.gif",
"https://cdn.weeb.sh/images/BJnD9a4Rb.gif",
"https://cdn.weeb.sh/images/rktsca40-.gif",
"https://cdn.weeb.sh/images/Sky1x1YwW.gif",
"https://i.some-random-api.ml/eT58KYZl8I.gif",
"https://i.some-random-api.ml/H4fkA0ZwLz.gif",
"https://cdn.weeb.sh/images/ryh6x04Rb.gif",
"https://cdn.weeb.sh/images/rkSN7g91M.gif",
"https://cdn.weeb.sh/images/rytzGAE0W.gif",
"https://cdn.weeb.sh/images/rktgg1Yv-.gif",
"https://cdn.weeb.sh/images/HkZqkyFvZ.gif",
"https://cdn.weeb.sh/images/SkksgsnCW.gif",
"https://cdn.weeb.sh/images/r1goyytPZ.gif",
"https://cdn.weeb.sh/images/ryLKqTVCW.gif",
"https://cdn.weeb.sh/images/SJmW1RKtb.gif",
"https://cdn.weeb.sh/images/Bk4Ry1KD-.gif",
"https://cdn.weeb.sh/images/HJGQlJYwb.gif",
"https://cdn.weeb.sh/images/Sk2FyQHpZ.gif",
"https://cdn.weeb.sh/images/Sk2f7J39G.gif",
"https://cdn.discordapp.com/attachments/584048511553634321/721335063362666536/r1AsJ1twZ.gif"
]
        embed=discord.Embed(
            description=f"{ctx.author.name} **pats** {member.name}",
            colour=0x12ba01
  )

        embed.set_image(url=f"{random.choice(pats)}")
    
        await ctx.send(
            embed=embed
        )

def setup(bot):
    bot.add_cog(Pat(bot))
