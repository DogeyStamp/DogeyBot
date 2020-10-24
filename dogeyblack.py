class ItemCoins:
    def __init__(self, item_id, count_min, count_max):
        """Describes a random amount of coins or items.

        Attributes

        item_id: str
            Item id or "coin" for dogecoins
        count_min:
            Minimum random amount of coins/items
        count_max:
            Maximum random amount of coins/items"""

        self.item_id = item_id
        self.count_min = count_min
        self.count_max = count_max


class Deal:
    """Information about black market deals

    Attributes

    provider: str
        Name of organisation/person behind the deal
    title: str
        Name of the deal
    desc: str
        Description of the deal.
    success_str: str
        Message displayed upon successful completion of deal.
    betray_str: str
        Message displayed upon betrayal by the provider.
    costs: ItemCoins list
        List of ItemCoins objects to be given to the provider to
        complete the deal
    rewards: ItemCoins list
        List of ItemCoins objects to be given to the person after
        successful completion of the deal
    betray_chance: float
        Percentage chance that the provider takes the costs and runs
        with the money.
    chance: float
        Percentage chance to get this deal when available
    deal_id: str
        id of the deal, preferably the item id, if it's an item deal.
    count_min: int
        Minimum amount of the same deal you can fulfill.
    count_max: int
        Maximum amount of the same deal you can fulfill.
    accept_str: str
        Message displayed as an example to accept the deal.
    trust_level: int
        Level of trust. Do not set, it is set in this file."""

    def __init__(
            self, provider, title,
            desc, success_str, betray_str, costs,
            rewards, betray_chance, chance,
            deal_id, count_min, count_max,
            accept_str, trust_level=0):
        self.provider = provider
        self.title = title
        self.desc = desc
        self.success_str = success_str
        self.betray_str = betray_str
        self.rewards = rewards
        self.costs = costs
        self.betray_chance = betray_chance
        self.chance = chance
        self.deal_id = deal_id
        self.count_min = count_min
        self.count_max = count_max
        self.accept_str = accept_str
        self.trust_level = trust_level


