import traceback, sys, discord, chalk
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType

class CommandError(client.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.Cog.listener()
    async def on_command_error(self, ctx, error):

        if hasattr(ctx.command, 'on_error'):
            return

        error = getattr(error, 'original', error)

        if isinstance(error, client.DisabledCommand):
            print(f"{ctx.command} is disabled with the command deco")

        elif isinstance(error, client.CommandNotFound):
            return

        elif isinstance(error, client.MissingPermissions):
            await ctx.send("Better ask Larson to help with that one! `(you need admin perms to use this command)`")

        else:
            tra = traceback.format_exception_only(type(error), error)
            embed = discord.Embed(description=f"`Oh damn... looks like I dropped my lemon cake, hold up lemme try to get another one... if that issue continued to happen ping Ahmed` ```py\n%s\n``` \n" % ''.join(tra), file=sys.stderr, color=0xff0000)
            embed.set_author(name="That's an issue!",icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
            print(f"Warning! The command '{ctx.command}' has just Errored!")
            print(f"Traceback: %s" % ''.join(tra))



def setup(bot):
    bot.add_cog(CommandError(bot))
