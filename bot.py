# bot.py
#import cogs
import json
import os
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!')


#created variables to hide token id and guild id's
TOKEN = os.environ['TOKEN']
GUILD = os.environ['GUILD']


client = discord.Client()
#checks if the bot joined the correct server
@client.event
async def on_ready():

    for guild in client.guilds:
        if guild.id == GUILD:
            print(guild)
            break

    print(f'{client.user} has connected to the server')



print("test")
@bot.command()
async def ping(ctx, arg):
    await ctx.send(arg)

@bot.event
async def on_message(ctx, message):
    if message.content == "hello":
        await ctx.send("fuck you")

    await bot.process_commands(message)


print(TOKEN,GUILD)

client.run(TOKEN)






