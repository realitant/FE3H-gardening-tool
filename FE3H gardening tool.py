import math

class Produce:
    def __init__(self,name,rank,grade,top1,bottom1,top2,bottom2,top3,bottom3):
        self.name=name
        self.rank=rank
        self.grade=grade
        self.top2=top2
        self.bottom2=bottom2
        self.top3=top3
        self.bottom3=bottom3
        self.top=[top1,top2,top3]
        self.bottom=[bottom1,bottom2,bottom3]

class Booster:
    def __init__(self,name,seeds):
        self.name=name
        self.seeds=seeds
    
SCORETOP=((-81,-20,0),(-59,-7,23))
SCOREBOT=((-60,-20,10),(-39,13,33))
MINMAX=(((-68,-48),(-47,-28)),((-27,-8),(-7,12)),((13,22),(23,32)))
TOP=(.7,.7,.6)
BOT=(.8,.6,.7)

AMOUNT=[[5.5,6.5,7.5,8.5,9.5],
        [6,7,8,9,10],
        [7,8,9,10,11],
        [8,9,10,11,12],
        [9,10,11,12,13],
        [10,11,12,13,14],
        [11,12,13,14,15]]

def getAmount(am1,clevel,am2=0):
    return AMOUNT[clevel][am1+am2-1]
    
    

MIXEDHERB=Produce("Mixed Herb Seeds",27,1,
                  ('Weeds','Weeds','Onion','Mixed Herb Seeds','Mixed Herb Seeds'),
                  ('Mixed Herb Seeds','Mixed Herb Seeds','Turnip','Cabbage','Peach Currant'),
                  ('Mixed Herb Seeds','Albinean Berries','Turnip','Turnip','Mixed Fruit Seeds'),
                  ('Mixed Herb Seeds','Peach Currant','Turnip','Yellow Flower Seeds','Mixed Fruit Seeds'),
                  ('Mixed Herb Seeds','Carrot','Northern Fodlan Seeds','Chickpeas','Cabbage'),
                  ('Western Fodlan Seeds','Tomato','Northern Fodlan Seeds','Daffodil','Chickpeas'))
WFODLAN=Produce('Western Fodlan Seeds',9,1,
                ('Zanado Fruit','Zanado Fruit','Carrot','Western Fodlan Seeds','Western Fodlan Seeds'),
                ('Western Fodlan Seeds','Noa Fruit','Chickpeas','Cabbage','Root Vegetable Seeds'),
                ('Western Fodlan Seeds','Noa Fruit','Noa Fruit','Peach Currant','Vegetable Seeds'),
                ('Western Fodlan Seeds','Noa Fruit','Tomato','Green Flower Seeds','Albinean Berries'),
                ("Western Fodlan Seeds","Noa Fruit",'Southern Fodlan Seeds','Blue Flower Seeds','Carrot'),
                ('Root Vegetable Seeds','Noa Fruit','Southern Fodlan Seeds','Sunflower','Onion'))
ROOTVEG=Produce("Root Vegetable Seeds",49,1,
                ('Weeds','Weeds','Chickpeas','Root Vegetable Seeds','Root Vegetable Seeds'),
                ('Root Vegetable Seeds','Albinean Berries','Tomato','Cabbage','Cabbage'),
                ('Root Vegetable Seeds','Carrot','Cabbage','Peach Currant','Northern Fodlan Seeds'),
                ('Root Vegetable Seeds','Noa Fruit','Cabbage','Pale-Blue Flower Seeds','Northern Fodlan Seeds'),
                ('Root Vegetable Seeds','Tomato','Morfis Seeds','Purple Flower Seeds','Chickpeas'),
                ('Blue Flower Seeds','Peach Currant','Morfis Seeds','Violet','Turnip'))
