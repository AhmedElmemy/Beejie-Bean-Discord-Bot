import discord, re
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Message(client.Cog):
    def __init__(self, bot):

        self.bot = bot

    @client.Cog.listener()
    async def on_message(self, message):
        
        if re.search(r"(Nigga|Nigger|Faggot|Shemale|Tranny|Vomit|N1gga)", message.content, re.IGNORECASE):
            await message.delete()
            censor = discord.Embed(
                title = '**You have been warned**',
                description = 'Avoid using this type of language or you\'ll be banned',
                colour = 0xff0000 )

            censor.set_footer(text=f"Please don't use this kind of offensive language!")
            await message.channel.send(embed=censor) 

def setup(bot):
    bot.add_cog(Message(bot))
