#This file is the main wrapper around logger module that provides to bot logging capability

#Standard imports
import sys, os

#Logging libraries
import logging, coloredlogs

#Check running script
if (__name__ == "__main__"):
    print("ERROR: Bad entry point. Run startBot.py instead")
    sys.exit(1)

class BotLog:
   
    #Class variables to be used
    _consoleLogger = None
    _internalLogger = None
    
    @classmethod
    def init(cls,*, level = logging.DEBUG):
        cls._consoleLogger = logging.getLogger("TestingBot")
        
        #Getting hook to stdout stream
        Stout = sys.stdout
        
        #Formatted logger output
        fmt = "%(asctime)s | %(name)s[%(process)d] %(levelname)s: %(message)s"
        
        #Filed styles
        field_style = {
            'asctime': {'color': 'white'},
            'hostname': {'color': 'magenta'},
            'levelname': {'bold': True, 'color': 'black'},
            'name': {'color': 214},
            'process' : {'color': 90},
            'programname': {'color': 'cyan'},
            'username': {'color': 'yellow'}
        }
        
        #Level styles
        level_style = {
            'debug': {'color': 'black', 'bright': True},
            'info': {},
            'warning': {'color': 'yellow'},
            'error': {'color': 'red'},
            'critical': {'bold': True, 'color': 16, 'background': 'red'},
            
            'notice': {'color': 'magenta'},
            'spam': {'color': 'green', 'faint': True},
            'success': {'bold': True, 'color': 'green'},
            'verbose': {'color': 'blue'}
            
        }    
        
        #Installing Colored Logger
        coloredlogs.install(
            level = level,
            fmt = fmt,
            level_styles = level_style,
            field_styles = field_style,
            logger = cls._consoleLogger,
            stream = Stout
        )
        cls._consoleLogger.debug("Finieshed intialization of Logger")
        cls._consoleLogger.debug("Example debug")
        cls._consoleLogger.info("Example info")
        cls._consoleLogger.warning("Example warning")
        cls._consoleLogger.error("Example error")
        cls._consoleLogger.critical("Example critical")
        
     
    
    #ConsoleLogger getter
    @classmethod
    def getConsoleLogger(cls):
        return cls._consoleLogger
    

#Run code upon import  
if (__name__ == "TestingBot.Log"):
   #Initialize Loggers
   BotLog.init()

    