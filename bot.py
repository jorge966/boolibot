# bot.py
#import cogs
import json
import os
import discord
from discord.ext import commands
intents = discord.Intents(messages=True, guilds=True)
bot = commands.Bot(command_prefix='!',intents=intents)


#created variables to hide token id and guild id's
TOKEN = os.environ['TOKEN']
GUILD = os.environ['GUILD']


client = discord.Client()
#checks if the bot joined the correct server
@client.event
async def on_ready():

    for guild in client.guilds:
        print(guild)


    print(f'{client.user} has connected to the server')




@bot.command()
async def ping(ctx):
    print("pong")
    await ctx.send("pong")

@bot.event
async def on_message(ctx, message):
    if message.content == "hello":
        await ctx.send("wurd up to turd up")

    await bot.process_commands(message)




client.run(TOKEN)






