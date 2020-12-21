import discord
import os
key = os.environ['token']
intents = discord.Intents.default()
intents.typing = True
intents.presences = True
client = discord.Client(intents=intents)
hangman = False
@client.event
async def on_member_update(before, after):
    if str(before.status) == "online":
        if str(after.status) == "offline":
            channel = client.get_channel(789694075787935778)
            await channel.send(f"LOOK GUYS HE DISCONNECTED {after.mention}")
hangwords = [
    "BLACKLIVESMATTER", "DRAGON", "SCHOOL", "DONALDTRUMP", "JOEBIDEN"
]
@client.event
async def on_message(message):
    global hangman
    if hangman == True:
        if message.content == "!hang":
            hangman = True
            channel = client.get_channel(789694075787935778)
            await channel.send(f"I'm thinking of a {len(hangwords[1])} letter word")
        if message.content == hangwords[1]:
            channel = client.get_channel(789694075787935778)
            await channel.send("YOU GOT IT POGGERS :open_mouth:")
            hangman = False
        if message.content == "!quit":
            hangman = False
            channel = client.get_channel(789694075787935778)
            await channel.send("adios amigo")
    else:
        if message.content == "!help":
            channel = client.get_channel(789694075787935778)
            await channel.send("Type !hang to play hangman :flushed:\nType !clear to clear all messages in the channel")
        if message.content == "!hang":
            hangman = True
            channel = client.get_channel(789694075787935778)
            await channel.send(f"I'm thinking of a {len(hangwords[1])} letter word")
            game = discord.Embed(title="Hangman", description="O\n/|\\\n`|\n/\\")
            await channel.send(embed=game)
        if message.content == "!clear":
            channel = client.get_channel(789694075787935778)
            await channel.purge()

client.run(key)