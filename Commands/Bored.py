import discord, random, aiohttp
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType
from discord import Embed

class Bored(client.Cog):

    def __init__(self, bot):
         self.bot = bot
         self.session = aiohttp.ClientSession()

    @client.command(name="bored", aliases=["whattodo", "nothingtodo"], usage="")
    @client.cooldown(1, 2, BucketType.user)
    async def bored(self, ctx):
        msg = await ctx.send("So... you're bored and you have nothing to do. Maybe there'll be something for you.")
        async with self.session.get("http://www.boredapi.com/api/activity/") as resp:
            data = await resp.json()
        embed = Embed(color=0x12ba01)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Found something!", value=data["activity"])
        await msg.edit(embed=embed)

def setup(bot):
    bot.add_cog(Bored(bot))
