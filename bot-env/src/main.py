# Import discrod.py
import discord

# Fetch weather info
import FW

# Import COMMANDS from the DISCORD.EXT module.
from discord.ext import commands


DISCORD_TOKEN = 'MTAwOTY4MzYwODMxMjc0NjA0Ng.GZMd4o.jGp5UNTE266qwGjCXCKbiZw9oelM9OvdFlGji4' # API Token

intents = discord.Intents.all() # or .all() if you ticked all, that is easier
intents.members = True # If you ticked the SERVER MEMBERS INTENT

#print("temperatura de: ", temp)#Print just to test

bot = commands.Bot(command_prefix="$", intents=intents)# Creates a new bot object with $ prefix and set the specified intents.


@bot.command()
async def temp(ctx, arg):#Defines the command testBot
	try:
		temp = round(FW.FetchWeather.getTemp(FW.FetchWeather.getWeather(FW.FetchWeather.replaceChar(arg))), 2)#Retrieve the actual temp in the specified argument
		await ctx.channel.send("Aloha Wachin " + ctx.message.author.name +"\n" + "La temperatura en " + arg + " es de : " + str(temp) + " °C")
	except:
		print("An exception ocurred")
bot.run(DISCORD_TOKEN)#Executes de bot with the specified token



