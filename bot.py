import os
import nextcord
from nextcord import Interaction
from nextcord.ext import commands

bot = commands.Bot(command_prefix="!", intents=nextcord.Intents.all())
bad_words=[ 'ntm', 'nique','pute']


@bot.event
async def on_ready():
    print("up")


@bot.event
async def on_message(message):
    for mot in message.content.split():
        if mot in bad_words:
            await message.delete()
            break


bot.run(os.environ['TOKEN'])
