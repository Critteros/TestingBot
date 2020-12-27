# This file is the main wrapper around logger module that provides to bot logging capability
# Setting of the logger rely on set enviroment variables
# CLIENT_LOGGER
#     CONSOLE /This will set the logger to use the coloredlogs library and print colored logs to STDOUT
#     NORMAL  /This will set the logger to use the logging module and write output to STDOUT
#     FILE    /This will set the logger to use the logging module and write output to a file
#           Default is NORMAL
#
# LOG_LEVEL
#   DEBUG /Sets log level to debug
#   INFO /Sets log level to info
#   WARNING /Sets log level to warning
#   ERROR /Sets log level to error
#   CRITICAL /Sets log level to critical
#
# LOG_INTERNAL
#   if set to TRUE  this setting enviroment variable will enable discord.py library to log to a file

# Standard imports
import sys
import os

# Logging libraries
import logging
import coloredlogs

# Check running script
if (__name__ == "__main__"):
    print("ERROR: Bad entry point. Run startBot.py instead")
    sys.exit(1)


class BotLog:

    #Prevent instance creation of this class
    def __new__(cls, *args, **kwargs):
        print("FATAL: Creating instances of main bot class is not supported")
        raise RuntimeError("BotLog instance creation: forbidden")
    
    # Class variables to be used
    _clientLogger = None
    _internalLogger = None

        
    #To test logger functionality
    @classmethod
    def logExamples(cls):
        cls._clientLogger.debug("Example debug")
        cls._clientLogger.info("Example info")
        cls._clientLogger.warning("Example warning")
        cls._clientLogger.error("Example error")
        cls._clientLogger.critical("Example critical")
    
    #ConsoleLogger getter
    @classmethod
    def getConsoleLogger(cls):
        return cls._clientLogger

####################################################################################################
#                       LOGGER BYPASSES
####################################################################################################
    @classmethod
    def debug(cls,*args, **kwargs):
        cls._clientLogger.debug(*args, **kwargs)
        
    @classmethod
    def info(cls,*args, **kwargs):
        cls._clientLogger.info(*args, **kwargs)
        
    @classmethod
    def warning(cls,*args, **kwargs):
        cls._clientLogger.warning(*args, **kwargs)
        
    @classmethod
    def error(cls,*args, **kwargs):
        cls._clientLogger.error(*args, **kwargs)
        
    @classmethod
    def critical(cls,*args, **kwargs):
        cls._clientLogger.critical(*args, **kwargs)
    
####################################################################################################

    #Inner init method, do not use it
    @classmethod
    def _init(cls, *, level = None):
        
        #Defaults
        LEVEL_VALUES = {
            "DEBUG": logging.DEBUG,
            "INFO" : logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR" : logging.ERROR,
            "CRITICAL": logging.CRITICAL
        }
        
        CLIENT_VALUES = {
            "CONSOLE",
            "NORMAL",
            "FILE"
        }
        
        #Read env variables
        level = level or os.environ.get('LOG_LEVEL', 'WARNING')
        client_type = os.environ.get('CLIENT_LOGGER', 'NORMAL')
        
        #Handle internal env
        tmp = os.getenv('LOG_INTERNAL')
        if ( (tmp is not None) and (tmp == "TRUE")):
            initInternal = True
        else:
            initInternal = False
        del tmp
        
        #User input handling
        level = level if (level in LEVEL_VALUES) else "WARNING"
        client_type = client_type if (client_type in CLIENT_VALUES) else "NORMAL"
        
        #Set level to a int variable
        level = LEVEL_VALUES[level]
        
        if client_type == "CONSOLE":
            cls._initConsoleLogger(level=level)
        elif client_type == "NORMAL":
            cls._initNormalLogger(level=level)
        elif client_type == "FILE":
            cls._initFileLogger(level=level)
        else:
            cls._initNormalLogger(level=level)
            
        if initInternal:
            cls._initInternalLogger(level=level)
            
####################################################################################################

    #Inner function to init Console Logger
    @classmethod
    def _initConsoleLogger(cls, *, level=logging.DEBUG):
        cls._clientLogger = logging.getLogger("TestingBot")

        # Getting hook to stdout stream
        Stout = sys.stdout

        # Formatted logger output
        fmt = "%(asctime)s | %(name)s[%(process)d] %(levelname)s: %(message)s"

        # Filed styles
        field_style = {
            'asctime': {'color': 'white'},
            'hostname': {'color': 'magenta'},
            'levelname': {'bold': True, 'color': 'black'},

            'name': {'color': 214},
            'process': {'color': 90},
            'programname': {'color': 'cyan'},
            'username': {'color': 'yellow'}
        }

        # Level styles
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

        # Installing Colored Logger
        coloredlogs.install(
            level=level,
            fmt=fmt,
            level_styles=level_style,
            field_styles=field_style,
            logger=cls._clientLogger,
            stream=Stout
        )

####################################################################################################    

    #Inner function to init File Logger
    @classmethod
    def _initFileLogger(cls,*,level=logging.DEBUG):
        cls._clientLogger = logging.getLogger("TestingBot")
        cls._clientLogger.setLevel(level)

        # Formatted logger output
        fmt = "%(asctime)s | %(name)s[%(process)d] %(levelname)s: %(message)s"
        
        #Create STDOUT handler
        handler = logging.FileHandler("client.log")
        handler.setLevel(level)
        
        #Create formatter
        formater = logging.Formatter(fmt = fmt, datefmt='%Y-%m-%d %H:%M:%S')
        
        #Attach formater
        handler.setFormatter(formater)
        
        #Attach handler
        cls._clientLogger.addHandler(handler)

####################################################################################################

    #Inner function to init Normal logger    
    @classmethod
    def _initNormalLogger(cls,*,level=logging.DEBUG):
        cls._clientLogger = logging.getLogger("TestingBot")
        cls._clientLogger.setLevel(level)
        
        # Getting hook to stdout stream
        Stout = sys.stdout

        # Formatted logger output
        fmt = "%(asctime)s | %(name)s[%(process)d] %(levelname)s: %(message)s"
        
        #Create STDOUT handler
        handler = logging.StreamHandler(Stout)
        handler.setLevel(level)
        
        #Create formatter
        formater = logging.Formatter(fmt = fmt, datefmt='%Y-%m-%d %H:%M:%S')
        
        #Attach formater
        handler.setFormatter(formater)
        
        #Attach handler
        cls._clientLogger.addHandler(handler)
      
####################################################################################################    
    
    #Inner funtion to init Internal logger  
    @classmethod
    def _initInternalLogger(cls,*,level=logging.DEBUG):
        cls._internalLogger = logging.getLogger("discord")

        # Formatted logger output
        fmt = "%(asctime)s | %(name)s[%(process)d] %(levelname)s: %(message)s"
        
        #Create STDOUT handler
        handler = logging.FileHandler("internal-discord.log")
        handler.setLevel(level)
        
        #Create formatter
        formater = logging.Formatter(fmt = fmt, datefmt='%Y-%m-%d %H:%M:%S')
        
        #Attach formater
        handler.setFormatter(formater)
        
        #Attach handler
        cls._internalLogger.addHandler(handler)

####################################################################################################

# Run code upon import
if (__name__ != "__main__"):
    # Initialize Loggers
    BotLog._init()
    BotLog.debug("Finished initializing BotLogger class")
