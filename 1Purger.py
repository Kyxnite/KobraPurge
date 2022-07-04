import os
from typing import Text
os.system('cls')
from discord.channel import DMChannel, GroupChannel, TextChannel
import subprocess, sys
from logging import critical
import requests
import threading
from requests import  post
from random import randint
from colorama import init, Fore as fore
from discord.ext import commands
import platform
import colorama
import asyncio
import configparser
import logging
import discord
colorama.init()
w = fore.WHITE
alreadystarted = False
b = fore.BLUE
lb = fore.LIGHTBLUE_EX
eagle = requests.get("https://raw.githubusercontent.com/StvnedEagle1337/Stuff/main/Discord.txt").text.replace("\n",'')
exposings = []
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
Eagle = commands.Bot(description='xD', command_prefix=".")

        
        
auth = requests.get("https://raw.githubusercontent.com/StvnedEagle1337/Stuff/main/Auth.txt").text
      

                                               
async def purgedm():
    theid = input(f"{fore.LIGHTBLUE_EX}{os.getlogin()}{w}@{fore.LIGHTBLUE_EX}{platform.node()} {fore.LIGHTGREEN_EX}~{fore.WHITE}$ {w}DM ID: {fore.WHITE}")
    amount = input(f"{fore.LIGHTBLUE_EX}{os.getlogin()}{w}@{fore.LIGHTBLUE_EX}{platform.node()} {fore.LIGHTGREEN_EX}~{fore.WHITE}$ {w}Amount(Leave Blank For Infinite): {fore.WHITE}")
    for channel in Eagle.private_channels:
     if isinstance(channel,GroupChannel):
         pass
     else:
     
    
        if channel.id == int(theid):
                if amount == "":
                    async for mss in channel.history(limit=None):
                        if (mss.author.id == Eagle.user.id):
                         if logmsgs == "True":
                            if mss.is_system() == True:
                                print(f"{lb}[{w}INFO{lb}] {w}| {lb}System Message Ignored")
                                return
                            else:
                                try:
                                 await mss.delete()    
                                 print(f"{lb}[{w}INFO{lb}] {w}| {lb}Deleted Message: {w}{mss.content}")
                                except:
                                    pass
                                 
                                
                    await mainmenu()
                else:
                    async for mss in channel.history(limit=int(amount)):
                        if (mss.author.id == Eagle.user.id):
                         if logmsgs == "True":
                            if mss.is_system() == True:
                                print(f"{lb}[{w}INFO{lb}] {w}| {lb}System Message Ignored")
                    
                                return
                            else:
                                print(f"{lb}[{w}INFO{lb}] {w}| {lb}Deleted Message: {w}{mss.content}")
                             
                            
                         if mss.is_system() == True:
                            print(f"{lb}[{w}INFO{lb}] {w}| {lb}System Message Ignored")
                            return
                         else:
                             if (mss.author.id == Eagle.user.id):
                              await mss.delete()      
                    await mainmenu()
    
                                                                               
async def purgegc():
    theid = input(f"{fore.LIGHTBLUE_EX}{os.getlogin()}{w}@{fore.LIGHTBLUE_EX}{platform.node()} {fore.LIGHTGREEN_EX}~{fore.WHITE}$ {w}GC ID: {fore.WHITE}")
    amount = input(f"{fore.LIGHTBLUE_EX}{os.getlogin()}{w}@{fore.LIGHTBLUE_EX}{platform.node()} {fore.LIGHTGREEN_EX}~{fore.WHITE}$ {w}Amount(Leave Blank For Infinite): {fore.WHITE}")
    for channel in Eagle.private_channels:

        if channel.id == int(theid):
            if isinstance(channel,GroupChannel):
                if amount == "":
                    async for mss in channel.history(limit=None):

                        if (mss.author.id == Eagle.user.id):

                         if showmessages == "True":
                            if mss.is_system() == True:
                                print(f"{lb}[{w}INFO{lb}] {w}| {lb}System Message Ignored")
                                
                            else:
                                try:

                                 if logmsgs == "True":
                                    f.write(mss.content + "\n")      
                                    await mss.delete() 
                                 else:
                                      await mss.delete()   
                                  
                                  
                                  
                                except:
                                    pass
                                print(f"{lb}[{w}INFO{lb}] {w}| {lb}Deleted Message: {w}{mss.content}")
                         else:
                            if mss.is_system() == True:
                                print(f"{lb}[{w}INFO{lb}] {w}| {lb}System Message Ignored")
                            
                            try:
                                await mss.delete()   
                                print(f"{lb}[{w}INFO{lb}] {w}| {lb}Deleted Message: {w}{mss.content}")
                                
                            except Exception as bh:
                                critical(bh)
                                pass
                            
                           
                           
                           
                                        
                else:
                    async for mss in channel.history(limit=int(amount)):
                        if (mss.author.id == Eagle.user.id):
                         if logmsgs == "True":
                            if mss.is_system() == True:
                                print(f"{lb}[{w}INFO{lb}] {w}| {lb}System Message Ignored")
                    
                                return
                            else:
                                print(f"{lb}[{w}INFO{lb}] {w}| {lb}Deleted Message: {w}{mss.content}")
                             
                            
                         if mss.is_system() == True:
                            print(f"{lb}[{w}INFO{lb}] {w}| {lb}System Message Ignored")
                            return
                         else:
                             if (mss.author.id == Eagle.user.id):
                              await mss.delete()      
    await mainmenu()
                                                                    
