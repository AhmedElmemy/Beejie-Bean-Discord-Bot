import asyncio, discord, flask, importlib, logging, os, random, re, traceback, webserver

import discord.ext.commands as client

from webserver import keep_alive

class BeejieBot(client.Bot):

    def __init__(self):

        super().__init__(command_prefix = ["b_","B_"], status = discord.Status.idle, activity = discord.Game(name = "Starting up..."))
        for file in os.listdir("Commands"):

            if file.endswith(".py"):
                name = file[:-3]
                try:

                    module = importlib.import_module(f"Commands.{name}")
                    self.load_extension(f"Commands.{name}")
                    print(f"Loaded command {name}")

                except(discord.ClientException, ModuleNotFoundError):

                    print(f"[X] Failed to load command {name}!")
                    print(traceback.format_exc())
        
        for file in os.listdir("Events"):

            if file.endswith(".py"):
                name = file[:-3]
                try:

                    module = importlib.import_module(f"Events.{name}")
                    self.load_extension(f"Events.{name}")
                    print(f"Loaded event {name}")

                except(discord.ClientException, ModuleNotFoundError):

                    print(f"[X] Failed to load event {name}!")
                    print(traceback.format_exc())

bot = BeejieBot()

keep_alive()
bot.run("")
