# Import discrod.py
import discord

# Fetch weather info
import FW

# Import COMMANDS from the DISCORD.EXT module.
from discord.ext import commands


DISCORD_TOKEN = '' # API Token

intents = discord.Intents.all() # or .all() if you ticked all, that is easier
intents.members = True # If you ticked the SERVER MEMBERS INTENT

bot = commands.Bot(command_prefix="$", intents=intents)# Creates a new bot object with $ prefix and set the specified intents.


@bot.command()
async def temp(ctx, arg):#Defines the command testBot
	try:
		#Retrieve the actual temp in the specified argument and round to 2 digits of decimal point
		temp = round(FW.FetchWeather.getTemp(FW.FetchWeather.getWeather(FW.FetchWeather.replaceChar(arg))), 2)
		await ctx.channel.send("Aloha Wachin " + ctx.message.author.name +"\n" + "La temperatura en " + arg + " es de : " + str(temp) + " °C")
	except:
		print("An exception ocurred")

@bot.command()
async def humidity(ctx, arg):#Defines the command testBot
	try:
		#Retrieve the actual temp in the specified argument and round to 2 digits of decimal point
		humidity = round(FW.FetchWeather.getHumidity(FW.FetchWeather.getWeather(FW.FetchWeather.replaceChar(arg))), 2)
		await ctx.channel.send("Aloha Wachin " + ctx.message.author.name +"\n" + "La humedad en " + arg + " es de : " + str(humidity) + " %")
	except:
		print("An exception ocurred")

bot.run(DISCORD_TOKEN)#Executes de bot with the specified token



