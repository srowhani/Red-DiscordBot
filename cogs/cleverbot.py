import discord
from discord.ext import commands
import aiohttp
import asyncio
import os
import cleverbot

class CleverBot:
    def __init__(self, bot):
        self.bot = bot
        self.cb = cleverbot.Cleverbot()


    @commands.command()
    async def ask(self, *question):
        try:
            await self.bot.say(self.cb.ask(" ".join(question)))
        except:
            print("Error")

def setup(bot):
    n = CleverBot(bot)
    bot.add_cog(n)
