import discord, random, time
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Userinfo(client.Cog):

    def __init__(self, bot):
         self.bot = bot


    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def userinfo(self, ctx, member: discord.Member = None):
      
      if member is None:
        sender = ctx.author

      else:
          sender = member
          embed = discord.Embed(title=f"{sender.name}'s User Information", color=0x12ba01)
          embed.add_field(name="User ID", value=f"{sender.id}", inline=False)
          embed.add_field(name="User Name", value=f"{sender.name}", inline=True)
          embed.add_field(name="Discriminator", value=f"{sender.discriminator}", inline=True)
          embed.add_field(name="User Status", value=f"{sender.status}", inline=True)
          embed.add_field(name="Highest Role", value=f"{sender.top_role}", inline=False)
          embed.set_thumbnail(url=sender.avatar_url)
          embed.add_field(name="Server nickname:",value=member.display_name)
          embed.add_field(name="Created at:",value=member.created_at.strftime("%a,%d %B %Y,%I:%M,UTC"))
          embed.add_field(name="Joined the server at:",value=member.joined_at.strftime("%a,%d %B %Y,%I:%M,UTC"))
          
          await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Userinfo(bot))
