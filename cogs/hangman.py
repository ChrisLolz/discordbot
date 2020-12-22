import discord
import random
from discord.ext import commands

words = [
    "BLACKLIVESMATTER", "DRAGON", "SCHOOL", "DONALDTRUMP", "JOEBIDEN"
]

men = ["https://i.imgur.com/hRzVg1N.png","https://i.imgur.com/cQmLMDO.png","https://i.imgur.com/sAeTvqP.png",
    "https://i.imgur.com/yHGrZqc.png","https://i.imgur.com/UKiV6J9.png","https://i.imgur.com/w7QJQFH.png",
    "https://i.imgur.com/apN30T6.png","https://i.imgur.com/KBMsCp9.png"
]

class hangman(commands.Cog):
    def __init__(self,client):
        self.client = client
        self.ranword = random.choice(words)
        self.lines = ['?']*(len(self.ranword))
        self.currman = 0

    @commands.command()
    async def hang(self,ctx):
        await ctx.send(f"I'm thinking of a {len(self.ranword)} letter word")
        game = discord.Embed(title="Hangman", description="".join(self.lines))
        game.set_image(url=men[self.currman])
        game.set_footer(text="!guess <letter> to guess and !quit to stop playing")
        await ctx.send(embed=game)

    @commands.command()
    async def guess(self,ctx,arg):
        if len(arg.upper()) == 1:
            if arg.upper() in self.ranword and arg.upper() not in self.lines:
                if "?" in self.lines:
                    if self.ranword.count(arg.upper()) > 1:
                        indices = [i for i, a in enumerate(self.ranword) if a == arg.upper()]
                        for i in indices:
                            self.lines[i] = arg.upper()
                    else:
                        pos = self.ranword.find(arg.upper())
                        self.lines[pos] = arg.upper()
                else:
                    await ctx.send("POGGERS YOU WON!!!")
                game = discord.Embed(title="Hangman", description="".join(self.lines))
                game.set_image(url=men[self.currman])
                game.set_footer(text="!guess <letter> to guess and !quit to stop playing")
                await ctx.send(embed=game)
            elif arg.upper() in self.lines:
                await ctx.send("YOU ALREADY GUESSED THAT :rage:")
            else:
                if self.currman < 6:
                    self.currman = self.currman + 1
                    game = discord.Embed(title="Hangman", description="".join(self.lines))
                    game.set_image(url=men[self.currman])
                    game.set_footer(text="!guess <letter> to guess and !quit to stop playing")
                    await ctx.send(embed=game)
                else:
                    self.currman = self.currman + 1
                    game = discord.Embed(title="Hangman", description="".join(self.lines))
                    game.set_image(url=men[self.currman])
                    game.set_footer(text="!guess <letter> to guess and !quit to stop playing")
                    await ctx.send(embed=game)
                    await ctx.send("YOU'RE A LOSER")
                    self.ranword = random.choice(words)
                    self.currman = 0
                    self.lines = ['?'] * (len(self.ranword))
        else:
            if arg.upper() == self.ranword:
                game = discord.Embed(title="Hangman", description=self.ranword)
                game.set_image(url=men[self.currman])
                game.set_footer(text="!guess <letter> to guess and !quit to stop playing")
                await ctx.send(embed=game)
                await ctx.send("POGGERS YOU GUESSED IT RIGHT!!")
                self.ranword = random.choice(words)
                self.currman = 0
                self.lines = ['?'] * (len(self.ranword))
            else:
                if self.currman < 6:
                    self.currman = self.currman + 1
                    game = discord.Embed(title="Hangman", description="".join(self.lines))
                    game.set_image(url=men[self.currman])
                    game.set_footer(text="!guess <letter> to guess and !quit to stop playing")
                    await ctx.send(embed=game)
                else:
                    self.currman = self.currman + 1
                    game = discord.Embed(title="Hangman", description="".join(self.lines))
                    game.set_image(url=men[self.currman])
                    game.set_footer(text="!guess <letter> to guess and !quit to stop playing")
                    await ctx.send(embed=game)
                    await ctx.send("YOU LOST HAHAAHH")
                    self.ranword = random.choice(words)
                    self.currman = 0
                    self.lines = ['?'] * (len(self.ranword))

    @commands.command()
    async def quit(self,ctx):
        self.ranword = random.choice(words)
        self.currman = 0
        self.lines = ['?']*(len(self.ranword))
        await ctx.send("adios amigo")

def setup(client):
    client.add_cog(hangman(client))