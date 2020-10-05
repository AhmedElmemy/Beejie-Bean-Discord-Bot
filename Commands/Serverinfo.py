import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Serverinfo(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def serverinfo(self, ctx, id: int): 
        embed = discord.Embed(
            colour = 0x12ba01
        )
        guild = self.bot.get_guild(id)
        sender = ctx.author
        embed.set_author(name="• Server Info → " + str(guild.name))
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="—", value="→ The information about the server will be listed below!"
                                        "\n —")
        embed.add_field(name="• Server name: ", value=str(guild.name))
        embed.add_field(name="• Server region: ", value=guild.region)
        embed.add_field(name="• Server ID: ", value=str(guild.id))
        embed.add_field(name="• Server owner: ", value=guild.owner)
        embed.add_field(name="• Server owner ID: ", value=guild.owner_id)
        embed.add_field(name="• Member count: ", value=guild.member_count)
        embed.add_field(name="• Text channels count: ", value="22")
        embed.add_field(name="• Voice channels count: ", value="8")
        embed.add_field(name="• Server creation: ", value=guild.created_at)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Serverinfo(bot))
