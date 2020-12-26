import discord
import os
from discord.ext import commands
from TestingBot.bot import BotClass

parameters = {}
parameters['discordToken'] = os.getenv('DISCORD_TOKEN')
Bot = BotClass(parameters)