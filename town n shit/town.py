import random

def mely():
    inputt=input("Melyik legyen? ")
    if inputt=="":
        return 1
    else:
        return int(inputt)


def rand(max):
    return random.randint(1,max)


def item_make_rnd(rng):
    item_type.append(random.randint(0,2))

    if rng == "low":
        item_value.append((random.randint(1,25)/100)+1)

    elif rng=="med":
        item_value.append((random.randint(25,60)/100)+1)

    elif rng=="high":
        item_value.append((random.randint(60,120)/100)+1)

    elif rng=="legendary":
        item_value.append((random.randint(150,221)/100)+1)
    
    item_prefix.append(prefixes[rng])

    item_equip.append(0)


def item_delete(index):
    item_equip.pop(index)
    item_prefix.pop(index)
    item_value.pop(index)
    item_type.pop(index)


def equipped_item_dmg(): 
    if van_itemed():
        for i in range(len(item_equip)):
            if item_equip[i] == 1:

                if item_type[i] == 0:
                    return item_value[i]
                else:
                    return 1
    else:
        return 1

def equipped_item_df():
    if van_itemed():
        for i in range(len(item_equip)):
            if item_equip[i] == 1:

                if item_type[i] == 1:
                    return item_value[i]
                else:
                    return 1
    else:
        return 1

def equipped_item_healing():
    if van_itemed():
        for i in range(len(item_equip)):
            if item_equip[i] == 1:

                if item_type[i] == 2:
                    return item_value[i]
                else:
                    return 1
    else:
        return 1


def upgrade(prefix,index): #monstereknél egy kis chance hogy egyel jobb rarity-t kapjunk

    if prefix=="elfogadható":
        item_prefix[index]="jó"
        item_value[index]=(random.randint(25,60)/100)+1

    elif prefix=="jó":
        item_prefix[index]="kiváló"
        item_value[index]=(random.randint(60,120)/100)+1

    elif prefix=="kiváló" and rand(2):
        item_prefix[index]="legendás"
        item_value[index]=(random.randint(150,221)/100)+1
    

def money_from_item_sale(itemValue):
    return round(itemValue*9,1)


def van_itemed():
    if len(item_type)!=0:
        return True


    
item_type=[] #0 sword / 1 shield / 2 heal
item_value=[] #pl ha 1.25 akkor type alapján vagy 1.25-ös szorzó dmg-re, vagy 1.25-ös szorzó df-re
item_equip=[] #0 nincs equippelve / 1 equippelve van
item_prefix=[]

types={
    0:"kard",
    1:"pajzs",
    2:"saláta"
}

prefixes={
    "low":"elfogadható",
    "med":"jó",
    "high":"kiváló",
    "legendary":"legendás"
    }

fasszopo_magyar_helyesiras={
    "kard":"kardot",
    "pajzs":"pajzsot",
    "saláta":"salátát"
}
fasszopo_magyar_helyesiras2={
    "kard":"kardod",
    "pajzs":"pajzsod",
    "saláta":"salátád"
}



#alap adatok:
'''
money=0
dmg=3
df=3 #defense

wpn_cost=10 #weapon cost
df_cost=10 #armor cost
'''

statok=[]

with open("cuccok.txt","r") as stats:
    for sor in stats:
        sor=sor.strip()
        statok.append(float(sor))

with open("items.txt","r",encoding='utf-8') as items:
    for sor in items:
        adatok=sor.strip().split(",")
        if adatok!=[""]:
            item_type.append(int(adatok[0]))
            item_value.append(float(adatok[1]))
            item_equip.append(int(adatok[2]))
            item_prefix.append(str(adatok[3]))

money=statok[0]
dmg=statok[1]
df=statok[2] #defense

wpn_cost=statok[3] #weapon cost
df_cost=statok[4] #armor cost


