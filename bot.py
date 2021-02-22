# bot.py

import os
import discord

#created variables to hide token id and guild id's
TOKEN = os.environ['TOKEN']
GUILD = os.environ['GUILD']


client = discord.Client()
#checks if the bot joined the correct server
@client.event
async def on_ready():

    for guild in client.guilds:
        if guild.id == GUILD:
            break

    print(f'{client.user} has connected to the server')

client.run(TOKEN)






