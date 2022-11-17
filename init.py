# This is my first bot discord so I'm learning at the same time 
import discord
import os

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
    if os.path.exists("config.json") :
        file = open("config.json", "w").readline()
    else :
        open("config.json", "w").write(json.dumps({"token": ""}))




intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    

@client.event
async def on_message(message):

    # simple calculator
    if message.content.startswith('/calc') :
        calc = message.content.split(" ")
        validOperator = ["+", "-", "*","/", "%"]

        try :
            isValidCommand = type(int(calc[1])) is int and calc[2] in validOperator and type(int(calc[3])) is int
        except  :
            isValidCommand = False

        if (isValidCommand) :
            if (calc[2] == "+") :
                res = int(calc[1]) + int(calc[3])
            elif (calc[2] == "-") :
                res = int(calc[1]) - int(calc[3])
            elif (calc[2] == "*") :
                res = int(calc[1]) * int(calc[3])
            elif (calc[2] == "/") :
                res = int(calc[1]) / int(calc[3])
            elif (calc[2] == "%") :
                res = int(calc[1]) % int(calc[3])
            calc[0] = " " 
            await message.channel.send("The result of your request is  :" + " ".join(calc) + " = " + str(res) )
        else :
            await message.channel.send("you can't calculate this way")
            


    if message.author == client.user:
        return
    if message.content.startswith('/test'):
        if (message.channel.id == 1042555682307715176)  :
            print(type(message.channel.id))
            await message.channel.send("you are in general")
        else :
            print(type(message.channel.id)) 
            await message.channel.send("you not in general")




client.run('TOKEN')
