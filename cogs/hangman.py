import discord
from discord.ext import commands

hangwords = [
    "BLACKLIVESMATTER", "DRAGON", "SCHOOL", "DONALDTRUMP", "JOEBIDEN"
]

class hangman(commands.Cog):
    def __init__(self,client):
        self.client = client
        self.lines = "?"*len(hangwords[1])

    @commands.command()
    async def hang(self,ctx):
        await ctx.send(f"I'm thinking of a {len(hangwords[1])} letter word")
        game = discord.Embed(title="Hangman", description=self.lines)
        game.set_image(url="https://i.imgur.com/hRzVg1N.png")
        game.set_footer(text="!guess <letter> to guess and !quit to stop playing")
        await ctx.send(embed=game)

    @commands.command()
    async def guess(self,ctx,arg):
        if arg == hangwords[1]:
            await ctx.send("POGGERS")

    @commands.command()
    async def quit(self,ctx):
        await ctx.send("adios amigo")

def setup(client):
    client.add_cog(hangman(client))