async def purgechannel():
    theid = input(f"{fore.LIGHTBLUE_EX}{os.getlogin()}{w}@{fore.LIGHTBLUE_EX}{platform.node()} {fore.LIGHTGREEN_EX}~{fore.WHITE}$ {w}Channel ID: {fore.WHITE}")
    amount = input(f"{fore.LIGHTBLUE_EX}{os.getlogin()}{w}@{fore.LIGHTBLUE_EX}{platform.node()} {fore.LIGHTGREEN_EX}~{fore.WHITE}$ {w}Amount(Leave Blank For Infinite): {fore.WHITE}")
    for guild in Eagle.guilds:
        for channel in guild.channels:
         if channel.id == int(theid):
            if isinstance(channel,TextChannel):
                if amount == "":
                    async for mss in channel.history(limit=None):
                        if (mss.author.id == Eagle.user.id):
                         if logmsgs == "True":
                            if mss.is_system() == True:
                                print(f"{lb}[{w}INFO{lb}] {w}| {lb}System Message Ignored")
                    
                                return
                            else:
                                if showmessages == "True":
                                    print(f"{lb}[{w}INFO{lb}] {w}| {lb}Deleted Message: {w}{mss.content}")
                                else:
                                    print(f"{lb}[{w}INFO{lb}] {w}| {lb}Deleted Message: {w}{mss.id}")
                             
                                
                                if mss.is_system() == True:
                                    print(f"{lb}[{w}INFO{lb}] {w}| {lb}System Message Ignored")
                                    return
                                else:
                                   if logmsgs == "True":
                                        f.write(mss.content + "\n")      
                                        await mss.delete() 
                                   else:
                                      await mss.delete()   
                else:
                    async for mss in channel.history(limit=int(amount)):
                        if (mss.author.id == Eagle.user.id):
                         if logmsgs == "True":
                            if mss.is_system() == True:
                                print(f"{lb}[{w}INFO{lb}] {w}| {lb}System Message Ignored")
                    
                                return
                            else:
                                if showmessages == "True":
                                    print(f"{lb}[{w}INFO{lb}] {w}| {lb}Deleted Message: {w}{mss.content}")
                                else:
                                    print(f"{lb}[{w}INFO{lb}] {w}| {lb}Deleted Message: {w}{mss.id}")
                                
                            
                            if mss.is_system() == True:
                                print(f"{lb}[{w}INFO{lb}] {w}| {lb}System Message Ignored")
                                return
                            else:
                                await mss.delete()      
            await mainmenu()
               
             
async def purgealldms():
    f = open("LoggedMessages.txt","a")
    for channel in Eagle.private_channels:
            if isinstance(channel,DMChannel):
                    if logmsgs == "True":
                        f.write(f"================================================================")
                        f.write(str(channel.recipient))
                    else:
                        pass
                    async for mss in channel.history(limit=None):
                        if (mss.author.id == Eagle.user.id):
                         if logmsgs == "True":
                            try:
                                f.write(mss.content + "\n")
                                f.flush()
                            except Exception as bruh:
                                critical(bruh)
                                
                                
                                pass
                         if logmsgs == "True":
                            if mss.is_system() == True:
                                print(f"{lb}[{w}INFO{lb}] {w}| {lb}System Message Ignored")
                                return
                            else:
                                
                                try:
                                     

                                  
                                     
                                 await mss.delete()    
                                 try:
                                    print(f"{lb}[{w}INFO{lb}] {w}| {lb}Deleted Message: {w}{mss.content}")
                                 except Exception as buh:
                                     critical(buh)
                                     pass
                                except Exception as b:
                                    critical(b)
                                    pass
                                             
    await mainmenu()
            
async def purgeallgcs():
    for channel in Eagle.private_channels:
            if isinstance(channel,GroupChannel):
                    async for mss in channel.history(limit=None):
                        if (mss.author.id == Eagle.user.id):
                         if logmsgs == "True":
                            if mss.is_system() == True:
                                print(f"{lb}[{w}INFO{lb}] {w}| {lb}System Message Ignored")
                    
                                return
                            else:
                                print(f"{lb}[{w}INFO{lb}] {w}| {lb}Deleted Message: {w}{mss.content}")
                             
        
                            if mss.is_system() == True:
                                print(f"{lb}[{w}INFO{lb}] {w}| {lb}System Message Ignored")
                                return
                            else:
                                await mss.delete()      
            await mainmenu()
               
               
