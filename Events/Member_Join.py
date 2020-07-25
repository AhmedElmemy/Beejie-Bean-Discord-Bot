import discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType

class Ready(client.Cog):

    def __init__(self, bot):

        self.bot = bot

    @client.Cog.listener()
    async def on_member_join(self, member):
    
        print(f'{member} has joined the server')
        channel=self.bot.get_channel(271888640936902656)
        await channel.send(f"Welcome {member.mention} to Beejie Bean's Lemon Cake Fest we hope you enjoy your stay here with us but make sure to check on the <#389308367614771201> and remember to stay moist 💦")

def setup(bot):
    bot.add_cog(Ready(bot))
