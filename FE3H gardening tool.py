import math

class Produce:
    def __init__(self,name,rank,grade,top,bottom):
        self.name=name
        self.rank=rank
        self.grade=grade
        self.top=top
        self.bottom=bottom

class Booster:
    def __init__(self,name,seeds):
        self.name=name
        self.seeds=seeds
    
SCORETOP=(0,21)
SCOREBOT=(10,31)

MIXEDHERB=Produce("Mixed Herb Seeds",27,1,('Mixed Herb Seeds','Carrot','Northern Fodlan Seeds','Chickpeas','Cabbage'),('Western Fodlan Seeds','Tomato','Northern Fodlan Seeds','Daffodil','Chickpeas'))
WFODLAN=Produce('Western Fodlan Seeds',9,1,("Western Fodlan Seeds","Noa Fruit",'Southern Fodlan Seeds','Blue Flower Seeds','Carrot'),('Root Vegetable Seeds','Noa Fruit','Southern Fodlan Seeds','Sunflower','Onion'))
ROOTVEG=Produce("Root Vegetable Seeds",49,1,('Root Vegetable Seeds','Tomato','Morfis Seeds','Purple Flower Seeds','Chickpeas'),('Blue Flower Seeds','Peach Currant','Morfis Seeds','Violet','Turnip'))
VEGS=Produce('Vegetable Seeds',33,1,('Noa Fruit','Onion','Albinean Seeds','Magdred Kirsch','Carrot'),('Nordsalat Seeds','Verona','Albinean Seeds','Lily of the Valley','Onion'))
NFODLAN=Produce('Northern Fodlan Seeds',53,2,('Northern Fodlan Seeds','Morfis Plum','Morfis Seeds','White Flower Seeds','Chickpeas'),('Southern Fodlan Seeds','Chickpeas','Morfis Seeds','Rose','Turnip'))
MRFPLUM=Produce('Morfis-Plum Seeds',18,4,('Morfis Plum','Morfis Plum','Eastern Fodlan Seeds','Purple Flower Seeds','Turnip'),('Nordsalat Seeds','Magdred Kirsch','Eastern Fodlan Seeds','Forget-me-nots','Zanado Treasure Fruit'))
SFODLAN=Produce('Southern Fodlan Seeds',37,2,('Southern Fodlan Seeds','Turnip','Morfis Plum','Yellow Flower Seeds','Magdred Kirsch'),('Verona','Peach Currant','Morfis Plum',"Baby's Breath",'Chickpeas'))
MORFIS=Produce("Morfis Seeds", 23,2,('Morfis Seeds','Albinean Berries','Tomato','Green Flower Seeds','Peach Currant'),('Magdred Kirsch','Carrot','Tomato','Anemone','Onion'))
NORDSALAT=Produce("Nordsalat Seeds",3,4,('Nordsalat','Nordsalat','Angelica Seeds','Pale-Blue Flower Seeds','Magdred Kirsch'),('Ailell Grass','Angelica','Angelica Seeds','Daffodil','Turnip'))
BOA=Produce("Boa-Fruit Seeds",31,5,('Boa Fruit','Boa Fruit','Zanado Treasure Fruit','Red Flower Seeds','Onion'),('Angelica Seeds','Zanado Treasure Fruit','Mixed Herb Seeds','Sunflower','Cabbage'))
ALBINEAN=Produce("Albinean Seeds", 20,2,('Albinean Seeds','Carrot','Tomato','White Flower Seeds','Turnip'),('Albinean Berries','Chickpeas','Tomato','Violet','Carrot'))
EFODLAN=Produce('Eastern Fodlan Seeds',42,2,('Eastern Fodlan Seeds','Tomato','Nordsalat Seeds','Blue Flower Seeds','Cabbage'),('Albinean Berries','Verona','Nordsalat','Pitcher Plant','Chickpeas'))
ANGELICA=Produce("Angelica Seeds",34,5,('Angelica','Angelica','Ailell Grass','Yellow Flower Seeds','Chickpeas'),('Boa-Fruit Seeds','Ailell Grass','Western Fodlan Seeds','Lily','Turnip'))
MIXEDFRT=Produce('Mixed Fruit Seeds', 44,1,('Mixed Fruit Seeds','Northern Fodlan Seeds','Eastern Fodlan Seeds','Green Flower Seeds','Onion'),('Northern Fodlan Seeds','Noa Fruit','Eastern Fodlan Seeds','Lily of the Valley','Cabbage'))
REDFLWR=Produce('Red Flower Seeds', 24, 3,('Daffodil','Onion','Blue Flower Seeds','Albinean Seeds','Rose'),('Rose','Mixed Herb Seeds','Albinean Seeds','Nordsalat','Magdred Kirsch'))
WHTFLWR=Produce('White Flower Seeds', 5, 3,('Sunflower','Southern Fodlan Seeds','Purple Flower Seeds','Turnip','Daffodil'),('Daffodil','Vegetable Seeds','Western Fodlan Seeds','Morfis-Plum Seeds','Boa Fruit'))
BLUFLWR=Produce('Blue Flower Seeds', 38, 3,('Violet','Chickpeas','Yellow Flower Seeds','Eastern Fodlan Seeds','Forget-me-nots'),('Forget-me-nots','Root Vegetable Seeds','Eastern Fodlan Seeds','Morfis-Plum Seeds','Nordsalat'))
PURPFLWR=Produce('Purple Flower Seeds', 16, 3,('Pitcher Plant','Cabbage','Green Flower Seeds','Mixed Herb Seeds','Violet'),('Lavender','Western Fodlan Seeds','Morfis Seeds','Eastern Fodlan Seeds','Albinean Berries'))
YELLFLWR=Produce('Yellow Flower Seeds', 55, 3,('Carnation','Morfis Seeds','Pale-Blue Flower Seeds','Onion','Sunflower'),('Sunflower','Northern Fodlan Seeds','Southern Fodlan Seeds','Boa-Fruit Seeds','Mixed Fruit Seeds'))
GREENFLWR=Produce("Green Flower Seeds",10,3,('Lily','Zanado Fruit','Red Flower Seeds','Cabbage','Pitcher Plant'),('Pitcher Plant','Root Vegetable Seeds','Eastern Fodlan Seeds','Tomato','Morfis Plum'))
PALEBLUFLWR=Produce("Pale-Blue Flower Seeds",1,3,('Lily of the Valley','Northern Fodlan Seeds','White Flower Seeds','Turnip','Anemone'),('Forget-me-nots','Mixed Fruit Seeds','Northern Fodlan Seeds','Tomato','Verona'))

