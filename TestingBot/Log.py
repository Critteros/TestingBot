# This file is the main wrapper around logger module that provides to bot logging capability
# Setting of the logger rely on set enviroment variables
# CLIENT_LOGGER
#     CONSOLE /This will set the logger to use the coloredlogs library and print colored logs to STDOUT
#     NORMAL  /This will set the logger to use the logging module and write output to STDOUT
#     FILE    /This will set the logger to use the logging module and write output to a file
#
#LOG_LEVEL
#   DEBUG /Sets log level to debug
#   INFO /Sets log level to info
#   WARNING /Sets log level to warning
#   ERROR /Sets log level to error
#   CRITICAL /Sets log level to critical
#
# LOG_INTERNAL
#   setting this enviroment variable will enable discord.py library to log to a file

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

    # Class variables to be used
    _clientLogger = None
    _internalLogger = None

    @classmethod
    def init(cls, *, level=logging.DEBUG):
        cls._initConsoleLogger(level=level)
        cls._initInternalLogger(level=level)
        
        #Testing only
        cls._clientLogger.debug("Example debug")
        cls._clientLogger.info("Example info")
        cls._clientLogger.warning("Example warning")
        cls._clientLogger.debug("Finieshed intialization of Logger")
        cls._clientLogger.error("Example error")
        cls._clientLogger.critical("Example critical")

    # ConsoleLogger getter
    @classmethod
    def getConsoleLogger(cls):
        return cls._clientLogger

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
    
    @classmethod
    def _initFileLogger(cls,*,level=logging.DEBUG):
        cls._clientLogger = logging.getLogger("TestingBot")

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
        
    @classmethod
    def _initNormalLogger(cls,*,level=logging.DEBUG):
        cls._clientLogger = logging.getLogger("TestingBot")
        
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


# Run code upon import
if (__name__ == "TestingBot.Log"):
    # Initialize Loggers
    BotLog.init()
