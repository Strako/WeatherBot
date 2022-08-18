import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('WeatherBot Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        

client = MyClient()
client.run('MTAwOTY1OTUwMTkzNjM5NDMwMA.G7-A4t.HC47nJA4FD7YCEv-60kqFlaxYhvyox7GZ2xMRg')
