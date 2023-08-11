import discord
from discord.ext import commands
from riotApi import *
from keys import DISC_AUTH_KEY


client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("ADDIT BOT READY")
    print("---------------")


@client.command()
async def getAcc(ctx, *, acc):

    resp_json = getAccountInfo(acc)


    img_url = "http://ddragon.leagueoflegends.com/cdn/13.15.1/img/profileicon/%d.png" % (resp_json['profileIconId'])
    acc_name = resp_json['name']
    acc_level = resp_json['summonerLevel']

    print(resp_json)
    await ctx.send(img_url)
    await ctx.send("Account Name: %s || Level: %d" % (acc_name, acc_level))


@client.command()
async def recentPerformance(ctx, *, acc):
    accountData = getAccountInfo(acc)
    puuid = accountData["puuid"]
    matches = getLastMatches(puuid, 20)
    winCount = 0

    await ctx.send("Calculating performance...")
    for match in matches:
        matchData = getMatchData(match)
        playerIndex = matchData['metadata']['participants'].index(puuid)
        win = matchData['info']['participants'][playerIndex]['win']
        if(win):
            winCount += 1


    await ctx.send("This player won %d of their last 20 ranked games" % (winCount))

client.run(DISC_AUTH_KEY)
