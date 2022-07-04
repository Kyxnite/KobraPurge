import os
from typing import T
os.system('cls')
from logging import critical
import requests
from colorama import init, Fore as fore
from discord.ext import commands
import colorama
import configparser
import logging
import discord
colorama.init()



w = fore.WHITE
alreadystarted = False
b = fore.BLUE
lb = fore.LIGHTBLUE_EX
eagle = requests.get("https://raw.githubusercontent.com/StvnedEagle1337/Stuff/main/Discord.txt").text.replace("\n",'')
config = configparser.ConfigParser()
config.read('Settings.INI')
token = config['settings']['token']  
delay = config['config']['delay']  
logmsgs = config['config']['logdeletedmessages']  
showmessages = config['config']['showmessagecontent']  
debug = config['misc']['debugmode']  
if debug == "True":
    debugmode = logging.DEBUG
else:
    debugmode = logging.WARNING
logging.basicConfig(
    level=debugmode,
    format= lb + "[" + w + "%(asctime)s\033[38;5;89m" + lb + "]" + w + " | %(message)s",
    datefmt="%H:%M:%S",
)
f = open("LoggedMessages.txt","w",encoding="utf-8")
mydiscord = requests.get("https://raw.githubusercontent.com/StvnedEagle1337/Stuff/main/Discord.txt").text
Eagle = discord.Client()
Eagle = commands.Bot(description='KottaWare | Premium', command_prefix=".", self_bot=True)



@Eagle.command()
async def clear(egirl):
        async for mss in egirl.channel.history(limit=None):
            if (mss.author.id == Eagle.user.id):
                critical(mss)
                try:
                   await mss.delete()  
                except:
                    pass


@Eagle.event
async def on_ready():
    critical("Connected to " + Eagle.user.name + "#" + Eagle.user.discriminator)
          

try:      
    Eagle.run(token, bot=False)
except:
    logging.critical("Something Failed... Starting Troubleshooter")