VEGS=Produce('Vegetable Seeds',33,1,
             ('Dried Vegetables','Dried Vegetables','Chickpeas','Vegetable Seeds','Vegetable Seeds'),
             ('Dried Vegetables','Chickpeas','Onion','Peach Currant','Turnip'),
             ('Vegetable Seeds','Onion','Tomato','Turnip','Mixed Herb Seeds'),
             ('Vegetable Seeds','Peach Currant','Onion','Purple Flower Seeds','Noa Fruit'),
             ('Noa Fruit','Onion','Albinean Seeds','Magdred Kirsch','Carrot'),
             ('Nordsalat Seeds','Verona','Albinean Seeds','Lily of the Valley','Onion'))
NFODLAN=Produce('Northern Fodlan Seeds',53,2,
                ('Dried Vegetables','Dried Vegetables','Onion','Northern Fodlan Seeds','Northern Fodlan Seeds'),
                ('Northern Fodlan Seeds','Tomato','Chickpeas','Mixed Fruit Seeds','Mixed Fruit Seeds'),
                ('Northern Fodlan Seeds','Carrot','Noa Fruit','Mixed Fruit Seeds','Root Vegetable Seeds'),
                ('Northern Fodlan Seeds','Peach Currant','Noa Fruit','Yellow Flower Seeds','Albinean Berries'),
                ('Northern Fodlan Seeds','Morfis Plum','Morfis Seeds','White Flower Seeds','Chickpeas'),
                ('Southern Fodlan Seeds','Chickpeas','Morfis Seeds','Rose','Turnip'))
MRFPLUM=Produce('Morfis-Plum Seeds',18,4,
                ('Zanado Fruit','Zanado Fruit','Peach Currant','Noa Fruit','Morfis-Plum Seeds'),
                ('Zanado Fruit','Morfis-Plum Seeds','Morfis Plum','Morfis Plum','Peach Currant'),
                ('Morfis-Plum Seeds','Peach Currant','Noa Fruit','Morfis Plum','Morfis Plum'),
                ('Morfis-Plum Seeds','Tomato','Morfis Plum','Morfis Plum','Albinean Seeds'),
                ('Morfis Plum','Morfis Plum','Eastern Fodlan Seeds','Purple Flower Seeds','Turnip'),
                ('Nordsalat Seeds','Magdred Kirsch','Eastern Fodlan Seeds','Forget-me-nots','Zanado Treasure Fruit'))
SFODLAN=Produce('Southern Fodlan Seeds',37,2,
                ('Weeds','Weeds','Carrot','Southern Fodlan Seeds','Southern Fodlan Seeds'),
                ('Southern Fodlan Seeds','Turnip','Peach Currant','Cabbage','Western Fodlan Seeds'),
                ('Southern Fodlan Seeds','Turnip','Cabbage','Peach Currant','Northern Fodlan Seeds'),
                ('Southern Fodlan Seeds','Turnip','Verona','Red Flower Seeds','Magdred Kirsch'),
                ('Southern Fodlan Seeds','Turnip','Morfis Plum','Yellow Flower Seeds','Magdred Kirsch'),
                ('Verona','Peach Currant','Morfis Plum',"Baby's Breath",'Chickpeas'))
MORFIS=Produce("Morfis Seeds", 23,2,
               ('Weeds','Weeds','Turnip','Morfis Seeds','Turnip'),
               ('Morfis Seeds','Morfis Seeds','Carrot','Turnip','Mixed Fruit Seeds'),
               ('Morfis Seeds','Morfis Seeds','Peach Currant','Chickpeas','Vegetable Seeds'),
               ('Morfis Seeds','Carrot','Turnip','White Flower Seeds','Vegetable Seeds'),
               ('Morfis Seeds','Albinean Berries','Tomato','Green Flower Seeds','Peach Currant'),
               ('Magdred Kirsch','Carrot','Tomato','Anemone','Onion'))
NORDSALAT=Produce("Nordsalat Seeds",3,4,
                  ('Dried Vegetables','Verona','Carrot','Nordsalat Seeds','Nordsalat Seeds'),
                  ('Dried Vegetables','Nordsalat Seeds','Chickpeas','Nordsalat','Nordsalat'),
                  ('Nordsalat Seeds','Carrot','Nordsalat','Nordsalat','Nordsalat'),
                  ('Nordsalat Seeds','Nordsalat','Magdred Kirsch','Verona','Albinean Berries'),
                  ('Nordsalat','Nordsalat','Angelica Seeds','Pale-Blue Flower Seeds','Magdred Kirsch'),
                  ('Ailell Grass','Angelica','Angelica Seeds','Daffodil','Turnip'))
