import discord
import os
import io
import sys
from discord.ext import commands

bot = commands.Bot(command_prefix='c.',description="A bot under development by Antony, Sleedyak and Free TNT. Feel free to drop into the server and help with development and for support at https://discord.gg/qv9UcBh")

developers = [
        311970805342928896,
        316586772349976586,
        292690616285134850
    ]

@bot.event
async def on_ready():
    ctx.send("Bot Is Online")
    

if not os.environ.get('TOKEN'):
  print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
