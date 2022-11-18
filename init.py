# This is my first bot discord so I'm learning at the same time 
import discord
import json
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

