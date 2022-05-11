import os

import discord
client = discord.Client()



@client.event
async def on_ready():
    print("Le bot est prêt !")
    pass

@client.event
async def on_message(message):
    pass

#Reaction diff msg


@client.event
async def on_message(message):
    print(message.content)

@client.event
async def on_message(message):
    if message.content == "Ping":
        await message.channel.send("Pong")

@client.event
async def on_message(message):
    if message.content == "!help":
        await message.channel.send("Voici toutes les commandes disponibles : ")




#new members with permission

default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)

@client.event
async def on_member_join(member):
    print("L'utilisateur {memmber.display_name} a rejoint le serveur !")

@client.event
async def on_member_join(member):
    general_channel = client.get_channel(952964197665357896)
    general_channel.send("Bienvenue sur le serveur {member.display_name} !")



client.run("OTUzMjc5NTUxNzY3NzE5OTc4.YjCQxA.MBFOXevITcePRyKHYiMI5210LP0")
