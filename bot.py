import datetime
import logging
logging.basicConfig(filename='dogeybot.log',format='[%(asctime)s] [%(levelname)s] - %(message)s',level=logging.INFO)
logging.info("DogeyBot starting... This program is Doge Approved. It is created by DogeyStamp.")
try:
    import discord
    import markovify
    import random
    import dogeystrings
    import dogeycmds
    import dogeytoken
    import sympy
    import time
    import praw
    import collections
    import asyncio
    import dogeyitems
    import dogeymine
    from math import ceil, floor, log
except Exception as err:
    logging.critical("Import error: {} Aborting...".format(err))
    exit(-1)

logging.info("Imports successful")

client = discord.Client()

reddit = praw.Reddit(client_id="E3x53vfG2tSR_A",
                     client_secret="_jioOka6CDeMoFuT49WqMJ4lEmA",
                     user_agent="discord:DogeyBot:v0.1 (by u/DogeyStamp)")

save = {}
with open("save","r", encoding="utf-8") as save_file:
    save_file.seek(0)
    new_save = save_file.read()
    save = eval(new_save)
save_file.close()
logging.info("Data retrieval successful")

def item_info(item_obj):
    embed = discord.Embed()
    if not item_obj:
        raise Exception("Attempted to get info for blank item.")
    embed.title = item_obj.name
    if item_obj.in_shop:
        embed.description = "*{}* - ID `{}`\nsells for {} dogecoins.\nbought for {} dogecoins.\n\n**{}**".format(item_obj.item_type,item_obj.item_id,item_obj.sell_cost, item_obj.buycost, item_obj.description)
    else:
        embed.description = "*{}* - ID `{}`\nsells for {} dogecoins.\ncan not be bought. \n\n**{}**".format(item_obj.item_type,item_obj.item_id,item_obj.sell_cost, item_obj.description)
    return embed

def save_data():
    with open("save","w", encoding="utf-8") as save_file:
        save_file.write(str(save))
        save_file.close()

def order_of_magnitude(number):
    if number == 0:
        return 0
    return floor(log(number, 10))

async def save_task():
    try:
        while(True):
            await asyncio.sleep(30)
            save_data()
    except asyncio.CancelledError:
        logging.info("Shutdown of data save task successful.")
@client.event
async def on_ready():
    logging.info('Login as {0.user} successful.'.format(client))
    client.loop.create_task(save_task())
