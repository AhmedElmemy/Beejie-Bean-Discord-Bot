import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Face(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 3, client.BucketType.user)
    async def face(self, ctx):
        responses = ['On']

        pics = [
            "https://cdn.discordapp.com/attachments/666566254601175080/688072306719064064/eJwVylEOxBAUQNG9WACPx0M3I6KinbQlmK_J7H3M773nw979Yhs75mxjE2I_R6p952PWHkvmpdZy5djOwVO9RZwzpuPOzxxCWemc.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688072307356598312/15230718_692085537638722_8094816833197621376_n.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688072307830292480/vlcsnap-2016-11-14-20h54m13s112_-_Copy.png", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688072308203585590/d.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688072308727742520/eyJ1cmwiOiJodHRwczovL2Rpc2NvcmQuc3RvcmFnZS5nb29nbGVhcGlzLmNvbS9hdHRhY2htZW50cy8yNzE4ODg2NDA5MzY5MDI2.png", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688072309021606056/2018-04-12_04.31.39.png", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688072478807162937/20200313_191155.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688072479251628032/20200313_185607.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688072480270581916/20200313_185543.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688072480883081216/20200313_185149.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688072481403437129/image.png", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073063698661441/ghv.JPG", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073063945732108/fgsg.png", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073064352972900/hgrtvfd.JPG", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073064675541027/image0-5.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073064973729928/20171103_010707.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073065841557549/received_217581235663892.gif", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073066252730420/Screenshot_20190623-131136_YouTube.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073066697457669/Screenshot_2018-07-14-06-16-02-1.png", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073271371104291/4rfed.JPG", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073271710974014/SFDSDCDSSCXDX.png", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073272859951117/ftyvg.JPG", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073273283706886/sessfsdfsd_2.png", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073273941950542/weds.gif", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073274852507653/tenor.gif", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073381785894996/20190902_213253.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073382134153303/Screenshot_20190901-152437_Twitter.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073382650052630/20190907_232234.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073383132659752/1490602422_giphy_1.gif", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073383833108552/20190901_014331.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073384143355904/Screenshot_20191127-193322_Gallery.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073384416116736/5t4ergf.JPG", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073688863735847/5t4erfdcx.JPG", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073689043828747/mandarin-500x500.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073689207537712/DjSi4urXsAA31nA_jpg_large.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073689434292264/Satentana.png", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073690197393421/4tref.JPG", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073754533953571/3w2r4efsdcx.JPG", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073754751926310/y56hgrt.JPG", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073754969899043/0105CCD819709FDFB40F8C04369F39925B1A54CE.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073755381334024/56ythgfb.JPG", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073755645444133/20200126_031712.jpg",
    "https://cdn.discordapp.com/attachments/666566254601175080/688073756056354908/5df795d7143cfa87ec582c5d32tzgjl202306044826_s.png", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073914290536484/6uyrhtg.JPG", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073914546520100/FB_IMG_1581172793017.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073917298245726/20191221_152033.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073917755031607/JPEG_20170828_000007.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073918334107870/20190913_021844.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073918581702743/5t6uyhgn.JPG", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073946708443141/IMG_20200224_043132.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073947501428760/vlcsnap-2020-02-27-13h43m11s728_-_Copy.png", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073947878653965/FB_IMG_1558447134372.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/688073948084437054/3rweds.PNG", 
    "https://cdn.discordapp.com/attachments/666566254601175080/689513476875616280/20200317_110013.jpg", 
    "https://cdn.discordapp.com/attachments/666566254601175080/691304443135918140/image-1.png", 
    "https://cdn.discordapp.com/attachments/666566254601175080/691304443504754798/eJwVzMENwyAMAMBdGABTp4DJNoggghRihN1X1d3bfu9xb_Nal9nNqTplBzi6FF6HFeWVW7WNuV01zy628ICsmss56q0CGB9EFJ4u.png"
        ]

        channel = ctx.message.channel
        ree = discord.Embed(
            colour = 0x12ba01
        )

        ree.set_image(url='{0}'.format(random.choice(pics)))
        await ctx.send(embed=ree)

def setup(bot):
    bot.add_cog(Face(bot))
