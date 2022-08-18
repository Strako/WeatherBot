import discord

# Import COMMANDS from the DISCORD.EXT module.
from discord.ext import commands

# API Token
DISCORD_TOKEN = 'MTAwOTY4MzYwODMxMjc0NjA0Ng.GZMd4o.jGp5UNTE266qwGjCXCKbiZw9oelM9OvdFlGji4'

intents = discord.Intents.all() # or .all() if you ticked all, that is easier
intents.members = True # If you ticked the SERVER MEMBERS INTENT

# Creates a new bot object with $ prefix and set the specified intents.
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.command()
async def testBot(ctx):
	await ctx.channel.send("Aloha Wachin " + ctx.message.author.name)

# Executes de bot with the specified token
bot.run(DISCORD_TOKEN)


