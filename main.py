import discord
import os
from discord.ext import commands

key = os.environ['token']
intents = discord.Intents.default()
intents.typing = True
intents.presences = True
client = commands.Bot(command_prefix='!', intents=intents)
client.remove_command('help')

# variables

# look guys
@client.event
async def on_member_update(before, after):
    if str(before.status) == "online":
        if str(after.status) == "offline":
            channel = client.get_channel(789694075787935778)
            await channel.send(f"LOOK GUYS HE DISCONNECTED {after.mention}")

# commands
@client.command()
async def help(ctx):
    await ctx.send("Type !hang to play hangman :flushed:\nType !clear to clear all messages in the channel\nType !tictacetoe to play tictactoe")

@client.command()
async def clear(ctx):
    await ctx.channel.purge()

@client.command()
async def about(ctx):
    await ctx.send("Created by the one and only Chris")

client.load_extension("cogs.hangman")
client.load_extension("cogs.tictactoe")
client.run(key)
