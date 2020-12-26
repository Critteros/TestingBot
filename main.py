import discord
import os
from discord.ext import commands
from TestingBot.bot import BotClass
import logging as log
import sys
import coloredlogs
import asyncio


#Conteiner for the Bot instance
Bot = None

#Main function and entry point for the bot
def main() -> None:
    
    logger = log.getLogger('discord')
    #handler = log.StreamHandler(sys.stdout)
    #handler.setFormatter(log.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    
    coloredlogs.install(fmt="%(asctime)s:%(levelname)s:%(name)s: %(message)s",level="DEBUG", logger=logger)
    #logger.setLevel(log.DEBUG)
    #logger.addHandler(handler)
    
    #Initialize Bot
    initBot()
    
    #Run async loop
    Bot.run()

#Function that initializes Bot global variable
def initBot() -> None:
    
    #List that will initialize Bot
    parameters = {} 
    
    #Referencing Bot to global variable
    global Bot
    
    #Initializing list of cogs
    parameters['cogs'] = set()
    
    #Listing all the cogs files 
    os_files = os.listdir("./TestingBot/Cogs")
    
    #Formatting cog files
    for file in os_files:
        if file.endswith('.py'):
            parameters['cogs'].add(f"TestingBot.Cogs.{file[:-3]}")
    del os_files

    
    #Setting parameters
    parameters['discordToken'] = os.getenv('DISCORD_TOKEN')
    
    #Initializing Global BOT variable
    Bot = BotClass(parameters) 




if (__name__ == '__main__'):
    print("Starting main process")
    main()
    

