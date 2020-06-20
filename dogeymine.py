class situation:
    def __init__(self, name='',body='',r1=0,r2=0,reward='',d1=0,d2=0, pic=":new_moon:"):
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

situations = [situation("coal","wow such black pebble\n+{} coal",1,5,'coal',-30,30)]