import discord
from discord.ext import commands
import random
import aiohttp
import asyncio
import os
import wolframalpha
from .utils.settings import Settings

class Wolfram:
    def __init__(self, bot):
        key = Settings().wolframkey
        self.bot = bot
        self.client = wolframalpha.Client(key)


    @commands.command()
    async def wolfram(self, *question):
        str = ''
        try:
            r = self.client.query(" ".join(question))
            for pod in r.pods:
                if not pod.text:
                    str = "**{}**:\n\t{}".format(pod.title, pod.img)
                else:
                    str = "**{}**:\n\t{}".format(pod.title, pod.text)
                await self.bot.say(str)
        except: pass

def setup(bot):
    n = Wolfram(bot)
    bot.add_cog(n)
