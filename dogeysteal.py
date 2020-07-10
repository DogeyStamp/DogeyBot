class StealCheck:
    """Information to see if a robber can succesfully bypass a defense.

    Attributes

    no_item: str
        String displayed when robber has none of offense_item.
    success: str
        String shown when robber is successful.
    defense_item: str
        ID of the defense item to bypass.
    defense_consume: bool
        Whether the defense_item should be consumed
        after a robbing.
    offense_item: str
        ID of the item used to bypass the defense.
    offense_min: int
        Miniumum amount of offense_item used.
    offense_max: int
        Maximum amount of offense_item used.
    consume: bool
        Whether the offense_item should be removed when robbing.
    not_enough: str
        String displayed when robber doesn't have enough
        offense_item."""

    def __init__(
        self, no_item,
        success, defense_item,
        offense_item, defense_consume=False,
        offense_min=1, offense_max=1,
        consume=False, not_enough="",
        ):
        self.defense_item = defense_item
        self.offense_item = offense_item
        self.offense_min = offense_min
        self.offense_max = offense_max
        self.consume = consume
        self.no_item = no_item
        self.not_enough = not_enough
        self.defense_consume = defense_consume
        self.success = success
steal_checks=[
            StealCheck(
                no_item="omg is this literally a bunker??",
                not_enough="wth the bunker survived {} nukes",
                success="ok bunker cant survive {} nuke.",
                defense_item="bunker",
                offense_item="nuke",
                offense_max=70,
                offense_min=10,
                consume=True),
            StealCheck(
                no_item="*poke poke* yea this vault is too hard to break",
                not_enough="you bomb the vault with {} bombs but it still not brok",
                success="you bombed the vault with {} bombs and get money inside",
                defense_item="vault",
                offense_item="bomb",
                offense_max=255,
                offense_min=90,
                consume=True),
            StealCheck(
                no_item="wow is money in safe? too secure.",
                success="u pry open safe with crowbar.",
                defense_item="safe",
                offense_item="crowbar"),
            StealCheck(
                no_item="attack doggo bites you. ouch",
                not_enough="doggo ate {} bones but still bite. ouch",
                success="doggo like u after eat {} of your bone.",
                defense_item="attack",
                offense_item="bone",
                offense_max=20,
                offense_min=2,
                consume=True),
            StealCheck(
                no_item="u see padlock. no pliers. aww.",
                success="u destroy lock with pliers. such cheap.",
                defense_item="lock",
                offense_item="pliers",
                defense_consume=True,
                consume=True)
            ]
        