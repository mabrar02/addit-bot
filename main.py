import discord
import requests
from discord.ext import commands
from hidden import AUTH_KEY
from hidden import API_KEY

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("ADDIT BOT READY")
    print("---------------")



@client.command()
async def getAcc(ctx, *, acc):
    acc.replace(" ", "%20")
    api_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + acc
    api_req = api_url + "?api_key=" + API_KEY
    response = requests.get(api_req)

    await ctx.send(response.json())

client.run(AUTH_KEY)