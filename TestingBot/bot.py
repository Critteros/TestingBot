import discord
from discord.ext import commands


class BotClass(commands.Bot):
    def __init__(self, parameters:dict):
        super().__init__(
            command_prefix = '?'
        )

        self.__DiscordToken = parameters.get('discordToken')
        self.run(self.__DiscordToken)
        
        