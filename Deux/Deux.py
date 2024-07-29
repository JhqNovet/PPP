import os
import discord, random
from discord.ext import commands

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

token = "MTI1OTk5MTkwNTQyMTIzNDE4Ng.GHv_Yl.opgFRugpKY-aVioOUGF72KreXoPCxvWY1yQGBQ"

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    print(f"Bienvenido, se ha iniciado como {bot.user}")

@bot.command()
async def heh(ctx,cout_heh = 5):
    await ctx.send("he" * cout_heh)

@bot.command()
async def triad(ctx):
    await ctx.send("The world is mine, but my heart is yours ")

@bot.command()
async def eva(ctx):
    files = os.listdir('img/eva')
    eva_random =random.choice(files)
    eva_path = os.path.join('img/eva',eva_random)
    await ctx.send(file = discord.File(eva_path))

@bot.command()
async def joker(ctx):
    files = os.listdir('img')
    joker_random =random.choice(files)
    joker_path = os.path.join('img',joker_random)
    await ctx.send(file = discord.File(joker_path))




bot.run(token)
