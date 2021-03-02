# bot.py
#import cogs
import json
import asyncio
import os
import discord
from discord.ext import commands
intents = discord.Intents(messages=True, guilds=True)
bot = commands.Bot(command_prefix='!',intents=intents)


#created variables to hide token id and guild id's
TOKEN = os.environ['TOKEN']
#GUILD = os.environ['GUILD']


client = discord.Client()
#checks if the bot joined the correct server
@bot.event
async def on_ready():

    for guild in client.guilds:
        print(guild)


    print(f'{bot.user} has connected to the server')


@bot.command(pass_context=True)
async def ping(ctx):
    print("pong")
    await ctx.send("pong")

@bot.event
async def on_message(message):  # ctx not needed in certain event like these
    if message.content == "hello" or 'Hello':
        # I had startswith at the end but didnt seem to work, will have to find a way to make it work
        await message.channel.send("Wurd up to turd up")
        # normally i would do ctx.send but message.channel.send seems to work here







bot.run(TOKEN)






