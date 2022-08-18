from tkinter import W
import discord
import requests
import json

# Import COMMANDS from the DISCORD.EXT module.
from discord.ext import commands

# API Token
DISCORD_TOKEN = 'MTAwOTY4MzYwODMxMjc0NjA0Ng.GZMd4o.jGp5UNTE266qwGjCXCKbiZw9oelM9OvdFlGji4'

intents = discord.Intents.all() # or .all() if you ticked all, that is easier
intents.members = True # If you ticked the SERVER MEMBERS INTENT

w_url = "https://api.openweathermap.org/data/2.5/weather?q=San Luis Potosí&appid=c5b301810a55cb0bbfc76fd009e4d5a5"#url
w_resp= requests.get(w_url)#se hace la request//make request
w_data = w_resp.json()#se guarda el json en una variable//sabe the info in json format


temp = (w_data['main']['temp']) -273.15#como la temperatura viene en kelvin se convierte a celcius y se guarda en temp//convert the temperature from kelvin to celcius


print("temperatura de: ", temp)#se imprime nomas pa calar//print just to test


# Creates a new bot object with $ prefix and set the specified intents.
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.command()
async def testBot(ctx):
	await ctx.channel.send("Aloha Wachin " + ctx.message.author.name)

# Executes de bot with the specified token
bot.run(DISCORD_TOKEN)


