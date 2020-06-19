class Item:
    def __init__(self, itemid, name='',buycost=-1,sellcost=-1,description='',itemType='item',inShop=True):
        self.name = name
        self.itemid = itemid
        self.buycost = buycost
        self.sellcost = sellcost
        self.description = description
        self.itemType = itemType
        self.inShop = inShop
items = [Item("test","test badge",-1,-1,"test item to test the inventory. such interest.","collectable",False)]
dic = {}
itemIds = []
for item in items:
    itemIds.append(item.itemid)
    dic[item.itemid] = item