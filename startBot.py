#This file is the entry point for the bot and root of all python scripts

#Standard imports
import discord, sys, asyncio
from discord.ext import commands

#Helpers
from TestingBot.start_helper import loadParameters

#Logger module
import TestingBot.Log


#Main bot class import (must be the last import otherwise it will create name conflict)
from TestingBot.TestingBot import TestingBot

if (__name__ != "__main__"):
    print("ERROR: Bad entry point. Run startBot.py instead")
    sys.exit(1)
else:
    print("INFO: Starting up..")
    
    print("DEBUG: Preparing to load parameters")
    parameters = loadParameters()
    
    #Initializing bot 
    TestingBot.initialize(parameters = parameters)
    
    #Run main loop
    #TestingBot.run()
    
    
    
    