@client.event
async def on_message(message):
    try:
        author = message.author.id
        if message.author == client.user or message.content.lower()[:4] != "bork":
            return
        def create_save(person,is_author=False):
            if not save.get(person):
                save[person] = {}
            save_defaults = {"coins":0,"inventory":{},"cooldown":{},"mine":{}}
            for default in save_defaults.keys():
                if not save[person].get(default):
                    save[person][default] = save_defaults[default]
            if (not save[person].get("joined")) and is_author:
                #Author's first use of the bot
                save[person]["joined"] = time.time()
        create_save(author,True)
        if "shutdown" in message.content:
            if author == 437654201863241740:
                await message.channel.send("initiating shutdown becuz i am good doggo")
                logging.info("Initiating shutdown...")
                save_data()
                logging.info("Data saved successfully. Exiting...")
                exit(0)
        if "cooldown" in message.content:
            if author == 437654201863241740:
                save[437654201863241740]["cooldown"] = {}
                await message.channel.send("cooldown removed")
        if random.randint(1,5) == 1:
            await message.channel.send("\n" + random.choice(dogeystrings.tips))
        cmd_dict = collections.OrderedDict([
                    ("commands","commands"),
                    ("date","time"),
                    ("help","help"),
                    ("buy","buy"),
                    ("share","share"),
                    ("gift","gift"),
                    ("inventory","inventory"),
                    ("inv","inventory"),
                    ("shop","shop"),
                    ("sell","sell"),
                    ("halp","help"),
                    ("time","time"),    
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
                    ("mine","mine"),
                    ("whats","calculate")])
        cmd = ''
        for i in cmd_dict.keys():
            if message.content.lower().find(i) != -1:
                cmd = cmd_dict[i]
                break
        if cmd:
            if save[author]["cooldown"].get(cmd) and time.time() - save[author]["cooldown"][cmd] < dogeycmds.cmds[cmd][2]:
                cooldown_seconds = dogeycmds.cmds[cmd][2]-round(time.time() - save[author]["cooldown"][cmd],2)
                if cooldown_seconds//(60*60*24):
                    await message.channel.send("> " + random.choice(dogeystrings.cool_strs).format(round(cooldown_seconds/(60*60*24),2),"day"))
                    return
                elif cooldown_seconds//(60*60):
                    await message.channel.send("> " + random.choice(dogeystrings.cool_strs).format(round(cooldown_seconds/(60*60),2),"hour"))
                    return
                elif cooldown_seconds//60:
                    await message.channel.send("> " + random.choice(dogeystrings.cool_strs).format(round(cooldown_seconds/60,2),"min"))
                    return
                else:
                    await message.channel.send("> " + random.choice(dogeystrings.cool_strs).format(round(cooldown_seconds,2),"sec"))
                    return
            else:
                save[author]["cooldown"][cmd] = time.time()
        if cmd == 'time':
            await message.channel.send(datetime.datetime.now())
            return
        if cmd == 'help':
            await message.channel.send(dogeystrings.help_prompt)
            return
        if cmd == 'commands':
            msg_cpy = message.content.lower()
            msg_cpy = msg_cpy.replace("bork","").replace("commands","",1)
            for cmd in dogeycmds.cmds.keys():
                if msg_cpy.find(cmd) != -1:
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
                img_ends = ["png","svg","jpg","jpeg","gif","tiff"]
                for ending in img_ends:
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
            await message.channel.send(random.choice(dogeystrings.post_strs))
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
            await message.channel.send(random.choice(dogeystrings.post_strs))
            await message.channel.send(embed=embed)
            await message.channel.send(mems[0][0])
            return
        if cmd == 'quote':
            num = random.randint(1,10000000)
            level = 1
            extra_reward = 0
            if num >= 7000000:
                level = 1
            elif num >= 3000000:
                level = 2
            elif num >= 500000:
                level = 3
            elif num >= 50000:
                level = 4
                extra_reward = 1
            elif num >= 9000:
                level = 5
                extra_reward = 500
            elif num >= 900:
                level = 6
                extra_reward = 5000
            elif num >= 800:
                level = 7
                extra_reward = 50000
            with open("dogeFortune{}.txt".format(level),encoding="utf-8") as f:
                text = f.read().split("%")
                extra_reward_str = ''
                if extra_reward != 0:
                    extra_reward_str = 'bork reward: {} dogecoins'.format(extra_reward)
                    save[author]["coins"] += extra_reward
                await message.channel.send(random.choice(text) + "\nRarity level: ***{0}***\n{1}".format(dogeystrings.rare[level-1],extra_reward_str))
                return
        if cmd == "balance":
            mentioned = False
            if len(message.mentions) > 0:
                bal_user = message.mentions[0]
                bal_name = message.mentions[0].name
                mentioned = True
            else:
                bal_user = message.author
                bal_name = message.author.name
            if not save.get(bal_user.id):
                await message.channel.send("he brok :)")
                return
            if save[bal_user.id]["coins"] == 0:
                if mentioned:
                    await message.channel.send("he brok :)")
                else:
                    await message.channel.send("u brok :(")
            else:
                embed=discord.Embed()
                embed.add_field(name="{}'s balance".format(bal_name), value=random.choice(dogeystrings.bal_strs).format(str(save[bal_user.id]["coins"])), inline=False)
                await message.channel.send(embed=embed)
            return
        if cmd == "inventory":
            for item in dogeyitems.items:
                if item.item_id in message.content.lower() and save[author]["inventory"].get(item.item_id) and save[author]["inventory"].get(item.item_id) > 0:
                    await message.channel.send(embed=item_info(item))
                    return
            embed = discord.Embed(title="{}'s inventory".format(message.author.name))
            items = []
            for item in save[author]["inventory"].keys():
                if not item in dogeyitems.item_ids:
                    logging.warning("Invalid item {} found in {}'s inventory, ID {}".format(item,message.author.name,author))
                else:
                    items.append(item)
            item_list = [item for item in items if save[author]["inventory"][item] > 0]
            if len(item_list) == 0:
                embed.description = 'oof u has no item. such empty.'
                await message.channel.send(embed=embed)
                return
            else:
                embed.description = "{} items. such cool".format(len(item_list))
            item_per_page = 12
            total_pages = ceil(len(item_list)/item_per_page)
            page_nmb = ''.join([i for i in message.content if i.isdigit()])
            if bool(page_nmb):
                page_nmb = int(page_nmb)-1
            else:
                page_nmb = 0
            if page_nmb+1>total_pages or page_nmb < 0:
                page_nmb = 0
            embed.set_footer(text="page {} out of {}".format(page_nmb+1,total_pages))
            for item in item_list[page_nmb*item_per_page:(page_nmb+1)*item_per_page]:
                item_obj = dogeyitems.dic[item]
                if not item in dogeyitems.item_ids:
                    logging.warning("Invalid item {} found in {}'s inventory, ID {}".format(item,message.author.name,author))
                    continue
                embed.add_field(name="{} - {}".format(item_obj.name,save[author]["inventory"][item]),value="ID: `{1}` - {0}".format(item_obj.item_type,item_obj.item_id),inline=True)
            await message.channel.send(embed=embed)
            return
        if cmd == "shop":
            for item in dogeyitems.items:
                if item.item_id in message.content.lower() and item.in_shop:
                    await message.channel.send(embed=item_info(item))
                    return
            else:
                embed = discord.Embed(title="doggo shop",description='henlo! pls buy my stuff')
                itemList = [item for item in dogeyitems.items if item.in_shop]
                item_per_page = 12
                total_pages = ceil(len(item_list)/item_per_page)
                page_nmb = ''.join([i for i in message.content if i.isdigit()])
                if bool(page_nmb):
                    page_nmb = int(page_nmb)-1
                else:
                    page_nmb = 0
                if page_nmb+1>total_pages or page_nmb < 0:
                    page_nmb = 0
                embed.set_footer(text="page {} out of {}".format(page_nmb+1,total_pages))
                for item in item_list[page_nmb*item_per_page:(page_nmb+1)*item_per_page]:
                    embed.add_field(name="{}".format(item.name),value="ID: `{1}` - {0}".format(item.item_type,item.item_id),inline=True)
                await message.channel.send(embed=embed)
                return
        if cmd == "buy":
            for item in dogeyitems.items:
                if item.item_id in message.content.lower() and item.in_shop:
                    quantity = ''.join([i for i in message.content if i.isdigit()])
                    if bool(quantity):
                        quantity = int(quantity)
                    else:
                        quantity = 1
                    cost = quantity * item.buy_cost
                    if save[author]["coins"] - cost >= 0:
                        embed = discord.Embed(title='bought!',description="bought {} {} for {} dogecoins.".format(quantity, item.name, cost))
                        save[author]["coins"] -= cost
                        if save[author]["inventory"].get(item.item_id):
                            save[author]["inventory"][item.item_id] += quantity
                        else:
                            save[author]["inventory"][item.item_id] = quantity
                        await message.channel.send(embed=embed)
                    else:
                        await message.channel.send("aww u not enough money.")
                    return
        if cmd == "sell":
            for item in dogeyitems.items:
                if item.item_id in message.content.lower():
                    quantity = ''.join([i for i in message.content if i.isdigit()])
                    if bool(quantity):
                        quantity = int(quantity)
                    else:
                        quantity = 1
                    if "max" in message.content.lower() or "all" in message.content.lower():
                        if save[author]["inventory"].get(item.item_id) and save[author]["inventory"][item.item_id] > 0:
                            quantity = save[author]["inventory"][item.item_id]
                    cost = quantity * item.sell_cost
                    if save[author]["inventory"].get(item.item_id):
                        if save[author]["inventory"][item.item_id] >= quantity:
                            embed = discord.Embed(title='sold!',description="sold {} {} for {} dogecoins.".format(quantity, item.name, cost))
                            save[author]["coins"] += cost
                            save[author]["inventory"][item.item_id] -= quantity
                            await message.channel.send(embed=embed)
                        else:
                            await message.channel.send("aww u not enough {}.".format(item.name))
                    return
        if cmd == "gift":
            #Knockoff sell code
            if len(message.mentions) > 0:
                gift_user = message.mentions[0]
                create_save(gift_user.id)
                gift_name = message.mentions[0].name
                if not save[gift_user.id].get("joined") or time.time() -  save[gift_user.id]["joined"] < 60*60*24*7:
                    await message.channel.send("hey hey no gib stuff to newb. very bad hooman.")
                    save[author]["cooldown"]["gift"] = 0
                    return
            else:
                await message.channel.send("who this gift for??")
                save[author]["cooldown"]["gift"] = 0
                return
            if time.time() - save[author]["joined"] < 60*60*24*7:
                await message.channel.send("hey u need to wait few days so me can tell ur not a new doggo here thx")
                save[author]["cooldown"]["gift"] = 0
                return
            cleaned_message = message.content.replace(gift_user.mention[2:],"")
            for item in dogeyitems.items:
                if item.item_id in message.content.lower():
                    quantity = ''.join([i for i in cleaned_message if i.isdigit()])
                    if bool(quantity):
                        quantity = int(quantity)
                    else:
                        quantity = 1
                    if "max" in message.content.lower() or "all" in message.content.lower():
                        if save[author]["inventory"].get(item.item_id) and save[author]["inventory"][item.item_id] > 0:
                            quantity = min(save[author]["inventory"][item.item_id],item.gift_limit)
                    if save[author]["inventory"].get(item.item_id):
                        if quantity > item.gift_limit:
                            await message.channel.send("wow. such amount! too much. limit for {} is {}.".format(item.name,item.gift_limit))
                            save[author]["cooldown"]["gift"] = 0
                        elif save[author]["inventory"][item.item_id] >= quantity:
                            embed = discord.Embed(title='given!',description="gave {} {} to {}. what a deal!".format(quantity, item.name, gift_name))
                            save[author]["inventory"][item.item_id] -= quantity
                            if not save[gift_user.id]["inventory"].get(item.item_id):
                                save[gift_user.id]["inventory"][item.item_id] = quantity
                            else:
                                save[gift_user.id]["inventory"][item.item_id] += quantity
                            await message.channel.send(embed=embed)
                            return
                        else:
                            await message.channel.send("aww u not enough {}.".format(item.name))
                            save[author]["cooldown"]["gift"] = 0
                    return
            else:
                save[author]["cooldown"]["gift"] = 0
        if cmd == "share":
            def receive_limit(x):
                return 10**order_of_magnitude(x)+2
            #Knockoff gift code
            if len(message.mentions) > 0:
                share_user = message.mentions[0]
                create_save(share_user.id)
                share_name = message.mentions[0].name
                if not save[share_user.id].get("joined") or time.time() -  save[share_user.id]["joined"] < 60*60*24*7:
                    await message.channel.send("hey hey no gib stuff to newb. very bad hooman.")
                    save[author]["cooldown"]["share"] = 0
                    return
                cleaned_message = message.content.replace(share_user.mention[2:],"")
            else:
                await message.channel.send("who this money for??")
                save[author]["cooldown"]["share"] = 0
                return
            quantity = ''.join([i for i in cleaned_message if i.isdigit()])
            limit = min(receive_limit(save[share_user.id]["coins"]),save[author]["coins"])
            if bool(quantity):
                quantity = int(quantity)
            else:
                await message.channel.send("how much dogecoin tho??")
                save[author]["cooldown"]["share"] = 0
                return
            if time.time() - save[author]["joined"] < 60*60*24*7:
                await message.channel.send("hey u need to wait few days so me can tell ur not a new doggo here thx")
                save[author]["cooldown"]["share"] = 0
                return
            if quantity <= limit:
                if save[author]["coins"] == 0:
                    tax = 0
                else:
                    tax = min(order_of_magnitude(save[author]["coins"])*0.08,0.99999999)
                old_quantity = quantity
                quantity -= tax
                quantity = round(quantity)
                save[author]["coins"] -= quantity
                save[share_user.id]["coins"] += quantity
                if quantity == old_quantity:
                    embed = discord.Embed(title='given!',description="gave {} dogecoins to {}. there was a tax of {}, but we rounded your money amount.".format(quantity, share_name,tax))
                else:
                    embed = discord.Embed(title='given!',description="gave {} dogecoins to {}. there was a tax of {}.".format(quantity, share_name,tax))
                await message.channel.send(embed=embed)
                return
            else:
                await message.channel.send("aww u cant send that much money u can only send {}".format(limit))
                save[author]["cooldown"]["share"] = 0
                return
        if cmd == "mine":
            args = message.content.lower().replace("bork",'').replace("mine","")
            def create_cfg(depth):
                def distribution(d1,d2,depth,peak):
                    if d1 > depth or d2 < depth:
                        return 0
                    center = ceil(abs(d1 + (d1 - d2)/2))
                    if depth <= center:
                        return round(peak * ((depth-d1)/(center-d1)))
                    if depth > center:
                        return round(peak * (abs(depth-d2)/abs(center-d2)))
                cfg = ["stone","stone","stone"]
                #Stone is always default, and gets replaced by other things during the config process
                #The rest is determined in dogeymine
                for sit in dogeymine.situations.keys():
                    if sit == 'stone':
                        continue
                    sit_ob = dogeymine.situations[sit]
                    remaining = distribution(sit_ob.d1,sit_ob.d2,depth,sit_ob.peak)
                    remaining = min(remaining,3)
                    rem_inds = [0,1,2]
                    while remaining > 0 and rem_inds:
                        remaining -= 1
                        if random.randint(1,sit_ob.chance) == 1:
                            ind = random.choice(rem_inds)
                            rem_inds.remove(ind)
                            cfg[ind] = sit
                #this just returns the config, it doesn't perform logic for danger, messages to display, etc.
                return cfg
            if (not save[author]["mine"]) or (save[author]["cooldown"].get(cmd) and (time.time() - save[author]["cooldown"][cmd] > 60*30)):
                #current is the configuration of the mine: stone stone lava, or something
                save[author]["mine"] = {"depth":0,"current":[]}
                cfg = create_cfg(save[author]["mine"]["depth"])
                save[author]["mine"]['current'] = cfg
            embed = discord.Embed(title="{}'s mine".format(message.author.name))
            ind = -1
            if 'm' in args:
                ind = 1
            elif 'r' in args:
                ind = 2
            elif 'l' in args:
                ind = 0
            else:
                embed.description = 'to mine, mine something: left (`l`) right (`r`) or middle (`m`) `bork mine l`, `bork mine r`, `bork mine m`'
            if ind != -1:
                curr_sit = save[author]["mine"]['current']
                sit_obj = dogeymine.situations.get(curr_sit[ind])
                if not sit_obj:
                    raise Exception("Mining situ not found: {}".format(curr_sit))
                if sit_obj.dangerous:
                    def danger():
                        if sit_obj.danger_dist == 0:
                            save[author]["mine"]["depth"] = 0
                        else:
                            save[author]["mine"]["depth"] = max(0,save[author]["mine"]["depth"]-sit_obj.danger_dist)
                        embed.description = sit_obj.danger_string
                    if sit_obj.req != '':
                        if not save[author]['inventory'].get(sit_obj.req):
                            if sit_obj.req_dang:
                                danger()
                            else:
                                save[author]["mine"]["depth"] += random.randint(1,3)
                                embed.description = sit_obj.req_str
                        else:
                            save[author]["mine"]["depth"] += random.randint(1,3)
                            amount = random.randint(sit_obj.r1, sit_obj.r2)
                            embed.description = sit_obj.body.format(amount)
                            if save[author]['inventory'].get(sit_obj.reward):
                                save[author]['inventory'][sit_obj.reward] += amount
                            else:
                                save[author]['inventory'][sit_obj.reward] = amount
                    else:
                        danger()
                elif sit_obj.req != '':
                    if not save[author]['inventory'].get(sit_obj.req):
                        embed.description = sit_obj.req_str
                        embed.title = embed.title + "\n{} depth\n{}".format(save[author]["mine"]["depth"],sit_obj.name)
                        mine_pics = []
                        for curr_sit in save[author]["mine"]['current']:
                            sit_obj = dogeymine.situations.get(curr_sit)
                            if not sit_obj:
                                raise Exception("Mining situ not found: {}".format(curr_sit))
                            mine_pics.append(sit_obj.pic)
                        embed.add_field(name="ur mine",value=' '.join(mine_pics))
                        await message.channel.send(embed=embed)
                        return
                    else:
                        save[author]["mine"]["depth"] += random.randint(1,3)
                        amount = random.randint(sit_obj.r1, sit_obj.r2)
                        embed.description = sit_obj.body.format(amount)
                        if save[author]['inventory'].get(sit_obj.reward):
                            save[author]['inventory'][sit_obj.reward] += amount
                        else:
                            save[author]['inventory'][sit_obj.reward] = amount
                else:
                    save[author]["mine"]["depth"] += random.randint(1,3)
                    amount = random.randint(sit_obj.r1, sit_obj.r2)
                    embed.description = sit_obj.body.format(amount)
                    if save[author]['inventory'].get(sit_obj.reward):
                        save[author]['inventory'][sit_obj.reward] += amount
                    else:
                        save[author]['inventory'][sit_obj.reward] = amount
                embed.title = embed.title + "\n{} depth\n{}".format(save[author]["mine"]["depth"],sit_obj.name)
                save[author]["mine"]['current'] = create_cfg(save[author]["mine"]["depth"])
            mine_pics = []
            for curr_sit in save[author]["mine"]['current']:
                sit_obj = dogeymine.situations.get(curr_sit)
                if not sit_obj:
                    raise Exception("Mining situ not found: {}".format(curr_sit))
                mine_pics.append(sit_obj.pic)
            embed.add_field(name="ur mine",value=' '.join(mine_pics))
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
        response_l = response.split()
        await message.channel.send(' '.join(response_l[:random.randint(10,45)])+"\n"+random.choice(dogeystrings.help_strs))
    except Exception as err:
        await message.channel.send("oh noes! I has an error, pls tell dogeystamp")
        logging.exception("{}\nInput causing error: {}\nAuthor: {}\nAuthor ID: {}".format(err,message.content,message.author.name+"#"+message.author.discriminator,author))
    

client.run(dogeytoken.token)