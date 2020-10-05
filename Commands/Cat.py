import discord, random, aiohttp
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType
from discord import Embed

class Cat(client.Cog):

    def __init__(self, bot):
         self.bot = bot
         self.session = aiohttp.ClientSession()

    @client.command(usage="")
    @client.cooldown(1, 2, BucketType.user)
    async def cat(self, ctx):
        msg = await ctx.send("🐱")
        async with self.session.get("https://some-random-api.ml/img/cat") as resp:
            data = await resp.json()
        embed = Embed(color=0x12ba01)
        embed.set_image(url=data["link"])
        await msg.edit(embed=embed)

def setup(bot):
    bot.add_cog(Cat(bot))
