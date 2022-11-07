# bot.py

import discord
import json
import requests
import random
import os

from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = '[Bot Token]'
DISCORD_GUILD = '[Server Name]'

client = discord.Client(intents=discord.Intents.all())
PREFIX: str = '$'


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=DISCORD_GUILD)
    print (
        f'{client.user} is connected to the following server:\n'
        f'{guild.name}'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$pet'):
        await message.channel.send('bro I am literally a cat, leave me alone')


client.run(DISCORD_TOKEN)
