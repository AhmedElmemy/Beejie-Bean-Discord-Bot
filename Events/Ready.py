import asyncio, discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType

class Ready(client.Cog):

    def __init__(self, bot):

        self.bot = bot

    @client.Cog.listener()
    async def on_ready(self):
    
        await self.bot.change_presence(
            status=discord.Status.online
        )
        print("Bot is Online")
        self.bot.loop.create_task(self.status_task())

    async def status_task(self):
        while not self.bot.is_closed():
            games = [
              
                "on Larson's grave",
                "Doki Doki Literature Club",
                "while flaying", "Toaru Majutsu No Index MMO", "with flaying knifes", "Minecraft", "Anime", "Type b_help for the commands list", "Left 4 Dead 2",
                "with Celty",
                "Mr burns is gay",
                "I said ride on",
                "Do people even read these?",
                "with Ryanna",
                "Mikoto is best girl fite me",
                "Penisfart",
                "Penisfart?",
                "🇵 🇪 🇳 🇮 🇸 🇫 🇦 🇷 🇹"
            ]
            for game in games:
                await self.bot.change_presence(activity=discord.Game(game))
                await asyncio.sleep(900)

def setup(bot):
    bot.add_cog(Ready(bot))
