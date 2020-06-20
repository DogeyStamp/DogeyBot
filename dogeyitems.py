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
         Item("iron","iron",-1,5,"hard stuff.","ore",False),
         Item("copper","copper",-1,10,"hey i found shiny dirt!!","ore",False),
         Item("silver","silver",-1,20,"shiny pebble?!","ore",False),
         Item("platinum","platinum",-1,40,"what?? this is not silver!?","ore",False),
         Item("gold","gold",-1,30,"solid bread. such valuable.","ore",False),
         Item("diamond","diamond",-1,100,"glass??","ore",False),
         Item("legendary","legendary dogecoin",-1,1000,"this is old coin. well preserved. such valuable.","collectable",False),
         Item("epic","epic dogecoin",-1,800,"was a legendary dogecoin but got degraded.","collectable",False),
         Item("rare","rare dogecoin",-1,400,"valuable. only 10000 were ever produced.","collectable",False),
         Item("old","old dogecoin",-1,300,"dogecoin collectors want it.","collectable",False),
         Item("fossil","fossil",-1,10,"oh look a fishy! such interest.","collectable",False),
         Item("aoww","aowwsteeng sculpture",3500,4000,"honoring the Aus Aowwsteeng fish","collectable",False)
         Item("uranium","uranium",-1,150,"such glow.","ore",False),
         Item("brocolli","brocolli",3,4,"vegetable. such disgust.","collectable",True),
         Item("amethyst","amethyst",-1,1000,"purple ice??","ore",True)
         Item("cobalt","cobalt",-1,25,"such blue.","ore",False),
         Item("cat","catter portrait",-1,110,"cats suck. such angry.","collectable",False),
         Item("doge rock","doge rock",-1,100,"its a doge rock.","ore",False),
         Item("doge rock","doge rock",-1,100,"its a doge rock.","ore",False)]
dic = {}
itemIds = []
for item in items:
    itemIds.append(item.itemid)
    dic[item.itemid] = item