import discord
from discord.ext import commands
import os


client = commands.Bot(intents=discord.Intents.default(), command_prefix='!', description="The Best Bot For The Best User!")


@client.event
async def on_ready():
    print("Il bot è pronto")


@client.command()
async def info(ctx):
    await ctx.send("Info!")




client.run("OTU0ODU3Nzg4ODA1Mzc4MTI4.Gi2aDI.AFDawHiKtFj1dqACAvYoO-2ax52sgOPgiqxsZ4")