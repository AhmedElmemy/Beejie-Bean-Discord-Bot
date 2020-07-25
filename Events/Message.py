import discord, re
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Message(client.Cog):
	def __init__(self, bot):

		self.bot = bot

	@client.Cog.listener()
	async def on_message(self, message):

		if re.search(r"^b_", message.content) or message.author.bot:

			return

		if re.search(r"(^|[^A-Za-z])Dr[aiu]nk(s|ing)?([^A-Za-z]|$)",
		             message.content, re.IGNORECASE):

			await message.channel.send("<:Notnowtoodrunk:682511932829466634>")

		if re.search(r"(Nick)", message.content, re.IGNORECASE):

			await message.channel.send("NICK IS SEXY AS FUCKKKK.")

		if re.search(r"(Mario)", message.content, re.IGNORECASE):

			await message.channel.send("Mario is gay.")

		if re.search(r"(Lemon cake)", message.content, re.IGNORECASE):

			await message.channel.send("<:LemonCake:612163813655183380>")

def setup(bot):
	bot.add_cog(Message(bot))
