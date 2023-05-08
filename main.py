import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
import os
import asyncio

client = commands.Bot(command_prefix=".", intents=discord.Intents.all())

bot_status = cycle(["Mickey Mouse IRL"])

@tasks.loop(seconds = 20)
async def change_status():
    await client.change_presence(activity = discord.Game(next(bot_status)))

@client.event
async def on_ready():
    print("Success Bot is connected to Discord")
    change_status.start()

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with client:
        await load()
        await client.start("MTEwMjQyNzYxMjk5Mjc3NDIyNQ.GjxuXb.tKWoDPuURgTpiddTTwUCgme5OKuXfh3Oe7KrlM")


asyncio.run(main())