seeds=[MIXEDHERB, WFODLAN, ROOTVEG, VEGS, NFODLAN, MRFPLUM, SFODLAN, MORFIS, NORDSALAT, BOA, ALBINEAN, EFODLAN, ANGELICA, MIXEDFRT, REDFLWR, WHTFLWR, BLUFLWR, PURPFLWR, YELLFLWR, GREENFLWR, PALEBLUFLWR]


HP=Booster('Fruit of Life',(WFODLAN,BLUFLWR))
STR=Booster('Rocky Burdock',(MIXEDHERB,ANGELICA,PURPFLWR))
MAG=Booster('Premium Magic Herbs',(SFODLAN,YELLFLWR))
DEX=Booster('Ailell Pomegranite',(MRFPLUM,MORFIS,GREENFLWR))
SPD=Booster('Speed Carrot',(NORDSALAT,PALEBLUFLWR))
LCK=Booster('Miracle Bean',(BOA,MIXEDFRT))
DEF=Booster('Ambrosia',(ROOTVEG,EFODLAN))
RES=Booster('White Verona',(VEGS,REDFLWR))
CHA=Booster('Golden Apple',(NFODLAN,ALBINEAN,WHTFLWR))

boosters=[HP,STR,MAG,DEX,SPD,LCK,DEF,RES,CHA]

itemset=set()
boosterlist=list()
for seed in seeds:
    itemset.update(seed.top)
    itemset.update(seed.bottom)

for stat in boosters:
    boosterlist.append(stat.name)
        

def sort(seeds,item):
    tops=list()
    bots=list()
    for seed in seeds:
        if seed.top.count(item)>0:
            tops.append(seed)
        if seed.bottom.count(item)>0:
            bots.append(seed)
    return (tops,bots)

def Score(seed1,am1,seed2=EFODLAN,am2=0):
    A=-5*((am1*seed1.rank+am2*seed2.rank)%12)
    B=math.floor(.8*(am1*seed1.grade+am2*seed2.grade))
    score=A+B
    return score

def topCombos(seeds,item):
    print("TOPS:")
    for i in range(1,6):
        for j in range(0, min(i,6-i)):
            for seed1 in seeds:
                for seed2 in seeds:
                    if SCORETOP[0] < Score(seed1,i,seed2,j) and Score(seed1,i,seed2,j) < SCORETOP[1]:
                        n=4-2*(seed1.top.count(item)+seed2.top.count(item))+(seed1.bottom.count(item)+seed2.bottom.count(item))
                        if seed1==seed2:
                            if j==0:
                                for k in range(n):
                                    print("*",end="")
                                print(i," ",seed1.name)
                        else:
                            if j>0:
                                for k in range(n):
                                    print("*",end="")
                                print(i," ",seed1.name," + ",j," ",seed2.name)

def botCombos(seeds,item):
    print("BOTTOMS:")
    for i in range(1,6):
        for j in range(0, min(i+1,6-i)):
            for seed1 in seeds:
                for seed2 in seeds:
                    if SCOREBOT[0] < Score(seed1,i,seed2,j) and Score(seed1,i,seed2,j) < SCOREBOT[1]:
                        n=4-2*(seed1.bottom.count(item)+seed2.bottom.count(item))+(seed1.top.count(item)+seed2.top.count(item))
                        if seed1==seed2:
                            if j==0:
                                for k in range(n):
                                    print("*",end="")
                                print(i," ",seed1.name)
                        else:
                            if j>0:
                                for k in range(n):
                                    print("*",end="")
                                print(i," ",seed1.name," + ",j," ",seed2.name)

def statCombos(stat):
    for i in range(1,6):
        for j in range(0,min(i+1,6-i)):
            for seed1 in stat.seeds:
                for seed2 in stat.seeds:
                    if SCORETOP[0] < Score(seed1,i,seed2,j) and Score(seed1,i,seed2,j) < SCOREBOT[1]:
                        if seed1==seed2:
                            if j==0:
                                print(i," ",seed1.name)
                        else:
                            if j>0:
                                print(i," ",seed1.name," + ",j," ",seed2.name)                        

def getCombos(item):
    if item in itemset:
        mytup=sort(seeds,item)
        topCombos(mytup[0],item)
        botCombos(mytup[1],item)
    else:
        if boosterlist.count(item)>0:
            statCombos(stat)
        else:
            print('Item not found')
on=True
while on:
    print("What do you want to grow?")                   
    item=input()
    getCombos(item)
    print("Press enter to run again or type 'exit' to quit")
    if input()=='exit':
        on=False









                   