BOA=Produce("Boa-Fruit Seeds",31,5,
            ('Weeds','Weeds','Peach Currant','Boa-Fruit Seeds','Boa-Fruit Seeds'),
            ('Weeds','Boa-Fruit Seeds','Boa Fruit','Boa Fruit','Boa Fruit'),
            ('Boa-Fruit Seeds','Peach Currant','Boa Fruit','Boa Fruit','Boa Fruit'),
            ('Boa-Fruit Seeds','Boa Fruit','Boa Fruit','Boa Fruit','Angelica Seeds'),
            ('Boa Fruit','Boa Fruit','Zanado Treasure Fruit','Red Flower Seeds','Onion'),
            ('Angelica Seeds','Zanado Treasure Fruit','Mixed Herb Seeds','Sunflower','Cabbage'))
ALBINEAN=Produce("Albinean Seeds", 20,2,
                 ('Zanado Fruit','Zanado Fruit','Peach Currant','Albinean Seeds','Albinean Seeds'),
                 ('Albinean Seeds','Chickpeas','Peach Currant','Albinean Berries','Mixed Fruit Seeds'),
                 ('Albinean Seeds','Albinean Seeds','Peach Currant','Albinean Berries','Root Vegetable Seeds'),
                 ('Albinean Seeds','Carrot','Peach Currant','Yellow Flower Seeds','Root Vegetable Seeds'),
                 ('Albinean Seeds','Carrot','Tomato','White Flower Seeds','Turnip'),
                 ('Albinean Berries','Chickpeas','Tomato','Violet','Carrot'))
EFODLAN=Produce('Eastern Fodlan Seeds',42,2,
                ('Weeds','Weeds','Tomato','Eastern Fodlan Seeds','Eastern Fodlan Seeds'),
                ('Eastern Fodlan Seeds','Verona','Onion','Peach Currant','Onion'),
                ('Eastern Fodlan Seeds','Eastern Fodlan Seeds','Onion','Onion','Morfis Seeds'),
                ('Eastern Fodlan Seeds','Peach Currant','Onion','Green Flower Seeds','Morfis Seeds'),
                ('Eastern Fodlan Seeds','Tomato','Nordsalat Seeds','Blue Flower Seeds','Cabbage'),
                ('Albinean Berries','Verona','Nordsalat','Pitcher Plant','Chickpeas'))
ANGELICA=Produce("Angelica Seeds",34,5,
                 ('Weeds','Weeds','Tomato','Angelica Seeds','Angelica Seeds'),
                 ('Weeds','Angelica Seeds','Angelica','Nordsalat','Angelica'),
                 ('Angelica Seeds','Angelica','Magdred Kirsch','Angelica','Angelica'),
                 ('Angelica Seeds','Angelica','Angelica','Angelica','Morfis-Plum Seeds'),
                 ('Angelica','Angelica','Ailell Grass','Yellow Flower Seeds','Chickpeas'),
                 ('Boa-Fruit Seeds','Ailell Grass','Western Fodlan Seeds','Lily','Turnip'))
MIXEDFRT=Produce('Mixed Fruit Seeds', 44,1,
                 ('Zanado Fruit','Zanado Fruit','Peach Currant','Mixed Fruit Seeds','Mixed Fruit Seeds'),
                 ('Mixed Fruit Seeds','Northern Fodlan Seeds','Northern Fodlan Seeds','Peach Currant','Root Vegetable Seeds'),
                 ('Mixed Fruit Seeds','Northern Fodlan Seeds','Peach Currant','Albinean Berries','Root Vegetable Seeds'),
                 ('Mixed Fruit Seeds','Northern Fodlan Seeds','Peach Currant','White Flower Seeds','Morfis Plum'),
                 ('Mixed Fruit Seeds','Northern Fodlan Seeds','Eastern Fodlan Seeds','Green Flower Seeds','Onion'),
                 ('Northern Fodlan Seeds','Noa Fruit','Eastern Fodlan Seeds','Lily of the Valley','Cabbage'))