while True:

    hp=100

    with open("cuccok.txt","w") as stats:
        print(money, file=stats)
        print(dmg, file=stats)
        print(df, file=stats)
        print(wpn_cost, file=stats)
        print(df_cost, file=stats)
    
    with open("items.txt","w",encoding='utf-8') as items:
        for i in range(len(item_type)):
            print(item_type[i],",",item_value[i],",",item_equip[i],","+item_prefix[i], file=items)

    print()
    print("minden elmentve, életpontok visszaszerezve!")
    print()
    print("Pénzed:",money,"arany")
    print("-------Város-------")
    print("1. Bolt")
    print("2. Felszerelés")
    print("3. Kaland")
    print("4. Kilépés")
    valasztas=mely()
    print()

    if valasztas==4:
        exit()

    elif valasztas==1:
        bolt=True

        while bolt:
            print("-------Bolt--------")
            print("Pénzed:",money,"arany")
            print("1. Fegyver fejlesztés,",wpn_cost,"aranyba kerül")
            print("2. Páncél fejlesztés,",df_cost,"aranyba kerül")
            print("3. Eladás")
            print("4. Vissza")
            valasztas=mely()
            print()

            if valasztas==1:
                if money>=wpn_cost:
                    dmg+=0.4
                    money=round(money-wpn_cost,1)
                    wpn_cost=round(wpn_cost*1.4,1)
                    print("Fegyver fejlesztve! Mostani sebzési szinted:",dmg, end="")
                    input()
                    print()
                else:
                    input("Nincs elég pénzed!")
                    print()
            
            elif valasztas==2:
                if money>=df_cost:
                    df+=0.4
                    money=round(money-df_cost,1)
                    df_cost=round(df_cost*1.4,1)
                    print("Páncél fejlesztve! Mostani védekezési pontod:",df, end="")
                    input()
                    print()
                else:
                    input("Nincs elég pénzed!")
                    print()
            
            elif valasztas==3:

                if van_itemed():
                    for i in range(len(item_type)):
                        if item_equip[i]==1:
                            print(">", end=" ")
                        print(f"{i+1}. {item_prefix[i]} {types[item_type[i]]}, {item_value[i]}-s szorzói effekt")
                    
                    eladni=input("Melyik legyen?(enter ha semelyik) ")
                    if eladni!="":
                        eladni= int(eladni)-1

                        print(f"\nbiztos hogy el akarod adni {money_from_item_sale(item_value[eladni])} aranyért e {item_prefix[eladni]} {fasszopo_magyar_helyesiras2[ types[ item_type[ eladni]]]}?", end=" ")
                        if input("(i/n) ")=="i":
                            money+=round( money_from_item_sale(item_value[eladni]) ,1)
                            item_delete(eladni)
                    print()

                else:
                    input("Nincsen felszerelésed amit el tudnál adni.")

            else:
                bolt=False


    elif valasztas==2:

        if van_itemed():
            for i in range(len(item_type)):
                if item_equip[i]==1:
                    print(">", end=" ")
                print(f"{i+1}. {item_prefix[i]} {types[item_type[i]]}, {item_value[i]}-s szorzói effekt")

            equip_wich=mely()-1

            for i in range(len(item_equip)):
                item_equip[i]=0

            item_equip[equip_wich]=1
        
        else:
            input("Nincsen felszerelésed.")


    elif valasztas==3:
        kaland=True
        harc=True

        diff=0

        hely=random.choice(["erdőbe","barlangba"])

        print("Sétálsz egy kicsit, és bemész egy",hely+".")

        while kaland:
            
            #-------------------------------------------------------------------------------------#
            #kaland kezdete!!! / gameplay loop

            ossz_enemy=random.randint(diff+1, 3+diff) #hány enemy lesz


            most_enemy=[]
            while len(most_enemy)<ossz_enemy:
                if diff==0:
                    most_enemy.append("goblin")
                else:
                    if rand(10-diff)==1 or rand(10-diff)==2:
                        most_enemy.append("bandita")
                        #meg kell csinálni hogy 10(vagy 9 idk) legyen a max deepness!!(diff)
                        #megvan csinalva
                    else:
                        most_enemy.append("goblin")

            most_enemy.append("Elmenekülés")
                        

            while len(most_enemy)>1:

                print("Körbenézel. van a közeledben:")
                for i in range(len(most_enemy)):
                    print(str(i+1)+".",most_enemy[i])
                #print(str(len(most_enemy)+1)+".","Elmenekülés")

                harcolni=mely()-1
                print()

                ##### enemy statok beállítása #####
                if most_enemy[harcolni]=="goblin":
                    enemy_hp=20
                    enemy_dmg=10
                    enemy_rng="low"
                    hit="goblint"

                elif most_enemy[harcolni]=="bandita":
                    enemy_hp=30
                    enemy_dmg=15
                    enemy_rng="med"
                    hit="banditát"
                ##### enemy statok beállítása #####
                else:
                    input("Elmenekültél.")
                    print()
                    kaland=False
                    harc=False
                    break
                
                enemy_hp=enemy_hp*(diff+1)*0.6
                enemy_dmg=enemy_dmg*(diff+1)*0.6

                while harc:
                    
                    most_df=df #csak azért kell ide is hogy rendesen lehessen védekezni

                    print("----"+most_enemy[harcolni],"harc----")
                    print(most_enemy[harcolni],"élete:",round(enemy_hp,1))
                    print("te életed:",round(hp,1))
                    print()
                    print("1. Ütés")
                    print("2. Védekezés")
                    valasztas=mely()
                    print()

                    if valasztas==1:

                        most_dmg=round(random.uniform(dmg-1,dmg+1),1)
                        if van_itemed():
                            most_dmg=most_dmg*equipped_item_dmg()

                        enemy_hp=enemy_hp-most_dmg
                        print("Megütötted a",hit+"! Kevesebb lett az élete",round(most_dmg,1),"ponttal!", end="")
                        input()

                        if enemy_hp<=0:
                            '''
                            money_aq=random.randint(money_aq-5,money_aq+5)
                            money=money+money_aq
                            print("Megölted az ellenséged, és kaptál",money_aq,"aranyat!", end="")
                            '''
                            if rand(3)!=3:
                                print("Megölted az ellenséged.", end="")
                            else:
                                print("Megölted az ellenséged, és észrevettél egy tárgyat nála!", end="")
                                input()
                                print("kaptál egy ", end="")

                                item_make_rnd(enemy_rng)
                                if rand(4)==1:
                                    upgrade(item_prefix[-1],-1)
                                print(item_prefix[-1],fasszopo_magyar_helyesiras[types[item_type[-1]]], end="")
                                print("!", end="")
                            
                            input()
                            print()
                            most_enemy.pop(harcolni)
                            break

                    else:
                        #most_df=most_df*1.5
                        if van_itemed():
                            most_df=most_df*equipped_item_df()

                        healing=3
                        
                        healing=healing*equipped_item_healing()
                        hp+=healing
                        if most_df!=most_df*equipped_item_df():
                            print("Magad elé tetted a pajzsod, ezzel megnövelve a védekezési pontodat!")
                        input(f"Volt időd enni, ezért feljebb ment az életed {healing} ponttal!")
                    

                    sebzodes=round(random.uniform(enemy_dmg-1,enemy_dmg+1),1)-most_df
                    if sebzodes<0:
                        sebzodes=0
                    hp=hp-sebzodes

                    print("Megütött a",most_enemy[harcolni]+", és szenvedtél",round(sebzodes,1),"pontnyi sebzést!", end="")
                    input()
                    print()

                    if hp<=0:
                        input("Meghaltál. Minden, amit nem vittél vissza a faluba, elveszett.")
                        exit() 
            

            if kaland==True:
                if diff>=9:
                    input("Elérted a végét. Visszamentél a városba.")
                    kaland=False
                    harc=False
                elif input("Vissza mész a városba, vagy tovább mész?(v/t) ")=="v":
                    input("visszamentél a városba.")
                    kaland=False
                    harc=False
                else:
                    diff+=1
                    print()
