import discord
import os
from discord.ext import commands
key = os.environ['token']
intents = discord.Intents.default()
intents.typing = True
intents.presences = True
client = discord.Client(intents=intents)

#cogs
"""
@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cigs,{filename[:-3]}')
"""
#variables
global gamehang
gamehang = False

@client.event
async def on_member_update(before, after):
    if str(before.status) == "online":
        if str(after.status) == "offline":
            channel = client.get_channel(789694075787935778)
            await channel.send(f"LOOK GUYS HE DISCONNECTED {after.mention}")

@client.event
async def on_message(message):
    if gamehang == False:
        if message.content == "!help":
            channel = client.get_channel(789694075787935778)
            await channel.send("Type !hang to play hangman :flushed:\nType !clear to clear all messages in the channel")
        if message.content == "!hang":
            gamehang == True
        if message.content == "!clear":
            channel = client.get_channel(789694075787935778)
            await channel.purge()

client.load_extension('cogs.hangman')
client.run(key)