import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Avatar(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def avatar(self, ctx, *, member:discord.Member=None):
	      author = ctx.author.name
	      author_avatar = ctx.author.avatar_url
	      if member == None:

		        AuthorAvatar = discord.Embed(
		            title = f"{author}'s avatar", 
		            colour = 0x12ba01
		        )
		        AuthorAvatar.set_image(url=author_avatar)
		        await ctx.send(embed=AuthorAvatar)

	      else:

		        member_name = member.name
		        member_avatar = member.avatar_url
		        MemberAvatar = discord.Embed(
		            title = f"{member_name}'s avatar", 
		            colour = 0x12ba01
		        )
		        MemberAvatar.set_image(url=member_avatar)
		        await ctx.send(embed=MemberAvatar)

def setup(bot):
    bot.add_cog(Avatar(bot))
