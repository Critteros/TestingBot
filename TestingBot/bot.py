import discord
from discord.ext import commands



class BotClass(commands.Bot):
    
    def __init__(self, parameters:dict):
        
        #Initializing comamnds.Bot constructor
        super().__init__(
            command_prefix = '?'
        )

        #Retriving discord Token from parameters
        self.__DiscordToken = parameters.get('discordToken')

        #Load cogs
        for cog_ in parameters.get('cogs'):
            self.load_extension(cog_)
        

        
    def run(self) -> None:
        super().run(self.__DiscordToken)
        