REDFLWR=Produce('Red Flower Seeds', 24, 3,
                ('Weeds','Weeds','Weeds','Carnation','Red Flower Seeds'),
                ('Weeds','Red Flower Seeds','Yellow Flower Seeds','Rose','Carnation'),
                ('Rose','Rose','Carnation','Lily','White Flower Seeds'),
                ('Daffodil','Lavender','Yellow Flower Seeds','Purple Flower Seeds','Blue Flower Seeds'),
                ('Daffodil','Onion','Blue Flower Seeds','Albinean Seeds','Rose'),
                ('Rose','Mixed Herb Seeds','Albinean Seeds','Nordsalat','Magdred Kirsch'))
WHTFLWR=Produce('White Flower Seeds', 5, 3,
                ('Weeds','Weeds','Weeds','Baby’s Breath','White Flower Seeds'),
                ('Weeds','White Flower Seeds','Green Flower Seeds','Daffodil','Baby’s Breath'),
                ('Daffodil','Baby’s Breath','Lily','Lily of the Valley','Blue Flower Seeds'),
                ('Sunflower','Anemone','Green Flower Seeds','Yellow Flower Seeds','Purple Flower Seeds'),
                ('Sunflower','Southern Fodlan Seeds','Purple Flower Seeds','Turnip','Daffodil'),
                ('Daffodil','Vegetable Seeds','Western Fodlan Seeds','Morfis-Plum Seeds','Boa Fruit'))
BLUFLWR=Produce('Blue Flower Seeds', 38, 3,
                ('Weeds','Weeds','Weeds','Forget-me-nots','Blue Flower Seeds'),
                ('Weeds','Blue Flower Seeds','Pale-Blue Flower Seeds','Anemone','Forget-me-nots'),
                ('Forget-me-nots','Forget-me-nots','Anemone','Rose','Purple Flower Seeds'),
                ('Violet','Lily of the Valley','Pale-Blue Flower Seeds','Green Flower Seeds','Yellow Flower Seeds'),
                ('Violet','Chickpeas','Yellow Flower Seeds','Eastern Fodlan Seeds','Forget-me-nots'),
                ('Forget-me-nots','Root Vegetable Seeds','Eastern Fodlan Seeds','Morfis-Plum Seeds','Nordsalat'))
PURPFLWR=Produce('Purple Flower Seeds', 16, 3,
                 ('Weeds','Weeds','Weeds','Lavender','Purple Flower Seeds'),
                 ('Weeds','Purple Flower Seeds','Red Flower Seeds','Violet','Lavender'),
                 ('Violet','Rose','Lavender','Forget-me-nots','Yellow Flower Seeds'),
                 ('Pitcher Plant','Baby’s Breath','Red Flower Seeds','Pale-Blue Flower Seeds','Green Flower Seeds'),
                 ('Pitcher Plant','Cabbage','Green Flower Seeds','Mixed Herb Seeds','Violet'),
                 ('Lavender','Western Fodlan Seeds','Morfis Seeds','Eastern Fodlan Seeds','Albinean Berries'))
YELLFLWR=Produce('Yellow Flower Seeds', 55, 3,
                 ('Weeds','Weeds','Weeds','Sunflower','Yellow Flower Seeds'),
                 ('Weeds','Yellow Flower Seeds','White Flower Seeds','Sunflower','Sunflower'),
                 ('Sunflower','Anemone','Daffodil','Lily','Green Flower Seeds'),
                 ('Carnation','Rose','White Flower Seeds','Red Flower Seeds','Pale-Blue Flower Seeds'),
                 ('Carnation','Morfis Seeds','Pale-Blue Flower Seeds','Onion','Sunflower'),
                 ('Sunflower','Northern Fodlan Seeds','Southern Fodlan Seeds','Boa-Fruit Seeds','Mixed Fruit Seeds'))
