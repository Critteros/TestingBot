#This file is the entry point for the bot and root of all python scripts

#Load .env
from dotenv import load_dotenv
load_dotenv()


#Standard imports
import discord, sys, asyncio, os
from discord.ext import commands

#Helpers
from TestingBot.start_helper import loadParameters


#Logger module
from TestingBot.Log import BotLog


#Main bot class import (must be the last import otherwise it will create name conflict)
from TestingBot.bot import TestingBot


if (__name__ != "__main__"):
    print("ERROR: Bad entry point. Run startBot.py instead")
    sys.exit(1)
else:
    
    BotLog.info("Starting up..")
   

    BotLog.debug("Preparing to load parameters")
    parameters = loadParameters()
    
    #Initializing bot 
    BotLog.debug("Initializing Bot")
    TestingBot.initialize(parameters = parameters)
    
    #Run main loop
    BotLog.info("Running main event loop")
    TestingBot.run()
    
    
    
    