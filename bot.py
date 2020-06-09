import discord
import markovify
import random
import dogeystrings
import dogeycmds
import sympy
import datetime
import praw

client = discord.Client()

reddit = praw.Reddit(client_id="E3x53vfG2tSR_A",
                     client_secret="_jioOka6CDeMoFuT49WqMJ4lEmA",
                     user_agent="discord:DogeyBot:v0.1 (by u/DogeyStamp)")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user or message.content.lower()[:4] != "bork":
        return
    try:
        if message.content.lower().find("time") != -1 or message.content.lower().find("date") != -1:
            await message.channel.send(datetime.datetime.now())
            return
        if message.content.lower().find("help") != -1 or message.content.lower().find("halp") != -1:
            await message.channel.send(dogeystrings.helpPrompt)
            return
        if message.content.lower().find("commands") != -1:
            response = ""
            for cmd in dogeycmds.cmds.keys():
               response = response + "\n{0}: {1}".format(cmd, dogeycmds.cmds[cmd][0])
               response = response + "\nUsage: {}".format(dogeycmds.cmds[cmd][1])
            for chunk in [response[i:i+2000] for i in range(0, len(response), 2000)]:
                await message.channel.send(chunk)
            return
        if message.content.lower().find("calculate") != -1 or message.content.lower().find("what's") != -1 or message.content.lower().find("whats") != -1:
            whitelist = ["1","2","3","4","5","6","7","8","9","0","*","+","%","-","/","!","^","(",")"]
            ind = max(message.content.lower().find("calculate"),message.content.lower().find("what's"),message.content.lower().find("whats"))
            eq = ''.join(ch for ch in message.content.lower()[ind:] if ch in whitelist)
            try:
                result = sympy.sympify(eq)
            except Exception:
                await message.channel.send("equals wowie!")
                return
            if len(str(result)) > 6000:
                await message.channel.send("aww. ur result is too chonker!!")
                return
            response = str(sympy.sympify(eq))
            for chunk in [response[i:i+2000] for i in range(0, len(response), 2000)]:
                await message.channel.send(chunk)
            return
        if message.content.lower().find("meme") != -1:
            mems = []
            for submission in reddit.subreddit("doge").hot(limit=30):
                imgEnds = ["png","svg","jpg","jpeg","gif","tiff"]
                for ending in imgEnds:
                    if submission.url.endswith(ending):
                        mems.append([submission.url,submission.title])
            random.shuffle(mems)
            embed=discord.Embed(title=mems[0][1], url=mems[0][0])
            await message.channel.send(embed=embed)

        with open("dogebase.txt",encoding="utf-8") as f:
            text = f.read().split("\n")
            random.shuffle(text)
            text = '\n'.join(text)
        text_model = markovify.Text(text)
        response = text_model.make_sentence()
        if not response:
            response = ''
        responseL = response.split()
        await message.channel.send(' '.join(responseL[:random.randint(10,45)])+"\n"+random.choice(dogeystrings.helpStrs))
        
    except Exception as err:
        await message.channel.send("Oh noes! I has an error: {}".format(err))
    

client.run(dogeystrings.token)
