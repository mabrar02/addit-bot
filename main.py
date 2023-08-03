import discord
from discord.ext import commands
from hidden import AUTH_KEY

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("ADDIT BOT READY")
    print("---------------")


@client.command()
async def helo(ctx):
    await ctx.send("testing hello from bot")


client.run(AUTH_KEY)