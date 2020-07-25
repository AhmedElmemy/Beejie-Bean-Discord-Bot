import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Help(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def help(self, ctx):
        embed = discord.Embed(title="Hello there! I'm Beejie the bot", description="Ahmed, ~~messed around~~ coded with python script until he finally made something outta his free time, if you have any kind of suggestions for the bot simply ask Ahmed or Beejie Bean.", color=0x12ba01)
        embed.add_field(name="b_ask", value="Ask me a yes or no question.", inline=True)
        embed.add_field(name="b_flay", value="Does anyone on the server is being a bitch? And you need someone to flay him? Hold my lemon cake.", inline=True)
        embed.add_field(name="b_quote", value="Makes me say one of Beejie's popular quotes. ||Gay.||", inline=True)
        embed.add_field(name="b_avatar @Member", value="Sends the avatar of the selected user.", inline=True)
        embed.add_field(name="b_gay", value="Shows how gay are you. 😛", inline=True)
        embed.add_field(name="b_face", value="Sends a random face picture.", inline=True)
        embed.add_field(name="b_psize", value="Shows your Penis's size. 😜", inline=True)
        embed.add_field(name="b_hug @Member", value="Hugs the selected user.", inline=True)
        embed.add_field(name="b_headpat @Member", value="Gives the selected user a headpat.", inline=True)
        embed.add_field(name="b_ping", value="Checks the host server ping speed.", inline=True)
        embed.add_field(name="b_help", value="Shows this list", inline=True)
        embed.add_field(name="b_IQ", value="Shows your IQ. ||Baka brain smh.||", inline=True)
        embed.add_field(name="b_test", value="Checks if I'm working or not.", inline=True)
        
        
        
        
        embed.add_field(name="and that's it!", value="I'm sure there will be more commands added as soon as possible, so stay tuned until then. ||Beejie bot: Version 2.8||")
        embed.set_footer(text="Invite Your Friends To Beejie's!: https://discord.gg/uyy6D9T")
        await ctx.send(embed=embed)

def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Help(bot))