async def purgeallchannels():
    theid = input(f"{fore.LIGHTBLUE_EX}{os.getlogin()}{w}@{fore.LIGHTBLUE_EX}{platform.node()} {fore.LIGHTGREEN_EX}~{fore.WHITE}$ {w}Guild ID: {fore.WHITE}")
    for guild in Eagle.guilds:
        if guild.id == int(theid):
          for channel in guild.channels:
            if isinstance(channel,TextChannel):
                try:
                     async for mss in channel.history(limit=None):
                        if (mss.author.id == Eagle.user.id):
                         if logmsgs == "True":
                            
                                if showmessages == "True":
                                        print(f"{lb}[{w}INFO{lb}] {w}| {lb}Deleted Message: {w}{mss.content}")
                                        await mss.delete()      
                                        

                                else:
                                    print(f"{lb}[{w}INFO{lb}] {w}| {lb}Deleted Message: {w}{mss.id}")
               
                except:
                    pass
          await mainmenu()
            


async def mainmenu():

    os.system("cls;clear")
  
  
    print(f"""
                                        ██╗  ██╗ ██████╗ ██████╗ ██████╗  █████╗ 
                                        ██║ ██╔╝██╔═══██╗██╔══██╗██╔══██╗██╔══██╗
                                        █████╔╝ ██║   ██║██████╔╝██████╔╝███████║
                                        ██╔═██╗ ██║   ██║██╔══██╗██╔══██╗██╔══██║
                                        ██║  ██╗╚██████╔╝██████╔╝██║  ██║██║  ██║
                                        ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝""".replace("█",f"{fore.WHITE}█{lb}")) 
    print(f"""
                                          ┌──────{lb}─────────────{b}──────────{lb}────────┐
                                          |  [{w}+{lb}] {w}| Made By {fore.LIGHTGREEN_EX}StvnedEagle{w}   {lb}  |
                                          └──────{b}────────────{lb}────────────{b}───────┘""")
    print(f"{lb}──────────────{b}────────────────────{lb}──────────────────────────────────────────────{b}──────────────────{lb}──────────────{b}────────\n")
    print(f'                               {lb}═════════════════{b}═══════════════{lb}════════════════{b}═══════════════{fore.RESET}\n')
    print(f'{fore.LIGHTBLUE_EX}                                {lb}[{w}1{lb}]{w}{fore.RESET} Purge A DM      {lb}[{w}2{lb}]{w}{fore.RESET} Purge a GC      {lb}[{w}3{lb}]{w}{fore.RESET} Purge A Channel    '        )    
    print(f'{fore.LIGHTBLUE_EX}                                {lb}[{w}4{lb}]{w}{fore.RESET} Purge All DMs   {lb}[{w}5{lb}]{w}{fore.RESET} Purge All GCs{lb}   [{w}6{lb}]{w}{fore.RESET} Purge All Channels  '        )    
    print()    
    print(f'                               {lb}═════════════════{b}═══════════════{lb}════════════════{b}═══════════════{fore.RESET}\n')
    choice = input(f"{fore.LIGHTBLUE_EX}{os.getlogin()}{w}@{fore.LIGHTBLUE_EX}{platform.node()} {fore.LIGHTGREEN_EX}~{fore.WHITE}$ {w}")
    if choice == "1":
        threading.Thread(target=await purgedm()).start()
    elif choice == "2":
        threading.Thread(target=await purgegc()).start()
    elif choice == "3":
        threading.Thread(target=await purgechannel()).start()
    elif choice == "4":
        threading.Thread(target=await purgealldms()).start()
    elif choice == "5":
        threading.Thread(target=await purgeallgcs()).start()
    elif choice == "6":
        threading.Thread(target=await purgeallchannels()).start()
    else:
        print(f"{w}input: ERROR: Invalid Choice has been given")
        await asyncio.sleep(1.7)
        await mainmenu()





async def modecheck():
    os.system("cls;clear")
    logging.critical("What Mode Do you wanna use? [c = Commandly / r = Remotely")
    ok = input()
    if "c" in ok:
        os.system("python Zbotmode.py")
        exit()
    else:
         
        await mainmenu()


async def start():
    if alreadystarted == True:
        return
    else:
        await modecheck()
        
        
        
        
@Eagle.event
async def on_ready():
    global alreadystarted
    logging.info(f"Connection: {Eagle.user.name}#{Eagle.user.discriminator}")
    if alreadystarted == False:
     await start()
    else:
        pass
    alreadystarted = True
    




def variant2(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
        return False
    else:
        return  True
    
    
def tokenchange():
    tokens = input(f"{fore.LIGHTBLUE_EX}{os.getlogin()}{w}@{fore.LIGHTBLUE_EX}{platform.node()} {fore.LIGHTGREEN_EX}~{fore.WHITE}$ {w}Token: ")
    
    Eagle.run(tokens,bot=False)
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
 

  
       

          

try:      
    Eagle.run(token, bot=False)
except:
    logging.critical("Something Failed... Starting Troubleshooter")
    tokenchange()