# bot.py

import json
import random
import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=os.getenv('DISCORD_GUILD'))
    print (
        f'{client.user} is connected!'
    )

@client.command(name='pet')
async def pet(ctx):
    await ctx.send(os.getenv('PET_PHRASES').split(',')[random.randint(0,3)])

client.run(os.getenv('DISCORD_TOKEN'))
