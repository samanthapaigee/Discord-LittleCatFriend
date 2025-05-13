#bot.py

import datetime
import json
import logging
import random
import os
from dotenv import load_dotenv
load_dotenv()
import discord
from discord.ext import commands

#how often people are bullied or LCF decides to be nice
BULLY_PROB = .2
SWEET_PROB = .2

TOKEN = os.getenv('DISCORD_TOKEN')

#variables for my victims :)
target_member_mean = {int(x) for x in os.getenv('BULLY_USER_ID','').split(',') if x.strip().isdigit()}
target_member_sweet = {int(x) for x in os.getenv('SWEET_USER_ID','').split(',') if x.strip().isdigit()}

#permission stuff
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True
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

@client.command(name='cat')
async def cat(ctx):
    await ctx.send(os.getenv('CAT_PHRASES'))

#because they kept trying to bully my bot!!
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(os.getenv('UNRECOGNIZED_PHRASES').split(',')[random.randint(0,1)])
        return
    raise error

@client.listen('on_message')
async def on_message(message: discord.Message):
    if message.content.startswith('$'):
        return
    if (message.author.id in target_member_mean and random.random() < BULLY_PROB):
        bully_phrases = os.getenv('BULLY_PHRASES').split(',')
        await message.channel.send(random.choice(bully_phrases))
    if (message.author.id in target_member_sweet and random.random() < SWEET_PROB):
        sweet_phrases = os.getenv('SWEET_PHRASES').split(',')
        await message.channel.send(random.choice(sweet_phrases))

#auth
client.run(os.getenv('DISCORD_TOKEN'))
