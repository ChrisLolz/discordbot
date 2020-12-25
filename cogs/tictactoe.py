import discord
from discord.ext import commands

class tictactoe(commands.Cog):
    def __init__(self,client):
        self.client = client
        self.player = 1
        self.ongoing = False
        self.board = [":one:",":two:",":three:",
                      ":four:",":five:",":six:",
                      ":seven:",":eight:",":nine:"]
    async def push(self,ctx):
        await ctx.send(f"{self.board[0]}{self.board[1]}{self.board[2]}")
        await ctx.send(f"{self.board[3]}{self.board[4]}{self.board[5]}")
        await ctx.send(f"{self.board[6]}{self.board[7]}{self.board[8]}")

    @commands.command()
    async def tictactoe(self,ctx):
        if self.ongoing == False:
            await self.push(ctx)
            await ctx.send("It's player1's turn\nUse !play position(ex.!play 1 changes the first tile)")
            self.ongoing = True

    @commands.command()
    async def play(self,ctx,pos):
        if self.ongoing == True:
            pos = int(pos)
            if self.player == 1:
                if self.board[pos-1] != (":x:" or ":o:"):
                    self.board[pos-1] = ':x:'
                    self.player = 2
                    await self.push(ctx)
                    await ctx.send("It's player2's turn")
                else:
                    await ctx.send("You can't do that, try another position")
            elif self.player == 2:
                if self.board[pos-1] != (":x:" or ":o:"):
                    self.board[pos-1] = ':o:'
                    self.player = 1
                    await self.push(ctx)
                    await ctx.send("It's player1's turn")
                else:
                    await ctx.send("You can't do that, try another position")

            #horizontal
            if self.board[0] == self.board[1] == self.board[2] == (":x:" or ":o:"):
                await ctx.send(f"player {self.player} won")
                self.ongoing = False
            if self.board[3] == self.board[4] == self.board[5] == (":x:" or ":o:"):
                await ctx.send(f"player {self.player} won")
                self.ongoing = False
            if self.board[6] == self.board[7] == self.board[8] == (":x:" or ":o:"):
                await ctx.send(f"player {self.player} won")
                self.ongoing = False

            #vertical
            if self.board[0] == self.board[3] == self.board[6] == (":x:" or ":o:"):
                await ctx.send(f"player {self.player} won")
                self.ongoing = False
            if self.board[1] == self.board[4] == self.board[7] == (":x:" or ":o:"):
                await ctx.send(f"player {self.player} won")
                self.ongoing = False
            if self.board[2] == self.board[5] == self.board[8] == (":x:" or ":o:"):
                await ctx.send(f"player {self.player} won")
                self.ongoing = False

            #diagonal
            if self.board[0] == self.board[4] == self.board[8] == (":x:" or ":o:"):
                await ctx.send(f"player {self.player} won")
                self.ongoing = False
            if self.board[2] == self.board[4] == self.board[6] == (":x:" or ":o:"):
                await ctx.send(f"player {self.player} won")
                self.ongoing = False

            if self.ongoing == False:
                self.player = 1
                self.board = [":one:",":two:",":three:",
                            ":four:",":five:",":six:",
                            ":seven:",":eight:",":nine:"]
        else:
            await ctx.send("!tictactoe before you can play the game")

def setup(client):
    client.add_cog(tictactoe(client))