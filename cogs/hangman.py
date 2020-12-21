import discord
from main import gamehang
from discord.ext import commands

hangwords = [
    "BLACKLIVESMATTER", "DRAGON", "SCHOOL", "DONALDTRUMP", "JOEBIDEN"
]
print(gamehang)
class hangman(commands.Cog):
    def __init__(self,client):
        self.client = client
    @commands.Cog.listener()
    async def on_message(self,message):
        if message == "!hang" and gamehang == False:
            gamehang = True
            channel = client.get_channel(789694075787935778)
            await channel.send(f"I'm thinking of a {len(hangwords[1])} letter word")
            game = discord.Embed(title="Hangman")
            game.set_image(url="https://i.imgur.com/hRzVg1N.png")
            await channel.send(embed=game)
        if message.content == hangwords[1]:
            channel = client.get_channel(789694075787935778)
            await channel.send("YOU GOT IT POGGERS :open_mouth:")
            gamehang = False
        if message.content == "!quit":
            gamehang = False
            channel = client.get_channel(789694075787935778)
            await channel.send("adios amigo")

def setup(client):
    client.add_cog(hangman(client))