GREENFLWR=Produce("Green Flower Seeds",10,3,
                  ('Weeds','Weeds','Weeds','Pitcher Plant','Green Flower Seeds'),
                  ('Weeds','Green Flower Seeds','Blue Flower Seeds','Pitcher Plant','Pitcher Plant'),
                  ('Pitcher Plant','Pitcher Plant','Rose','Rose','Pale-Blue Flower Seeds'),
                  ('Lily','Violet','Blue Flower Seeds','White Flower Seeds','Red Flower Seeds'),
                  ('Lily','Zanado Fruit','Red Flower Seeds','Cabbage','Pitcher Plant'),
                  ('Pitcher Plant','Root Vegetable Seeds','Eastern Fodlan Seeds','Tomato','Morfis Plum'))
PALEBLUFLWR=Produce("Pale-Blue Flower Seeds",1,3,
                    ('Weeds','Weeds','Weeds','Carnation','Pale-Blue Flower Seeds'),
                    ('Weeds','Pale-Blue Flower Seeds','Purple Flower Seeds','Carnation','Carnation'),
                    ('Anemone','Anemone','Forget-me-nots','Rose','Red Flower Seeds'),
                    ('Lily of the Valley','Pitcher Plant','Purple Flower Seeds','Blue Flower Seeds','White Flower Seeds'),
                    ('Lily of the Valley','Northern Fodlan Seeds','White Flower Seeds','Turnip','Anemone'),
                    ('Forget-me-nots','Mixed Fruit Seeds','Northern Fodlan Seeds','Tomato','Verona'))

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
    for tier in range(3):
        itemset.update(seed.top[tier])
        itemset.update(seed.bottom[tier])

for stat in boosters:
    boosterlist.append(stat.name)

def EV(item,seed1,am1,tier,side,cmax,seed2=EFODLAN,am2=0):
    EV=0
    if side=="top":
        amt=getAmount(am1,cmax,am2=am2)
        prob=(1/(5*(am1+am2)))*(am1*(seed1.top[tier-1].count(item)*TOP[tier-1]+seed1.bottom[tier-1].count(item)*(1-TOP[tier-1]))
                                +am2*(seed2.top[tier-1].count(item)*TOP[tier-1]+seed2.bottom[tier-1].count(item)*(1-TOP[tier-1])))
        EV=amt*prob
    else:
        amt=getAmount(am1,cmax,am2=am2)
        prob=(1/(5*(am1+am2)))*(am1*(seed1.top[tier-1].count(item)*(1-BOT[tier-1])+seed1.bottom[tier-1].count(item)*(BOT[tier-1]))
                                +am2*(seed2.top[tier-1].count(item)*(1-BOT[tier-1])+seed2.bottom[tier-1].count(item)*(BOT[tier-1])))
        EV=amt*prob
    return EV
        
def sort(seeds,item,tier):
    sort=list()
    for seed in seeds:
        if seed.top[tier-1].count(item)>0:
            sort.append(seed)
        else:
            if seed.bottom[tier-1].count(item)>0:
                sort.append(seed)
    return sort

def Score(seed1,am1,seed2=EFODLAN,am2=0):
    A=-5*((am1*seed1.rank+am2*seed2.rank)%12)
    B=math.floor(.8*(am1*seed1.grade+am2*seed2.grade))
    score=A+B
    return score

def sortAlg(option):
    return option[-1]

