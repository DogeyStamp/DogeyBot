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
              "broccoli":situation("broccoli","??\n+{} broccoli",1,5,'broccoli',-15,15,3,5,":broccoli:"),
              "pamphlet":situation("chapstacks soup pamphlet","wow... i see paper. such interest.\n+{} chapstacks soup pamphlet.",1,2,'pamphlet',-15,15,3,5,":newspaper:"),
              "doge rock":situation("doge rock","i found a doge such wow\n+{} doge rock",1,2,'doge rock',-15,15,3,30),
              "cat":situation("catter portrait","such disgust. i hate catter.\n+{} catter portrait",1,2,'cat',-15,15,3,33,":cat:"),
              "coal":situation("coal","wow such black pebble\n+{} coal",1,5,'coal',-15,100,15,7),
              "iron":situation("iron","wow this is hard\n+{} iron",1,4,'iron',-15,750,7,15),
              "copper":situation("copper","shiny dirt!!\n+{} copper",1,2,'copper',-15,650,12,30),
              "silver":situation("silver","so you're saying this isn't iron?!\n+{} ~~iron~~ silver",1,1,'silver',-15,1300,20,30),
              "cobalt":situation("cobalt","me enjoy blue stuff\n+{} cobalt",1,1,'cobalt',-15,1300,20,30),
              "platinum":situation("platinum","so you're saying this isn't silver?!\n+{} ~~silver~~ platinum",1,1,'platinum',0,1500,20,40),
              "gold":situation("gold","me likes eating solid bread\n+{} ~~solid bread~~ gold",1,2,'gold',700,1300,4,12),
              "diamond":situation("diamond","wow glass\n+{} diamond",1,4,'diamond',700,1500,20,40),
              "old":situation("old dogecoin","wow i want to collect it\n+{} old dogecoins",1,2,'old',100,1500,3,20),
              "rare":situation("rare dogecoin","wow its an antique!! such wow.\n+{} rare dogecoins",1,2,'rare',200,1500,3,80),
              "epic":situation("epic dogecoin","wow its an antique!! only slightly worn. such valuable.\n+{} epic dogecoins",1,2,'epic',400,1500,3,130),
              "legendary":situation("legendary dogecoin","wow its a well preserved antique!! such rare.\n+{} legendary dogecoins",1,2,'legendary',600,1500,3,300),
              "aoww":situation("aowwsteeng sculpture","an aowwsteeng sculpture?? wow\n+1 aowwsteeng sculpture",1,1,'aoww',0,300,1,2500),
              "lava":situation("lava","wow hot stuff. such burn!\n+{} lava orb",1,4,'lava',0,6000,6,2,":fire:", "lavasuit",True,'',True,"omg u burned urself. such ouch! u go surface to hospital."),
              "bomb":situation("bomb","u defuse the bomb using pliers. wow that was dangerous\n+{} bomb",1,2,'bomb',0,700,3,2,":firecracker:", "pliers",True,'',True,"aaaaaaaaaaa run run its gonna explode\n-500 depth",500),
              "uranium":situation("uranium","u sure thats safe??\n+{} uranium",1,5,'uranium',1400,2000,7,10),
              "amethyst":situation("amethyst","how long have i been in this mine?? purple ice??\n+{} amethyst",1,3,'amethyst',2000,4000,4,20),
              "elder":situation("elder rock","is this uranium?? why it glowing?? levitating rock????\n+{} elder rock",1,1,'elder rock',1000,5000,5,40),
              "dogium":situation("dogium","wow this is one of the rarest minerals!!\n+{} dogium",1,2,'dogium',3000,5000,4,40),
              "catium":situation("catium","very disgust. necessary for science tho\n+{} dogium",1,1,'catium',4500,5000,3,10,":pouting_cat:","hazmat",True,'',True,"hecc! its catium! poison. ruun. need hazmat suit.\n-600 depth",600),
              "bug":situation("ancient bug","wow interest. old bug. still alive! in core of planet.\n+{} ancient bugger",1,3,'bug',4000,5000,4,10,":microbe:","hazmat",True,'',True,"aaaaaaaaa run run run the hecc is this\n-500 depth",500),
              "superlava":situation("superlava","",0,0,'lava',0,10000,3,1,":large_orange_diamond:", "",True,'',True,"superlava instantly burns you. aaaaah. go to surface.")}
