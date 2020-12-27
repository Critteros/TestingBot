#This file help initialize the bot

#Standard imports
import sys, os
from dotenv import load_dotenv



if (__name__ == "__main__"):
    print("ERROR: Bad entry point. Run startBot.py instead")
    sys.exit(1)
    
#Function to load env variables from .env and convert them to disctionary    
def loadParameters() -> dict:
    
    parameters = {
        "discordToken" : "",
        "bungieToken" : "",
        "prefix" : "",
        "cogs" : set()
    }

    #Loading env variables
    _loadEnv(parameters)
    
    #Load cogs into dict
    _loadCogs(parameters)
    
    print("INFO: Loading parameters complete")
    return parameters
    

#Internal Function to load Cogs into dictionary   
def _loadCogs(dict_: dict) -> None:
    
    #Get all files in Cogs directory
    os_files = os.listdir("./TestingBot/Cogs")
    
    #Format files
    for file in os_files:
        if file.endswith('.py'):
            dict_['cogs'].add(f"TestingBot.Cogs.{file[:-3]}")
    
#Internal Function to load Env variables    
def _loadEnv(dict_: dict) -> None:
    
    #Load env variables from .env file using library
    load_dotenv()
    
    #Loading Discord Token
    if os.environ.get('DISCORD_TOKEN') is not None:
        dict_["discordToken"] = os.getenv('DISCORD_TOKEN')
    else:
        print("CRITICAL: Discord Token does not exist, exitting")
        sys.exit(1)

    #Loading Bungie Token
    if os.environ.get('BUNGIE_TOKEN') is not None:
        dict_["bungieToken"] = os.getenv('BUNGIE_TOKEN')
    else:
        #Todo implement handling
        print("CRITICAL: BUNGIE Token does not exist")
    
    #Loading default bot prefix
    if os.environ.get('DEFAULT_PREFIX') is not None:
        dict_["prefix"] = os.getenv('DEFAULT_PREFIX')
    else:
        print("WARNING: Default token not specified defaulting to '?'")
        dict_["prefix"] = "?"