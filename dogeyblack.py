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
        Message displayed as an example to accept the deal."""

    def __init__(
            self, provider, title,
            desc, success_str, betray_str, costs,
            rewards, betray_chance, chance,
            deal_id, count_min, count_max,
            accept_str):
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


# Each list in this represents a level of trust.
sits = [
    [
        # Trust level 0
        Deal(
            "cat robber", "Museum Robbery",
            "I stole from the Museum of Aowwsteeng, and have come to sell you Aowwsteeng pamphlets at reduced price. I'll give you a pamphlet for 1 dogecoin each. Meow?",
            "Ok I gave you ***{1[1]} pamphlets*** for ***{0[1]} dogecoins***. Don't tell people where this came from. Meow.",
            "Haha I stole your ***{0[1]} coins*** and gave you nothing back meowww",
            [ItemCoins("coin", 1, 1)],
            [ItemCoins("pamphlet", 1, 1)],
            25,
            90,
            "pamphlet",
            1, 121,
            "`bork buy 10 pamphlets from that cat at the black market`"),
        Deal(
            "bone seller", "low price bones",
            "i give bones. please just buy. don't ask how i got them. {0[1]} each. acceptable quality woof bones.",
            "woof woof here's your ***{1[1]} bones*** for ***{0[1]} dogecoins***. please make good use of them",
            "im sorry but i stole ***{0[1]} coins*** from you. woof.",
            [ItemCoins("coin", 240, 260)],
            [ItemCoins("bone", 1, 1)],
            30,
            90,
            "bone",
            1, 21,
            "`bork buy 12 bones at the black market`"),
        Deal(
            "garden doggo", "broccoli",
            "unsanitary broccoli. such delicious. 1 dogecoin per brocolli.",
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
            "highly basic locks for you. {0[1]} dogecoin each.",
            "i actually made this from stolen materials. thank for buy. summary: ***{0[1]} dogecoin*** for ***{1[1]} padlock.***",
            "i am very sorry for betrayal. ***-{0[1]} dogecoin***",
            [ItemCoins("coin", 180, 220)],
            [ItemCoins("lock", 1, 1)],
            20,
            90,
            "lock",
            1, 6,
            "`bork buy a lock from the black market`"),
        Deal(
            "panda", "golden chopsticks",
            "highly valuable golden chopsticks. need {0[1]} chapstacks soup pamphlets in exchange.",
            "these are counterfeit lol ***{0[1]} dogecoin*** for ***{1[1]} chopstick.*** you can sell it full price tho. i also gave you free fortune cookies.",
            "i led you all along there were no chopsticks in the first place ***-{0[1]} dogecoin***",
            [ItemCoins("coin", 400, 700)],
            [ItemCoins("chopstick", 1, 1), ItemCoins("fortune", 2, 4)],
            40,
            5,
            "chopstick",
            1, 6,
            "`bork buy a pair of chopsticks from the black market`")
    ],
    [
        # Trust level 1
    ],
    [
        # Trust level 2
    ],
    [
        # Trust level 3
    ],
    [
        # Trust level 4
    ],
    [
        # Trust level 5
    ],
    [
        # Trust level 6
    ],
    [
        # Trust level 7
    ],
]
