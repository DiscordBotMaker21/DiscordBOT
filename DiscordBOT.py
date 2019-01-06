import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import time
import random
import os
import math
import socket

bot = commands.Bot(command_prefix="*")
TOKEN = "NTA2NTA4Mzc0MzA1ODAwMTk0.Dwm5WQ.4wpGuRr13g5u0ZYLvP-gvZgu5y4"


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
bot.run(NTA2NTA4Mzc0MzA1ODAwMTk0.Dwm5WQ.4wpGuRr13g5u0ZYLvP-gvZgu5y4)
