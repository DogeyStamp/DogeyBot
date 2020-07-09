class Item:
    def __init__(self, item_id, name='',buy_cost=-1,sell_cost=-1,description='',item_type='item',in_shop=True,gift_limit=1):
        self.name = name
        self.item_id = item_id
        self.buy_cost = buy_cost
        self.sell_cost = sell_cost
        self.description = description
        self.item_type = item_type
        self.in_shop = in_shop
        self.gift_limit = gift_limit
items = [Item("alpha","test badge alpha",-1,-1,"test item to test the inventory. such interest.","collectable",False,0),
         Item("beta","test badge beta",-1,-1,"test item to test the inventory. such interest.","collectable",False,1),
         Item("coal","coal",-1,1,"dark powdery rock. such flammable!","ore",False,100),
         Item("iron","iron",-1,2,"hard stuff.","ore",False,50),
         Item("copper","copper",-1,3,"hey i found shiny dirt!!","ore",False,50),
         Item("silver","silver",-1,5,"shiny pebble?!","ore",False,20),
         Item("platinum","platinum",-1,30,"what?? this is not silver!?","ore",False,10),
         Item("gold","gold",-1,20,"solid bread. such valuable.","ore",False,10),
         Item("diamond","diamond",-1,100,"glass??","ore",False,10),
         Item("legendary","legendary dogecoin",-1,1000,"this is old coin. well preserved. such valuable.","collectable",False,1),
         Item("epic","epic dogecoin",-1,800,"was a legendary dogecoin but got degraded.","collectable",False,1),
         Item("rare","rare dogecoin",-1,200,"valuable. only 10000 were ever produced.","collectable",False,2),
         Item("old","old dogecoin",-1,70,"dogecoin collectors want it.","collectable",False,5),
         Item("fossil","fossil",-1,3,"oh look a fishy! such interest.","collectable",False,100),
         Item("bug","ancient bug",-1,1000,"this is scientifically interesting. it definitely won't escape the lab! haha.","collectable",False,1),
         Item("bomb","bomb",1000,2,"this is a bomb. it should be safe. right??","item",True,100),
         Item("pliers","pliers",500,50,"lets you cut wires. mainly to defuse bomb. very helpful.","item",True,0),
         Item("aoww","aowwsteeng sculpture",3500,4000,"honoring the Aus Aowwsteeng fish","collectable",False,1),
         Item("uranium","uranium",-1,150,"such glow.","ore",False,3),
         Item("broccoli","broccoli",2,1,"vegetable. such disgust.","collectable",True,150),
         Item("amethyst","amethyst",-1,1000,"purple ice??","ore",False,1),
         Item("cobalt","cobalt",-1,25,"such blue.","ore",False,4),
         Item("dogium","dogium",-1,2500,"such doge. very cool.","ore",False,1),
         Item("catium","catium",-1,2000,"used for scientific analysis of catters.","ore",False,1),
         Item("elder","elder rock",-1,5000,"elder rocks are gods. i mean dogs.","ore",False,1),
         Item("cat","catter portrait",-1,35,"cats suck. such angry.","collectable",False,5),
         Item("doge rock","doge rock",-1,100,"its a doge rock.","ore",False,2),
         Item("lavasuit","lava suit",10000,3000,"lets you harvest lava without harm","item",True,0),
         Item("jackhammer","jackhammer",70000,3000,"can break very solid minerals.","item",True,0),
         Item("obsidian","obsidian",-1,100,"only the most solid mineral","ore",False,2),
         Item("hazmat","hazmat suit",100000,1000,"lets you touch... biohazards.","item",True,0),
         Item("pamphlet","chapstacks soup pamphlet",-1,2,"oh wow this is something about... chapstacks soup. such interest. mythical properties?","collectable",False,100),
         Item("lava","lava orb",-1,30,"wow this is hot please don't touch me","ore",False,7)]
dic = {}
item_ids = []
for item in items:
    item_ids.append(item.item_id)
    dic[item.item_id] = item
