# bot.py

import discord
from discord.ext import commands
import json
import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client(intents=discord.Intents.all())
PREFIX: str = '$'


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=os.getenv('DISCORD_GUILD'))
    print (
        f'{client.user} is connected to the following server:\n'
        f'{guild.name}'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$pet'):
        await message.channel.send(os.getenv('PET_PHRASES').split('/')[random.randint(0,2)])


client.run(os.getenv('DISCORD_TOKEN'))
