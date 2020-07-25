import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Hug(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def hug(self, ctx,member: discord.Member):
        hugs=['https://images-ext-1.discordapp.net/external/jl7M0u9JvcyLaPRZPZzX0r0qIuplweNAsf3zGx-CPvo/https/cdn.nekos.life/hug/hug_063.gif',
          'https://images-ext-2.discordapp.net/external/CWTblaLMsWiI08Ee4Lv-OORkkAUukXQm5XOQuJ0CJJw/https/cdn.nekos.life/hug/hug_067.gif',
          'https://images-ext-1.discordapp.net/external/dl08FYbwmly0s81Wn16P05F4x-2ZBe5qbbttsf8Qwp4/https/cdn.nekos.life/hug/hug_009.gif',
          'https://images-ext-1.discordapp.net/external/74SFDuvP30_dVfzovYj8sQanzBViM0Kuu_Km6NAGIjY/https/cdn.nekos.life/hug/hug_070.gif?width=448&height=395',
'https://cdn.discordapp.com/attachments/719970418303434913/720030092817858570/tenor_1.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/719970533197873162/Hy0KO_7DZ.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/719970591633047592/tenor.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/719970532740562954/B1D9J1tvZ.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/719970532165943346/BJ0sOOmDZ.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/719970531503505518/SyaAd_7vW.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720030093241614556/tenor_3.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720030093761839104/tenor_2.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720030094361624666/tenor_4.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720030095187640330/tenor_5.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720031351981736007/tenor_6.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720031352434458674/tenor_7.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720031498438443049/tenor_9.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720031497779675226/tenor_8.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720031623084507146/tenor_10.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720293365425504326/SknauOQwb.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720293364871725147/BysjuO7D-.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720293364607614996/HkzndOXvZ.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720293364200767528/BJx2l0ttW.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720293363495993354/BkotddXD-.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720293363202654258/H1ui__XDW.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720293362900533318/HJU2OdmwW.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720293362627772546/BkZngAYtb.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720293361906483270/r1kC_dQPW.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720292915967951372/ryg2dd7wW.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720292915347456050/BkFnJsnA-.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720292914755797222/Bk5haAocG.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720292914042765372/S1DyFuQD-.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720292913623597096/SJfEks3Rb.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720292912868622366/H1X6OOmPW.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720292912012722206/rJnKu_XwZ.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720292911648079892/Sy65_OQvZ.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720292911341764638/r1bAksn0W.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720292214210691092/Sk80wyhqz.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720292213384544256/B10Tfknqf.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720292212860256366/rJCigAYFZ.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720292212348420166/rkx1dJ25z.gif'
'https://cdn.discordapp.com/attachments/719970418303434913/720292211576537198/BJF5_uXvZ.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720292211211763722/rkIK_u7Pb.gif',
'https://cdn.discordapp.com/attachments/719970418303434913/720292210800853002/rJaog0FtZ.gif']
        embed=discord.Embed(
            description=f"{ctx.author.name} **hugged** {member.name}",
            colour=0x12ba01
  )

        embed.set_image(url=f"{random.choice(hugs)}")
    
        await ctx.send(
            embed=embed
        )

def setup(bot):
    bot.add_cog(Hug(bot))
