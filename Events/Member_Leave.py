import discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType

class Ready(client.Cog):

    def __init__(self, bot):

        self.bot = bot

    @client.Cog.listener()
    async def on_member_remove(self, member):
    
        print(f'{member} has left the server')
        channel=self.bot.get_channel(731461766411845652)
        await channel.send(f"{member.name} just left the server.")

def setup(bot):
    bot.add_cog(Ready(bot))
