import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Staffhelp(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    @client.has_permissions(manage_messages=True)
    async def staffhelp(self, ctx):
        embed = discord.Embed(title="Staff members only commands help list.", color=0x12ba01)
        embed.add_field(name="b_clear (amount)", value="Use this to make me delete multiple messages at once, instead of deleting every single message on your own. Example: `b_clear 50` and it will delete 50 messages above the command.", inline=True)
        embed.add_field(name="b_warn @User (reason)", value="Use this command to warn a user if they missed any of the rules of the server. Example: `b_warn @member violating rule 8` or `b_warn 4742788532785 violating rule 7` and it will warn the selected user.", inline=True)
        embed.add_field(name="b_kick @User (reason)", value="Kicks the selected user from the server. Example: `b_kick @member being annoying` and the reason will be saved in the audit log", inline=True)
        embed.add_field(name="b_ban @User (reason)", value="Bans the selected user from the server. Example: `b_ban @member being aggressive` and the reason will be saved in the audit log", inline=True)
        embed.add_field(name="b_dm (user ID) (message)", value="Sends a message to selected user with bot Example: `b_dm 5716272819171616 Please be more respectful to other members... Thank you.` and the message will be sent", inline=True)

        embed.add_field(name="Notes:", value="These commands will work for the staff members only (Flayers) and it won\'t work with any other member so you must have the flayer role or higher in order to use these commands. To get a user's ID you must make sure you have the developer mode enabled from your setting on discord if you have it enabled than simply open a user\'s profile, scroll down, then click \"Copy ID\" you will need it to for a few commands like the DM and the Warn command but it's useful since it sends the user/member the message without pinging them and it can be used in the mod/admin chat so you should know about it")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Staffhelp(bot))
