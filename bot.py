print("DogeyBot starting...\nThis program is Doge-Approved, and created by DogeyStamp.")
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
import dogeyitems
from math import ceil

def timeStampPrint(toPrint):
    print("[{}] ".format(datetime.datetime.now()) + toPrint)

timeStampPrint("[INFO] Imports successful")

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
timeStampPrint("[INFO] Data retrieval successful")

def saveData():
    with open("save","w", encoding="utf-8") as saveFile:
        saveFile.write(str(save))
        saveFile.close()

async def saveTask():
    try:
        while(True):
            await asyncio.sleep(30)
            saveData()
    except asyncio.CancelledError:
        timeStampPrint("[INFO] Shutdown of data save task successful.")
@client.event
async def on_ready():
    timeStampPrint('[INFO] Login as {0.user} successful.'.format(client))
    client.loop.create_task(saveTask())
@client.event
async def on_message(message):
    try:
        author = message.author.id
        if message.author == client.user or message.content.lower()[:4] != "bork":
            return
        if not save.get(author):
            save[author] = {}
        saveDefaults = {"coins":0,"inventory":{}}
        for default in saveDefaults.keys():
            if not save[author].get(default):
                save[author][default] = saveDefaults[default]
        if "shutdown" in message.content:
            if author == 437654201863241740:
                await message.channel.send("initiating shutdown becuz i am good doggo")
                timeStampPrint("[INFO] Initiating shutdown...")
                saveData()
                timeStampPrint("[INFO] Data saved successfully. Exiting...")
                exit(0)
        if random.randint(1,5) == 1:
            await message.channel.send("\n" + random.choice(dogeystrings.tips))
        cmdDict = collections.OrderedDict([("time","time"),
                    ("commands","commands"),
                    ("date","time"),
                    ("help","help"),
                    ("halp","help"),
                    ("bank","balance"),
                    ("bal","balance"),
                    ("coin","balance"),
                    ("balance","balance"),
                    ("meme","meme"),
                    ("maymay","meme"),
                    ("politic","politic"),
                    ("news","news"),
                    ("quote","quote"),
                    ("calculate","calculate"),
                    ("what's","calculate"),
                    ("inventory","inventory"),
                    ("inv","inventory"),
                    ("whats","calculate"),])
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
            msgCpy = message.content.lower()
            msgCpy = msgCpy.replace("bork","").replace("commands","",1)
            for cmd in dogeycmds.cmds.keys():
                if msgCpy.find(cmd) != -1:
                    embed=discord.Embed(title=cmd,description=dogeycmds.cmds[cmd][0])
                    embed.set_footer(text="bork bork!")
                    embed.add_field(name='usage',value=dogeycmds.cmds[cmd][1])
                    await message.channel.send(embed=embed)
                    return
            for category in dogeycmds.categories:
                if category in message.content.lower():
                    response = ''
                    for cmd in dogeycmds.cmds.keys():
                        if not dogeycmds.cmds[cmd][3] == category:
                            continue
                        response += "`{}` ".format(cmd)
                    embed=discord.Embed(title=category,description=response)
                    embed.set_footer(text="remember to bork before commands!!")
                    await message.channel.send(embed=embed)
                    break
            else:
                embed=discord.Embed(title="Help")
                for category in dogeycmds.categories:
                    embed.add_field(name=category, value="`bork commands {}`".format(category), inline=True)
                embed.set_footer(text="bork bork!")
                await message.channel.send(embed=embed)
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
                extraReward = 50
            elif num >= 900:
                level = 6
                extraReward = 500
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
            mentioned = False
            if len(message.mentions) > 0:
                balUser = message.mentions[0]
                balName = message.mentions[0].name
                mentioned = True
            else:
                balUser = message.author
                balName = message.author.name
            if not save.get(balUser.id):
                await message.channel.send("he brok :)")
                return
            if save[balUser.id]["coins"] == 0:
                if mentioned:
                    await message.channel.send("he brok :)")
                else:
                    await message.channel.send("u brok :(")
            else:
                embed=discord.Embed()
                embed.add_field(name="{}'s balance".format(balName), value=random.choice(dogeystrings.balStrs).format(save[balUser.id]["coins"]), inline=False)
                await message.channel.send(embed=embed)
            return
        if cmd == "inventory":
            embed = discord.Embed(title="{}'s inventory".format(message.author.name))
            nItems = len(save[author]["inventory"].keys())
            if nItems == 0:
                embed.description = 'oof u has no item. such empty.'
                await message.channel.send(embed=embed)
                return
            else:
                embed.description = "{} items. such cool".format(nItems)
            itemList = [item for item in save[author]["inventory"].keys()]
            itemPerPage = 12
            totalPages = ceil(len(itemList)/itemPerPage)
            pageNmb = ''.join([i for i in message.content if i.isdigit()])
            if bool(pageNmb):
                pageNmb = int(pageNmb)-1
            else:
                pageNmb = 0
            if pageNmb+1>totalPages or pageNmb < 0:
                pageNmb = 0
            embed.set_footer(text="page {} out of {}".format(pageNmb+1,totalPages))
            for item in itemList[pageNmb*itemPerPage:(pageNmb+1)*itemPerPage]:
                itemObj = dogeyitems.dic[item]
                if not item in dogeyitems.itemIds:
                    timeStampPrint("[WARN] Invalid item {} found in {}'s inventory, ID {}".format(item,message.author.name,author))
                    continue
                embed.add_field(name="{} - {}".format(itemObj.name,save[author]["inventory"][item]),value="ID: `{1}` - {0}".format(itemObj.itemType,itemObj.itemid),inline=True)
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
        await message.channel.send("oh noes! I has an error, pls tell dogeystamp")
        timeStampPrint("[ERROR] {}".format(err))
    

client.run(dogeytoken.token)