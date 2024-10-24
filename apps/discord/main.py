import discord
from discord.ext import commands
import os
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run(TOKEN)

