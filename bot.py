#add all of the modules and the packages required

import os
import logging

import discord
from discord.ext import commands 
from cogs.musicCog import MusicCog
from cogs.errorCog import ErrorCog
from cogs.otherCog import CommandsCog

#add logging for all of the updates from discord
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#this helps us to get the bot token, which is like the username for Discord to identify the bot
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
activity = discord.Activity(type=discord.ActivityType.listening, name="to music in vc | ted.help")

bot = commands.Bot(command_prefix='ted.', intents=intents, activity=activity, status=discord.Status.idle)

@bot.event
async def on_ready():
    print("TedTunes V2 is Online!")


bot.add_cog(MusicCog(bot))
bot.add_cog(CommandsCog(bot))
bot.add_cog(ErrorCog(bot))

bot.run(TOKEN)
