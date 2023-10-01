import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default()        )

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
     
@bot.command()
async def see_you(ctx, count_bye = 2):
    await ctx.send("Bye" * count_bye)    

bot.run("MTE1NTUwMDcwNDY5MDA3Nzc5Ng.GkzB6t.dfZYLAWN3gPKSTOPjE2FCSaBZY55vtD2dpKqC4")
