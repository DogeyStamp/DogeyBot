class Item:
    def __init__(self, itemid, name='',buycost=-1,sellcost=-1,description='',itemType='item',inShop=True):
        self.name = name
        self.itemid = itemid
        self.buycost = buycost
        self.sellcost = sellcost
        self.description = description
        self.itemType = itemType
        self.inShop = inShop
items = [Item("alpha","test badge alpha",-1,-1,"test item to test the inventory. such interest.","collectable",False),
         Item("beta","test badge beta",-1,-1,"test item to test the inventory. such interest.","collectable",False),
         Item("coal","coal",-1,1,"dark powdery rock. such flammable!","ore",False),
         Item("iron","iron",-1,2,"hard stuff.","ore",False),
         Item("copper","copper",-1,3,"hey i found shiny dirt!!","ore",False),
         Item("silver","silver",-1,5,"shiny pebble?!","ore",False),
         Item("platinum","platinum",-1,30,"what?? this is not silver!?","ore",False),
         Item("gold","gold",-1,20,"solid bread. such valuable.","ore",False),
         Item("diamond","diamond",-1,100,"glass??","ore",False),
         Item("legendary","legendary dogecoin",-1,1000,"this is old coin. well preserved. such valuable.","collectable",False),
         Item("epic","epic dogecoin",-1,800,"was a legendary dogecoin but got degraded.","collectable",False),
         Item("rare","rare dogecoin",-1,200,"valuable. only 10000 were ever produced.","collectable",False),
         Item("old","old dogecoin",-1,70,"dogecoin collectors want it.","collectable",False),
         Item("fossil","fossil",-1,3,"oh look a fishy! such interest.","collectable",False),
         Item("bug","ancient bug",-1,1000,"this is scientifically interesting. it definitely won't escape the lab! haha.","collectable",False),
         Item("bomb","bomb",1000,2,"this is a bomb. it should be safe. right??","item",True),
         Item("pliers","pliers",500,50,"lets you cut wires. mainly to defuse bomb. very helpful.","item",True),
         Item("aoww","aowwsteeng sculpture",3500,4000,"honoring the Aus Aowwsteeng fish","collectable",False),
         Item("uranium","uranium",-1,150,"such glow.","ore",False),
         Item("broccoli","broccoli",2,1,"vegetable. such disgust.","collectable",True),
         Item("amethyst","amethyst",-1,1000,"purple ice??","ore",False),
         Item("cobalt","cobalt",-1,25,"such blue.","ore",False),
         Item("dogium","dogium",-1,2500,"such doge. very cool.","ore",False),
         Item("catium","catium",-1,2000,"used for scientific analysis of catters.","ore",False),
         Item("elder","elder rock",-1,5000,"elder rocks are gods. i mean dogs.","ore",False),
         Item("cat","catter portrait",-1,35,"cats suck. such angry.","collectable",False),
         Item("doge rock","doge rock",-1,100,"its a doge rock.","ore",False),
         Item("lavasuit","lava suit",10000,3000,"lets you harvest lava without harm","item",True),
         Item("jackhammer","jackhammer",70000,3000,"can break very solid minerals.","item",True),
         Item("obsidian","obsidian",-1,100,"only the most solid mineral","ore",False),
         Item("hazmat","hazmat suit",100000,1000,"lets you touch... biohazards.","item",True),
         Item("pamphlet","chapstacks soup pamphlet",-1,2,"oh wow this is something about... chapstacks soup. such interest. mythical properties?","collectable",False),
         Item("lava","lava orb",-1,50,"wow this is hot please don't touch me","ore",False)]
dic = {}
itemIds = []
for item in items:
    itemIds.append(item.itemid)
    dic[item.itemid] = item
