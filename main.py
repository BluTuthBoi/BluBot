import discord
from discord import Member, Client

class MyClient(Client):
    async def on_ready(self):
        activity = discord.Activity(type=discord.ActivityType.watching, name="Your Chats.")
        await self.change_presence(status=discord.Status.online, activity=activity)
        print('Logged on as ' + str(self.user))




token = "Nzc5NjUzMT#Getprank'dbro#A2NzkwOTU3MDg4.X7jqiQ.h_Hk#Idk#QwaOZk-WeUh9Hdk7hhpVKSk"
client_token = token.split{"#"}
bot = MyClient()
bot.run(client_token[0]+client_token[2]+client_token[4])
