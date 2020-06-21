class situation:
    def __init__(self, name='',body='',r1=0,r2=0,reward='',d1=0,d2=0, peak=1, chance=1, pic=":new_moon:", req='', reqDang=False, reqStr='', dangerous=False,dangerString='',dangerDist=0):
        self.name = name
        self.body = body
        #random threshold for reward numbers
        self.r1 = r1
        self.r2 = r2
        #rewarded item
        self.reward = reward
        #depth threshold for finding items, with occurences most concentrated at the middle
        self.d1 = d1
        self.d2 = d2
        #peak amount of ore per config at depth between d1 and d2
        self.peak = peak
        #when selected with d1, d2, peak, chance is another factor that can eliminate this situation. expressed as the fraction 1 over chance.
        self.chance = chance
        #picture to be displayed when this situation is chosen
        self.pic = pic
        #item required to harvest it
        self.req = req
        #whether not having the required item while harvesting it is dangerous
        self.reqDang = reqDang
        #message displayed when you can't harvest it, dangerString will display instead of this if reqDang is True.
        self.reqStr = reqStr
        #whether this item will set you back (lava)
        self.dangerous = dangerous
        #what it says when it sets you back
        self.dangerString = dangerString
        #the distance it sends you back (0 for all the way to the surface)
        self.dangerDist = dangerDist

situations = {"stone":situation("stone","dig down.",0,0,'coal',0,0,0,0),
              "coal":situation("coal","wow such black pebble\n+{} coal",1,5,'coal',-15,100,15,7),
              "iron":situation("iron","wow this is hard\n+{} iron",1,4,'iron',-15,750,7,15),
              "copper":situation("copper","shiny dirt!!\n+{} copper",1,2,'copper',-15,650,12,30),
              "silver":situation("silver","so you're saying this isn't iron?!\n+{} ~~iron~~ silver",1,1,'silver',-15,1300,20,30),
              "cobalt":situation("cobalt","me enjoy blue stuff\n+{} cobalt",1,1,'cobalt',-15,1300,20,30),
              "platinum":situation("platinum","so you're saying this isn't silver?!\n+{} ~~silver~~ platinum",1,1,'platinum',0,1500,20,40),
              "gold":situation("gold","me likes eating solid bread\n+{} ~~solid bread~~ gold",1,2,'silver',700,1300,4,12),
              "diamond":situation("diamond","wow glass\n+{} diamond",1,4,'diamond',700,1500,20,40),
              "legendary":situation("legendary dogecoin","wow its a well preserved antique!! such rare.\n+{} legendary dogecoins",1,2,'legendary',600,1500,3,250),
              "epic":situation("epic dogecoin","wow its an antique!! only slightly worn. such valuable.\n+{} epic dogecoins",1,4,'epic',400,1500,3,100),
              "rare":situation("rare dogecoin","wow its an antique!! such wow.\n+{} rare dogecoins",1,5,'rare',200,1500,3,50),
              "old":situation("old dogecoin","wow i want to collect it\n+{} old dogecoins",1,5,'old',100,1500,3,20),
              "lava":situation("lava","wow hot stuff. such burn!\n+{} lava orb",1,4,'lava',0,6000,6,2,":fire:", "lavasuit",True,'',True,"omg u burned urself. such ouch! u go surface to hospital.")}