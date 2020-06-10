import discord
import markovify
import random
import dogeystrings
import dogeycmds
import dogeytoken
import sympy
import time
import datetime
import praw
import collections
import asyncio

client = discord.Client()

reddit = praw.Reddit(client_id="E3x53vfG2tSR_A",
                     client_secret="_jioOka6CDeMoFuT49WqMJ4lEmA",
                     user_agent="discord:DogeyBot:v0.1 (by u/DogeyStamp)")

cooldown = {}
save = {}
with open("save","r", encoding="utf-8") as saveFile:
    saveFile.seek(0)
    newSave = saveFile.read()
    save = eval(newSave)
saveFile.close()
print("Data retrieval [ OK ]")

async def shutdown():
    tasks = [task for task in asyncio.Task.all_tasks() if task is not
             asyncio.tasks.Task.current_task()]
    list(map(lambda task: task.cancel(), tasks))
    results = await asyncio.gather(*tasks, return_exceptions=False)

def saveData():
    with open("save","w", encoding="utf-8") as saveFile:
        saveFile.write(str(save))
        saveFile.close()

async def saveTask():
    try:
        while(True):
            await asyncio.sleep(5)
            saveData()
    except asyncio.CancelledError:
        print("Successful shutdown of data save task.")
@client.event
async def on_ready():
    print('Login as {0.user} [ OK ]'.format(client))
    client.loop.create_task(saveTask())
@client.event
async def on_message(message):
    author = message.author.id
    if message.author == client.user or message.content.lower()[:4] != "bork":
        return
    if not save.get(author):
        save[author] = {}
        save[author]["coins"] = 0
    if "shutdown" in message.content:
        if author == 437654201863241740:
            await message.channel.send("initiating shutdown becuz i am good doggo")
            print("Initiating shutdown...")
            saveData()
            print("Data saved successfully. Exiting...")
            await shutdown()
            exit(0)
    try:
        cmdDict = collections.OrderedDict([("time","time"),
                    ("date","time"),
                    ("help","help"),
                    ("halp","help"),
                    ("commands","commands"),
                    ("bank","balance"),
                    ("dogecoin","balance"),
                    ("balance","balance"),
                    ("meme","meme"),
                    ("maymay","meme"),
                    ("politic","politic"),
                    ("news","news"),
                    ("quote","quote"),
                    ("calculate","calculate"),
                    ("what's","calculate"),
                    ("whats","calculate")])
        cmd = ''
        for i in cmdDict.keys():
            if message.content.lower().find(i) != -1:
                cmd = cmdDict[i]
                break
        if cmd:
            if cooldown.get(author):
                if cooldown[author].get(cmd) and time.time() - cooldown.get(author)[cmd] < dogeycmds.cmds[cmd][2]:
                    await message.channel.send("> " + random.choice(dogeystrings.coolStrs).format(round(dogeycmds.cmds[cmd][2]-round(time.time() - cooldown[author][cmd],2),2)))
                    return
                else:
                    cooldown[author][cmd] = time.time()
            else:
                cooldown[author] = {}
                cooldown[author][cmd] = time.time()
        if cmd == 'time':
            await message.channel.send(datetime.datetime.now())
            return
        if cmd == 'help':
            await message.channel.send(dogeystrings.helpPrompt)
            return
        if cmd == 'commands':
            response = ""
            for cmd in dogeycmds.cmds.keys():
               response = response + "\n_***{0}***_: *{1}*".format(cmd, dogeycmds.cmds[cmd][0])
               response = response + "\nUsage: {}".format(dogeycmds.cmds[cmd][1])
            for chunk in [response[i:i+2000] for i in range(0, len(response), 2000)]:
                await message.channel.send(chunk)
            return
        if cmd == 'calculate':
            whitelist = ["1","2","3","4","5","6","7","8","9","0","*","+","%","-","/","!","^","(",")","."]
            ind = max(message.content.lower().find("calculate"),message.content.lower().find("what's"),message.content.lower().find("whats"))
            eq = ''.join(ch for ch in message.content.lower()[ind:] if ch in whitelist)
            if eq == '':
                await message.channel.send("equals wowie!")
                return
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
        if cmd == 'meme':
            mems = []
            for submission in reddit.subreddit("doge").hot(limit=30):
                imgEnds = ["png","svg","jpg","jpeg","gif","tiff"]
                for ending in imgEnds:
                    if submission.url.endswith(ending):
                        mems.append([submission.url,submission.title,submission.permalink,submission.score])
            random.shuffle(mems)
            embed=discord.Embed(title=mems[0][1], url='https://reddit.com'+mems[0][2])
            embed.set_image(url=mems[0][0])
            embed.add_field(name="Upvotes", value="{}".format(mems[0][3]), inline=True)
            await message.channel.send(embed=embed)
            return
        if cmd == 'politic':
            mems = []
            for submission in reddit.subreddit("politics").hot(limit=30):
                mems.append([submission.url,submission.title,submission.permalink,submission.score])
            random.shuffle(mems)
            embed=discord.Embed(title=mems[0][1], url='https://reddit.com'+mems[0][2])
            embed.add_field(name="Upvotes", value="{}".format(mems[0][3]), inline=True)
            await message.channel.send(random.choice(dogeystrings.postStrs))
            await message.channel.send(embed=embed)
            await message.channel.send(mems[0][0])
            return
        if cmd == 'news':
            mems = []
            for submission in reddit.subreddit("news").hot(limit=30):
                mems.append([submission.url,submission.title,submission.permalink,submission.score])
            random.shuffle(mems)
            embed=discord.Embed(title=mems[0][1], url='https://reddit.com'+mems[0][2])
            embed.add_field(name="Upvotes", value="{}".format(mems[0][3]), inline=True)
            await message.channel.send(random.choice(dogeystrings.postStrs))
            await message.channel.send(embed=embed)
            await message.channel.send(mems[0][0])
            return
        if cmd == 'quote':
            num = random.randint(1,10000000)
            level = 1
            extraReward = 0
            if num >= 7000000:
                level = 1
            elif num >= 3000000:
                level = 2
            elif num >= 500000:
                level = 3
            elif num >= 50000:
                level = 4
                extraReward = 1
            elif num >= 9000:
                level = 5
                extraReward = 10
            elif num >= 900:
                level = 6
                extraReward = 100
            elif num >= 800:
                level = 7
                extraReward = 5000
            with open("dogeFortune{}.txt".format(level),encoding="utf-8") as f:
                text = f.read().split("%")
                extraRewardStr = ''
                if extraReward != 0:
                    extraRewardStr = 'bork reward: {} dogecoins'.format(extraReward)
                    save[author]["coins"] += extraReward
                await message.channel.send(random.choice(text) + "\nRarity level: ***{0}***\n{1}".format(dogeystrings.rare[level-1],extraRewardStr))
                return
        if cmd == "balance":
            if save[author]["coins"] == 0:
                await message.channel.send("u brok :(")
            else:
                embed=discord.Embed()
                embed.add_field(name="{}'s balance".format(message.author.name), value=random.choice(dogeystrings.balStrs).format(save[author]["coins"]), inline=False)
                await message.channel.send(embed=embed)
            return
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
    

client.run(dogeytoken.token)