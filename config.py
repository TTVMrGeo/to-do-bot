import discord
from discord.ext import commands

INTENTS = discord.Intents.all()
BOT_TOKEN = "MTI5NjgwNzcyNzQ4NTU1MDYyMw.G6roGc.o5iXBwpy-efkwQim2A1o2JlA3S_sxzlSz95UH0"
BOT_PREFIX = ">"
CLIENT = commands.Bot(command_prefix=BOT_PREFIX, intents=INTENTS)