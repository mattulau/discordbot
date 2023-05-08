import discord
from discord.ext import commands
import random

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping.py is ready")

    @commands.command()
    async def ping(self, ctx):
        bot_latency = round(self.client.latency * 1000)

        await ctx.send(f"Pong! {bot_latency} ms.")
    
    @commands.command()
    async def matt(self, ctx):
        await ctx.send(file = discord.File("./assets/rick.gif"))

    @commands.command()
    async def pent(self, ctx):
        await ctx.send(file = discord.File("./assets/luffy-one-piece.gif"))
    
    @commands.command()
    async def naji(self, ctx):
        await ctx.send(file = discord.File("./assets/omg-new-jeans.gif"))

    @commands.command()
    async def sam(self, ctx):
        await ctx.send(file = discord.File("./assets/giphy.gif"))

    @commands.command()
    async def gm(self, ctx):
        await ctx.send(file = discord.File("./assets/sakuteam-sakurateam.gif"))

    @commands.command()
    async def gn(self, ctx):
        await ctx.send(file = discord.File("./assets/cant-sleep-pokemon.gif"))
    
    @commands.command(aliases = ["8ball", "eightball", "eight ball", "8 ball"])
    async def ask(self, ctx, *, questions):
        with open("respond.txt", "r") as f:
            random_responses = f.readlines()
            response = random.choice(random_responses)

        await ctx.send(response)

async def setup(client):
    await client.add_cog(Ping(client))


