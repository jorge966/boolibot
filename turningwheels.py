import discord
import random
from discord.ext import commands




class Gambling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    def coinflip(self):
        return random.randint(0,1)

    #@commands.command()
    #async def gamble(self, ctx , money = int):
        