# Each list in this represents a level of trust.
sits = [
    [
        # Trust level 0
        Deal(
            "robber cat", "Museum Robbery",
            "I stole from the Museum of Aowwsteeng, and have come to sell you Aowwsteeng pamphlets at reduced price. I'll give you a pamphlet for ***1 dogecoin*** each. Meow?",
            "Ok I gave you ***{1[1]} pamphlets*** for ***{0[1]} dogecoins***. Don't tell people where this came from. Meow.",
            "Haha I stole your ***{0[1]} coins*** and gave you nothing back meowww",
            [ItemCoins("coin", 1, 1)],
            [ItemCoins("pamphlet", 1, 1)],
            60,
            90,
            "pamphlet",
            1, 121,
            "`bork buy 10 pamphlets from that cat at the black market`"),
        Deal(
            "bone seller", "low price bones",
            "i give bones. please just buy. don't ask how i got them. ***{0[1]}*** each. acceptable quality woof bones.",
            "woof woof here's your ***{1[1]} bones*** for ***{0[1]} dogecoins***. please make good use of them",
            "im sorry but i stole ***{0[1]} coins*** from you. woof.",
            [ItemCoins("coin", 240, 260)],
            [ItemCoins("bone", 1, 1)],
            50,
            90,
            "bone",
            1, 21,
            "`bork buy 12 bones at the black market`"),
        Deal(
            "garden doggo", "broccoli",
            "unsanitary broccoli. such delicious. ***1 dogecoin*** per brocolli.",
            "please do not report me to government. ***{1[1]} broccoli*** for you. cost ***{0[1]} dogecoins***.",
            "stole ***{0[1]} coins*** from you. if u are optimistic, at least you don't have to eat bad broccoli.",
            [ItemCoins("coin", 1, 1)],
            [ItemCoins("broccoli", 1, 1)],
            20,
            90,
            "broccoli",
            1, 57,
            "`bork buy 14 broccolis from the black market`"),
        Deal(
            "lock doggo", "locks",
            "highly basic locks for you. ***{0[1]} dogecoin*** each.",
            "i actually made this from stolen materials. thank for buy. summary: ***{0[1]} dogecoin*** for ***{1[1]} padlock.***",
            "i am very sorry for betrayal. ***-{0[1]} dogecoin***",
            [ItemCoins("coin", 30, 45)],
            [ItemCoins("lock", 1, 1)],
            40,
            90,
            "lock",
            1, 6,
            "`bork buy a lock from the black market`"),
        Deal(
            "panda", "golden chopsticks",
            "highly valuable golden chopsticks. need ***{0[1]} chapstacks soup pamphlets*** in exchange.",
            "these are counterfeit lol ***{0[1]} pamphlet*** for ***{1[1]} chopstick.*** you can sell it full price tho. i also gave you free fortune cookies.",
            "i led you all along there were no chopsticks in the first place ***-{0[1]} pamphlets***",
            [ItemCoins("pamphlet", 400, 700)],
            [ItemCoins("chopstick", 1, 1), ItemCoins("fortune", 2, 4)],
            40,
            5,
            "chopstick",
            1, 6,
            "`bork buy a pair of chopsticks from the black market`")
    ],
    [
        # Trust level 1
        Deal(
            "miner doggo", "tax-free coal",
            "my mine is hidden from the police so it's tax free. ***{0[1]} dogecoin*** for ***{1[1]} coal.***",
            "nice doing business with you. ***{0[1]} dogecoin*** for ***{1[1]} coal.***",
            "the mine was a hoax ***-{0[1]} dogecoin***",
            [ItemCoins("coin", 250, 400)],
            [ItemCoins("coal", 420, 500)],
            50,
            90,
            "coal",
            1, 3,
            "`bork buy a load of coal from the black market`"),
        Deal(
            "miner doggo", "cheap iron",
            "cheap, cheap, labour. don't ask more about it. ***{0[1]} dogecoin*** for ***{1[1]} iron.***",
            "nice doing business with you. ***{0[1]} dogecoin*** for ***{1[1]} iron.***",
            "the deal was a hoax ***-{0[1]} dogecoin***",
            [ItemCoins("coin", 40, 60)],
            [ItemCoins("iron", 100, 100)],
            60,
            70,
            "iron",
            1, 15,
            "`bork buy a load of iron from the black market`")
    ],
    [
        # Trust level 2
        Deal(
            "miner doggo", "cheap diamonds",
            "cheap, cheap, labour. don't ask more about it. ***{0[1]} dogecoin*** for ***{1[1]} diamond.***",
            "nice doing business with you. ***{0[1]} dogecoin*** for ***{1[1]} diamond.***",
            "the deal was a hoax ***-{0[1]} dogecoin***",
            [ItemCoins("coin", 40, 60)],
            [ItemCoins("diamond", 1, 1)],
            50,
            50,
            "diamond",
            1, 3,
            "`bork buy a diamond from the black market`"),
        Deal(
            "bomb doggo", "bombs",
            "i made these bombs. robber cat asked me for them, but i hate cats. ***{0[1]} dogecoin*** for each bombs.",
            "wonder what you will do with these. ***{0[1]} dogecoin*** for ***{1[1]} bombs.***",
            "if you know me well, you'd know i wouldn't risk making illegal bombs. ***-{0[1]} dogecoin***",
            [ItemCoins("coin", 10, 20)],
            [ItemCoins("bomb", 1, 1)],
            50,
            70,
            "bomb",
            1, 1000,
            "`bork buy 10 bombs from the black market`"),
        Deal(
            "defense doggo", "defense items",
            "i stole this guy's defense stuff. i'll offer ***{1[1]} locks, and a safe*** for ***{0[1]} dogecoin***.",
            "hope robber cat won't rob you. to summarise: ***{0[1]} dogecoin*** for ***{1[1]} locks, and a safe***.",
            "robber cat stole the stuff i was going to give you :( ***-{0[1]} dogecoin***",
            [ItemCoins("coin", 300, 320)],
            [ItemCoins("lock", 2, 3), ItemCoins("safe", 1, 1)],
            60,
            70,
            "defense",
            1, 2,
            "`bork buy a set of defense items from the black market`")
    ],
    [
        # Trust level 3
        Deal(
            "miner doggo", "lava",
            "i have some lava you can get. ***{0[1]} dogecoin*** for ***{1[1]} lava orbs.***",
            "***{0[1]} dogecoin*** for ***{1[1]} lava.*** cool.",
            "i don't have a lava suit yet, and lied about the lava. ***-{0[1]} dogecoin***",
            [ItemCoins("coin", 10, 29)],
            [ItemCoins("lava", 1, 1)],
            70,
            70,
            "lava",
            1, 100,
            "`bork buy 10 lava from the black market`"),
        Deal(
            "miner doggo", "obsidian",
            "i managed to get some obsidian during a long mining trip. ***{0[1]} dogecoin*** for ***{1[1]} obsidian pieces.***",
            "***{0[1]} dogecoin*** for ***{1[1]} obsidian.*** why do you want this?",
            "robber cat stole my jackhammer, so i couldn't mine obsidian for you. ***-{0[1]} dogecoin***",
            [ItemCoins("coin", 70, 99)],
            [ItemCoins("obsidian", 1, 1)],
            60,
            70,
            "obsidian",
            1, 100,
            "`bork buy 10 obsidian from the black market`")
    ],
    [
        # Trust level 4
        Deal(
            "scout doggo", "tools",
            "i have some extra tools for robbing people. ***{0[1]} dogecoin*** for ***{1[1]} pliers, {2[1]} crowbar, and {3[1]} bones.***",
            "here are you tools. here is the deal again: ***{0[1]} dogecoin*** for ***{1[1]} pliers, {2[1]} crowbar, and {3[1]} bones.***",
            "i lied to you about the tools, why would a scout try to rob?? such dumb. ***-{0[1]} dogecoin***",
            [ItemCoins("coin", 1000, 2000)],
            [ItemCoins("pliers", 1, 2), ItemCoins(
                "crowbar", 1, 1), ItemCoins("bone", 1, 2)],
            50,
            70,
            "rob",
            1, 2,
            "`bork buy 2 sets of robbing tools from the black market`"),
        Deal(
            "bank doggo", "vault",
            "i will give you the extra vault in the bank i work at for ***{0[1]} dogecoin***.",
            "you spent ***{0[1]} dogecoin*** and got ***1 vault*** and an extra ***{2[1]} dogecoins*** inside the vault.",
            "robber cat stole the vault. ***-{0[1]} dogecoin***",
            [ItemCoins("coin", 3000, 4500)],
            [ItemCoins("vault", 1, 1), ItemCoins("coin", 120, 500)],
            40,
            70,
            "vault",
            1, 1,
            "`bork buy a vault from the black market`"),
        Deal(
            "robber cat", "Coin Collections",
            "Give me a crowbar and I will rob a coin collector's safe. We will split the rewards.",
            "In exchange for your crowbar, I gave you ***{1[1]} old dogecoins, {2[1]} rare dogecoins, and {3[1]} epic dogecoins.***",
            "Your crowbar was broken. I'm not giving it back to you.",
            [ItemCoins("crowbar", 1, 1)],
            [ItemCoins("old", 1, 5), ItemCoins(
                "rare", 1, 2), ItemCoins("epic", 1, 2)],
            80,
            70,
            "coin",
            1, 1,
            "`bork accept the coin robbery at the black market`")  
    ],
    [
        # Trust level 5
        Deal(
            "inventor doggo", "lava suits",
            "i managed to make a lava suit production line with underpaid workers and bad working conditions. ***{0[1]} dogecoin*** dogecoins each.",
            "here is your lava suit. good job saving a bunch of dogecoins compared to the normal 10000 price.",
            "the government broke into my factory and confiscated everything.",
            [ItemCoins("coin", 6000, 8000)],
            [ItemCoins("lavasuit", 1, 1)],
            50,
            70,
            "lavasuit",
            1, 1,
            "`bork buy a lavasuit at the black market`"),
        Deal(
            "science doggo", "ancient bug",
            "so this :microbe: was found in the ground. i stole it from the high security lab and it started duplicating. free bugs! buy them at ***{0[1]} dogecoin*** each.",
            "here` is your bug. thanks for ***{0[1]} dogecoin***.",
            "i dropped my tube with the stuff inside lol. wonder if its safe...",
            [ItemCoins("coin", 700, 800)],
            [ItemCoins("bug", 1, 1)],
            60,
            70,
            "bug",
            10, 15,
            "`bork buy a bug at the black market`")  
    ],
    [
        # Trust level 6
        Deal(
            "omeger", "trademark",
            "omegaa stole my name for his gang but i trademarked it. give ***{0[1]} dogecoin*** for my \"lawyers\" and i will split the 100000 dogecoins he will give me with you.",
            "ok we got his money. it cost ***{0[1]} dogecoin*** and you get ***{1[1]} coins*** back.",
            "our \"lawyers\" failed their job. you lost ***{0[1]} dogecoin***.",
            [ItemCoins("coin", 7000, 11000)],
            [ItemCoins("coin", 49000, 51000)],
            70,
            50,
            "trademark",
            1, 1,
            "`bork accept the trademark deal at the black market`"),
        Deal(
            "builder doggo", "jackhammer",
            "some highly powerful jackhammers stolen from my workplace. ***{0[1]}*** each.",
            "ok here's your jackhammer. have fun overheating in the mines.",
            "robber cat stole the jackhammer. oof -***{0[1]} dogecoin***",
            [ItemCoins("coin",60000, 70000)],
            [ItemCoins("jackhammer", 1, 1)],
            20,
            50,
            "jackhammer",
            1, 1,
            "`bork buy a jackhammer at the black market`"),
        Deal(
            "science doggo", "hazmat suit",
            "these suits were also at that high security lab. wonder what they are used for. ***{0[1]}*** each.",
            "have fun with your suit. it cost ***{0[1]} dogecoin***",
            "the government found out i stole the suits -***{0[1]} dogecoin***",
            [ItemCoins("coin",90000, 100000)],
            [ItemCoins("hazmat", 1, 1)],
            20,
            50,
            "hazmat",
            1, 1,
            "`bork buy a hazmat suit at the black market`")
    ],
    [
        Deal(
            "science doggo", "quarantine",
            "so apparently this \"bug\" was dangerous. if you help me pretend to try and quarantine it by giving me 2 hazmat suits, i will pay you ***{1[1]}***.",
            "have fun with your {1[1]} coins.",
            "the government realised i have no medical experience -***{0[1]} hazmat suit***",
            [ItemCoins("hazmat",2, 2)],
            [ItemCoins("coin", 200000, 205000)],
            20,
            50,
            "quarantine",
            1, 1,
            "`bork accept the quarantine deal at the black market`"),
        Deal(
            "robber cat", "Ultimate Break In",
            "I'm planning on freeing my fellow cats from the high security jail. I need {0[1]} nukes to do it. In exchange, I'll give you some money from the cats.",
            "The cats offered {1[1]} coins for you.",
            "The cats were killed by the explosions. -***{0[1]} nukes***",
            [ItemCoins("nuke",18, 24)],
            [ItemCoins("coin", 240000, 260000)],
            20,
            50,
            "break in",
            1, 1,
            "`bork accept to fund the break in at the black market`")
        # Trust level 7
    ]
]

for level in range(len(sits)):
    for deal in sits[level]:
        deal.trust_level = level
