#This file contains the main class of the bot

#Standard imports
import discord, os ,sys
from discord.ext import commands

if (__name__ == "__main__"):
    print("ERROR: Bad entry point. Run startBot.py instead")
    sys.exit(1)
    
class TestingBot:
    
    #Prevent instance creation of this class
    def __new__(cls, *args, **kwargs):
        print("FATAL: Creating instances of main bot class is not supported")
        raise RuntimeError("TestingBot instance creation: forbidden")
    
    @classmethod
    def initialize(cls, *, parameters: dict):
        cls._bot = commands.Bot(command_prefix= parameters["prefix"])
        cls._discordToken = parameters["discordToken"]
        
        #Loading cogs
        for cog_ in parameters["cogs"]:
            cls._bot.load_extension(cog_)
            
    @classmethod
    def getClient(cls):
        return cls._bot
    
    @classmethod
    def run(cls):
        cls._bot.run(cls._discordToken)