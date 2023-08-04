import discord
from discord.ext import commands
from hidden import AUTH_KEY

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("ADDIT BOT READY")
    print("---------------")


def to_upper(argument):
    return argument.upper()

@client.command()
async def up(ctx, *, content: to_upper):
    await ctx.send(content)

@client.command()
async def test(ctx):
    message = "you're not him"
    if(ctx.author.name.lower() == "addit"):
        message = "you're him"

    await ctx.send(message)

client.run(AUTH_KEY)