def Combos(seeds,item):
    options=list()
    for tier in range(1,4):
        goodseeds=sort(seeds,item,tier)
        for i in range(1,6):
            for j in range(0, min(i,6-i)):
                for seed1 in goodseeds:
                    for seed2 in seeds:
                        score=Score(seed1,i,seed2,j)
                        if SCORETOP[0][tier-1] < score and score < SCORETOP[1][tier-1]:
                            minc=max(0,math.ceil((MINMAX[tier-1][0][0]-score)/2))
                            maxc=min(6,math.floor((MINMAX[tier-1][0][1]-score)/2))
                            if seed1==seed2:
                                if j==0:
                                    option=(i,seed1.name,minc,maxc, EV(item,seed1,i,tier,"top",maxc))
                                    options.append(option)
                            else:
                                if j>0:
                                    option=(i,seed1.name,j,seed2.name,minc,maxc,EV(item,seed1,i,tier,"top",maxc,seed2=seed2,am2=j))
                                    options.append(option)
                        if SCOREBOT[0][tier-1]< score and score < SCOREBOT[1][tier-1]:
                            minc=max(0,math.ceil((MINMAX[tier-1][1][0]-score)/2))
                            maxc=min(6,math.floor((MINMAX[tier-1][1][1]-score)/2))
                            if seed1==seed2:
                                if j==0:
                                    option=(i,seed1.name,minc,maxc, EV(item,seed1,i,tier,"bottom",maxc))
                                    options.append(option)
                            else:
                                if j>0:
                                    option=(i,seed1.name,j,seed2.name,minc,maxc, EV(item,seed1,i,tier,"bottom",maxc))
                                    options.append(option)  
    options.sort(key=sortAlg,reverse=True)
    for i in range(1,min(len(options),51)):
        option=options[i-1]
        if len(option)==5:
            print(option[0],option[1], "\tCultivate Level:",option[2],"-",option[3],"\tEV: ",round(option[4],2))
        else:
            print(option[0],option[1],"+",option[2],option[3], "\tCultivate Level:",option[4],"-",option[5],"\tEV: ",round(option[6],2))
    print("See All? ", len(options)-50, " more...(y/n)")
    if input()=='y' and len(options)>51:
        for i in range(51,len(options)):
            option=options[i-1]
            if len(option)==5:
                print(option[0],option[1], "\tCultivate Level:",option[2],"-",option[3],"\tEV: ",round(option[4],2))
            else:
                print(option[0],option[1],"+",option[2],option[3], "\tCultivate Level:",option[4],"-",option[5],"\tEV: ",round(option[6],2))

def getTier(score):
    tier=-1
    side=-1
    if score < SCORETOP[1][0]:
        return (1,0)
    if score < SCOREBOT[1][1]:
        return (1,1)
    if score < SCORETOP[2][0]:
        return (2,0)
    if score < SCOREBOT[2][1]:
        return (2,1)
    if score < SCORETOP[3][0]:
        return (3,0)
    else:
        return (3,1)

def tierScore(tier):
    if tier==(1,0):
        return 1
    if tier==(1,1):
        return 3
    if tier==(2,0):
        return 5
    if tier==(2,1):
        return 10
    if tier==(3,0):
        return 15
    if tier==(3,1):
        return 20

def statCombos(stat,seeds):
    options=list()
    for i in range(1,6):
        for j in range(0,min(i+1,6-i)):
            for seed1 in stat.seeds:
                for seed2 in stat.seeds:
                    score=Score(seed1,i,seed2,j)
                    tier=getTier(score)
                    minc=max(0,math.ceil((MINMAX[tier[0]-1][tier[1]][0]-score)/2))
                    statscore=tierScore(tier)*getAmount(i,6,j)
                    if seed1==seed2:
                        if j==0:
                            option=(i,seed1.name,minc,statscore)
                            options.append(option)
                    else:
                        if j>0:
                            option=(i,seed1.name,j,seed2.name,minc,statscore)
                            options.append(option)
    options.sort(key=sortAlg,reverse=True)
    for option in options:
        if len(option)==4:
            print(option[0],option[1], "\tCultivate Level:", option[2], "+\t\tSCORE:\t", option[3])
        else:
            print(option[0],option[1], "+", option[2],option[3],"\tCultivate Level:", option[4], "+\t\tSCORE:\t", option[5])

def getCombos(item):
    if item in itemset:
        Combos(seeds,item)
    else:
        if boosterlist.count(item)>0:
            statCombos(stat,seeds)
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
