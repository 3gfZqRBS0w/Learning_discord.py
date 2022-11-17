# This is my first bot discord so I'm learning at the same time 

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/test'):
        if (message.channel.id == 1042555682307715176)  :
            print(type(message.channel.id))
            await message.channel.send("you are in general")
        else :
            print(type(message.channel.id)) 
            await message.channel.send("you not in general")



client.run('MTA0MjU1NDQyODk3ODM2ODU1Mg.GiXW5n.CQ_8cv-gx7iNbYWmrv86nCO_9n4cGOKrZJMopQ')
