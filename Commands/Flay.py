import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Flay(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def flay(self, ctx, *, arg1=None):
        
        if arg1 is None:

            await ctx.send("Who do you want me to flay? 🗡️ ")

        elif arg1 == "me" or arg1 == "Me" or arg1 == "mE" or arg1 == "ME":

            await ctx.send("With pleasure 🗡️")

        elif arg1 == "<@271920728675319808>":

            await ctx.send("Why would you want to delete the guy who gave you the ability to use me? Shame on you!")

        elif arg1 == "<@576691800081825802>":

            await ctx.send("Don't even think about touching babygurl.")
   
        elif arg1 == "<@271892913049305089>":

            await ctx.send("In your dreams.")

        elif arg1 == "<@240715859218268161>":

            await ctx.send("Do you really think I would let you flay the best boy?")

        elif arg1 == f"<@666380503515004990>" or arg1 == "Beejie":

            await ctx.send("Nice try.")
            
        elif arg1 == f"@everyone":

            await ctx.send("Try harder than that.")
        
            
        else:
          
            await ctx.send(f'{arg1} got flayed :dagger:')
            self.arg = arg1

def setup(bot):
    bot.add_cog(Flay(bot))
