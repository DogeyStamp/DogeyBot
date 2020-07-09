class Situation:
    def __init__(self, name='',body='',r1=0,r2=0,reward='',d1=0,d2=0, peak=1, chance=1, pic=":new_moon:", req='', req_dang=False, req_str='', dangerous=False,danger_string='',danger_dist=0):
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
        self.req_dang = req_dang
        #message displayed when you can't harvest it, dangerString will display instead of this if reqDang is True.
        self.req_str = req_str
        #whether this item will set you back (lava)
        self.dangerous = dangerous
        #what it says when it sets you back
        self.danger_string = danger_string
        #the distance it sends you back (0 for all the way to the surface)
        self.danger_dist = danger_dist

situations = {"stone":Situation("stone","dig down.",0,0,'coal',0,0,0,0),
              "broccoli":Situation("broccoli","??\n+{} broccoli",1,5,'broccoli',-15,15,3,5,":broccoli:"),
              "pamphlet":Situation("chapstacks soup pamphlet","wow... i see paper. such interest.\n+{} chapstacks soup pamphlet.",1,2,'pamphlet',-15,15,3,5,":newspaper:"),
              "doge rock":Situation("doge rock","i found a doge such wow\n+{} doge rock",1,2,'doge rock',-15,15,3,30),
              "cat":Situation("catter portrait","such disgust. i hate catter.\n+{} catter portrait",1,2,'cat',-15,15,3,33,":cat:"),
              "coal":Situation("coal","wow such black pebble\n+{} coal",1,5,'coal',-15,100,15,7),
              "iron":Situation("iron","wow this is hard\n+{} iron",1,4,'iron',-15,750,7,15),
              "copper":Situation("copper","shiny dirt!!\n+{} copper",1,2,'copper',-15,650,12,30),
              "silver":Situation("silver","so you're saying this isn't iron?!\n+{} ~~iron~~ silver",1,1,'silver',-15,1300,20,30),
              "cobalt":Situation("cobalt","me enjoy blue stuff\n+{} cobalt",1,1,'cobalt',-15,1300,20,30),
              "platinum":Situation("platinum","so you're saying this isn't silver?!\n+{} ~~silver~~ platinum",1,1,'platinum',0,1500,20,40),
              "gold":Situation("gold","me likes eating solid bread\n+{} ~~solid bread~~ gold",1,2,'gold',700,1300,4,12),
              "diamond":Situation("diamond","wow glass\n+{} diamond",1,4,'diamond',700,1500,20,40),
              "old":Situation("old dogecoin","wow i want to collect it\n+{} old dogecoins",1,2,'old',100,1500,3,20),
              "rare":Situation("rare dogecoin","wow its an antique!! such wow.\n+{} rare dogecoins",1,2,'rare',200,1500,3,80),
              "epic":Situation("epic dogecoin","wow its an antique!! only slightly worn. such valuable.\n+{} epic dogecoins",1,2,'epic',400,1500,3,130),
              "legendary":Situation("legendary dogecoin","wow its a well preserved antique!! such rare.\n+{} legendary dogecoins",1,2,'legendary',600,1500,3,300),
              "aoww":Situation("aowwsteeng sculpture","an aowwsteeng sculpture?? wow\n+1 aowwsteeng sculpture",1,1,'aoww',0,300,1,2500),
              "lava":Situation("lava","wow hot stuff. such burn!\n+{} lava orb",1,4,'lava',0,6000,6,2,":fire:", "lavasuit",True,'',True,"omg u burned urself. such ouch! u go surface to hospital."),
              "bomb":Situation("bomb","u defuse the bomb using pliers. wow that was dangerous\n+{} bomb",1,2,'bomb',0,700,3,2,":firecracker:", "pliers",True,'',True,"aaaaaaaaaaa run run its gonna explode\n-500 depth",500),
              "uranium":Situation("uranium","u sure thats safe??\n+{} uranium",1,5,'uranium',1400,2000,7,10),
              "amethyst":Situation("amethyst","how long have i been in this mine?? purple ice??\n+{} amethyst",1,3,'amethyst',2000,4000,4,20),
              "elder":Situation("elder rock","is this uranium?? why it glowing?? levitating rock????\n+{} elder rock",1,1,'elder',1000,5000,5,80),
              "obsidian":Situation("obsidian","wow very very hard stuff\n+{} obsidian",1,4,'obsidian',3000,6000,6,2,":white_square_button:", "jackhammer",False,'this is too hard to break. need jackhammer.'),
              "dogium":Situation("dogium","wow this is one of the rarest minerals!!\n+{} dogium",1,2,'dogium',3000,5000,4,40),
              "catium":Situation("catium","very disgust. necessary for science tho\n+{} dogium",1,1,'catium',4500,5000,3,10,":pouting_cat:","hazmat",True,'',True,"hecc! its catium! poison. ruun. need hazmat suit.\n-600 depth",600),
              "bug":Situation("ancient bug","wow interest. old bug. still alive! in core of planet.\n+{} ancient bugger",1,3,'bug',4000,5000,4,10,":microbe:","hazmat",True,'',True,"aaaaaaaaa run run run the hecc is this\n-500 depth",500),
              "superlava":Situation("superlava","",0,0,'lava',0,15000,3,2,":large_orange_diamond:", "",True,'',True,"superlava instantly burns you. aaaaah. go to surface.")}
