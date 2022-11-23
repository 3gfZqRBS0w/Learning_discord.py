# This is my first bot discord so I'm learning at the same time 
import discord
from discord.ext import commands
import json
import os
import random





# FOR DEBUGGING #############################################

def get_veriable_name(variable):
    current_file = os.path.basename(__file__)
    with open(current_file, "r") as f:
        for line in f:
            if variable in line:
                return line.split("=")[0].strip()
    
    return None

############################################################

#not finished yet





#intents = discord.Intents.default()
#intents.message_content = True



client = commands.Bot(command_prefix='/', intents=discord.Intents.all())



"""
@client.event
async def on_message(message):
    if (message.content.startswith("Hello")) :
        await client.process_commands(message.channel.send("Hey"))

@client.command()
async def test(ctx, arg1, arg2):
    await ctx.send(f'You passed {arg1} and {arg2}')
"""




jeu = {}


regle = {
    "Ciseau" : "Pierre",
    "Feuille" : "Ciseau",
    "Pierre" : "Feuille"
}


@client.command()
async def add(ctx, a:int, b:int):
    await ctx.send(f"The calculation result is:\n***{a+b}***")
@client.command()
async def subtract(ctx, a:int, b:int):
    await ctx.send(f"The calculation result is:\n***{a-b}***")
@client.command()
async def multiply(ctx, a:int, b:int):
    await ctx.send(f"The calculation result is:\n***{a*b}***")
@client.command()
async def devide(ctx, a:int, b:int):
    await ctx.send(f"The calculation result is:\n***{a/b}***")




@client.command()
async def jouonsAuPierreFeuilleCiseau(message) :
    await message.channel.send("C'est d'accord, jouons au Pierre Feuille Ciseau !\nEn trois manche, je te laisse commencer.\nPour jouer il suffit d'écrire sur le channel soit Ciseau, Feuille ou Pierre.")
    # Création de la partie
    jeu[message.author] = {
        "me_score" : 0,
        "bot_score" : 0,
        "round" : 0,
        "channel" : message.channel.id
    }
        





@client.listen('on_message')
async def on_message(message) :
    if message.author != client.user :
        if (message.author in jeu.keys()) :
            if (jeu[message.author]["channel"] == message.channel.id ) :
                bot = random.choice(list(regle.values()))
                if (message.content in regle.values()) :
                    # Traitement du coup
                    jeu[message.author]["round"] += 1
                    await message.channel.send("Mon coup est " + str(bot))
                    if ( bot == message.content ) :
                        await message.channel.send("Égalité")
                    elif ( message.content == regle[bot] ) :
                        jeu[message.author]["me_score"] += 1
                        await message.channel.send("Tu as gagné")
                    else :
                        jeu[message.author]["bot_score"] += 1
                        await message.channel.send("Tu as perdu")
                    # Fin de la partie 
                    if (jeu[message.author]["round"] >= 3) :
                        if (jeu[message.author]["me_score"] > jeu[message.author]["bot_score"]) :
                            await message.channel.send("Tu m'as battu...")
                        else :
                            if not (jeu[message.author]["me_score"] == jeu[message.author]["bot_score"]) :
                                await  message.channel.send("J'ai gagné haha")
                            else :
                                await message.channel.send("Egalité...")
                        # Fin de la partie on détruit le dictionnaire 
                        del jeu[message.author]
                else :
                    await message.channel.send("Vous n'êtes pas sur le bon channel")

    
                






"""
@client.event
async def on_message(message) :
    if message.author != client.user :
        await message.channel.send("ooo") 

print(type(client))
@client.command()

@client.choices(fruits=[
client.Choice(name='apple', value=1),
client.Choice(name='banana', value=2),
client.Choice(name='cherry', value=3),
])
async def fruit(interaction: discord.Interaction, fruits):
    await interaction.response.send_message(f'Your favourite fruit is {fruits}.')


@client.event
async def on_message(message):
    # simple calculator
    if message.content.startswith('/calc') :
        calc = message.content.split(" ")
        validOperator = ["+", "-", "*","/", "%"]
        try :
            isValidCommand = type(float(calc[1])) is float and calc[2] in validOperator and type(float(calc[3])) is float
        except  :
            isValidCommand = False

        if (isValidCommand) :
            if (calc[2] == "+") :
                res = float(calc[1]) + float(calc[3])
            elif (calc[2] == "-") :
                res = float(calc[1]) - float(calc[3])
            elif (calc[2] == "*") :
                res = float(calc[1]) * float(calc[3])
            elif (calc[2] == "/") :
                res = float(calc[1]) / float(calc[3])
            elif (calc[2] == "%") :
                res = float(calc[1]) % float(calc[3])
            calc[0] = " " 
            await message.channel.send("The result of your request is  :" + " ".join(calc) + " = " + str(res) )
        else :
            await message.channel.send("you can't calculate this way")
            


    if message.author == client.user:
        return
    if message.content.startswith('/isingeneral'):
        if (message.channel.id == 1042555682307715176)  :
            print(type(message.channel.id))
            await message.channel.send("you are in general")
        else :
            print(type(message.channel.id)) 
            await message.channel.send("you not in general")

"""




# Protection du token 

if os.path.exists("config.json") :
    file = json.loads(open("config.json", "r").readline())
    if (file["token"] == "") :
        print("the token must be define in config json")
        quit() ;
    else :
        client.run(file["token"])
else :
    fp = open('config.json', 'w')
    fp.write(json.dumps({"token": ""}))
    fp.close()
    print("the token must be define in config json")
    quit()

