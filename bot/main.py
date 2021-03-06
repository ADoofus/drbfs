import discord
import os
from colorama import Fore, Back, Style
from datetime import datetime
from tzlocal import get_localzone_name
import pytz

client = discord.Client()
term_size = os.get_terminal_size()
me = os.getenv('user1')
me2 = os.getenv('user2')
me3 = os.getenv('user3')
d = os.getenv('user4')
d2 = os.getenv('user5')
token = os.getenv('TOKEN')
tz = pytz.timezone('America/Los_Angeles')

@client.event
async def on_ready():
  print("    ___                                           ____    ")
  print("   /   |  ____ ___  ____  ____ ___  _______     /  __  \  ")
  print("  / /| | / __ `__ \/ __ \/ __ `/ / / / ___/    |  [  ]  | ")
  print(" / ___ |/ / / / / / /_/ / /_/ / /_/ (__  )     |  ____  | ")
  print("/_/  |_/_/ /_/ /_/\____/\__, /\__,_/____/      |  |  |  | ")
  print("                       /____/                             "
  print(Fore.LIGHTBLACK_EX + '=' * term_size.columns)
  print(Fore.RED + "Now reading messages:",)
  print(Fore.LIGHTBLACK_EX + '=' * term_size.columns)

@client.event
async def on_message(message):
  timeZone = pytz.timezone(str("America/Los_Angeles")) 
  datetime_now = datetime.now(timeZone)
  print(Fore.GREEN + "Server: " + str(message.guild.name) + Fore.LIGHTBLACK_EX + "   |  " + Fore.BLUE + "Channel: #" + str(message.channel))
  current_time = datetime_now.strftime("%A, %m-%d-%Y [%H:%M %p]")
  print(Fore.LIGHTBLACK_EX + current_time)
  if message.author.id == me or me2 or me3:
    print(Fore.RED + str(message.author.name) + ": " + Fore.WHITE + str(message.content))
  elif message.author.id == d:
    print(Fore.LIGHTBLUE_EX + str(message.author.name) + ": " + Fore.WHITE + str(message.content))
  elif message.author.id == d2:
      print(Fore.LIGHTMAGENTA_EX + str(message.author.name) + ": " + Fore.WHITE + str(message.content))
  print(Fore.LIGHTBLACK_EX + '=' * term_size.columns)
    
client.run(token)
