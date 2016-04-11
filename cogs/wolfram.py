import discord
from discord.ext import commands
from random import randint
from random import choice
import random
import aiohttp
import asyncio
import os
import wolframalpha
from .utils import checks

class Wolfram:
    "( ͡° ͜ʖ ͡°)"
    def __init__(self, bot):
        self.bot = bot
        self.client = wolframalpha.Client("RGTRAE-AVKP22Q8H7")


    @commands.command(no_pm=False)
    async def wolfram(self, q: str):
        try:
            r = self.client.query(q)
            for pod in r.pods:
                await self.bot.say("**{}**: {}".format(pod.title, pod.text))
        except:
            await self.bot.say("Sorry, unable to find any results :(")

def setup(bot):
    n = Wolfram(bot)
    bot.add_cog(n)
