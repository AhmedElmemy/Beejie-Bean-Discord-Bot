import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Quotes(client.Cog):
	def __init__(self, bot):
		self.bot = bot

	@client.command(pass_context=True, aliases=['quote'])
	@client.cooldown(1, 2, BucketType.user)
	async def quotes(self, ctx):
		responses = [
		    "NICK, IS SEXYYY AS FUCKKK!!!",
		    "PUT YOUR HEAD BETWEEN YOUR LEGS AND SNIFF",
		    "Just so everyone knows, if you nag me for Dark motherfucking Carnival i will flay you all alive and feed your rotting corpses to the hounds",
		    "🇵 🇪 🇳 🇮 🇸 🇫 🇦 🇷 🇹",
		    "I mean as long as we have our likes and hobbies we enjoy in life that keeps our minds distracted and allows us to escape reality there are ways to push through it some days",
		    "We all gay", "who isn't gay these days!", "I hate society",
		    "Sniff the wall",
		    "EVERYONE GET MCMOIST YOU SEXY MCWHORES AND SNIFF BETWEEN YOUR MCFUCKIN MCLEGS",
		    "Man people suck", "EVERYONE GET MOIST YOU SEXY WHORES",
		    "Larson ya gay cunt"
		]
		await ctx.send(f"{random.choice(responses)}")


def setup(bot):
	bot.add_cog(Quotes(bot))
