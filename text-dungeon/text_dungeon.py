from __future__ import print_function  
from __future__ import division 
from functools import partial        
import random
import sys
import threading
import time

#Dungeon Game by: Jonas Aigner
#Github Profile: Jonas Aigner
#Core Game by: Horst Jens on Github
#Aktual Development Stage: Alpha, Not Aviable for Download
#Last Modification: 14.12.2018
#Next Paches: More Items
#
#NOTE: THIS GAME IS ONLY PLAYABLE IN GERMAN
#
#THIS GAME IS MADE BY A BEGINNER





Kreislauf = 0                                           #Most of the definitions are useless put I keep them
Ende = 0                                           
looten = "looten"
l = "looten"
schlafen = "schlafen"
s = "s"
aufbleiben = "aufbleiben"
a = "a"
auf = "aufbleiben"
inventar = "inventar"
i = "inventar"
essen = "essen"
trinken = "trinken"
t = "trinken"
e = "essen"
Ja = "Ja"
Nein = "Nein"
tag = 0
time1 = 0
stathung = "stathung"
statdurst = "statdurst"
food_express = "food_express"
water_express = "water_express"
resetstats = "resetstats"
crafting = "crafting"
craften = "craften"
c = "craften"
Stock = "Stock"
Kleinholz = "Kleines Holz"
Schnitzmesser = "Schnitzmesser"
eins = "eins"
zwei = "zwei"
drei = "drei"
Magier = "Magier"
Jaeger = "Jaeger"
Krieger = "Krieger"
Handwerker = "Handwerker"
vertei = 0
verteixx = 0
verteiyy = 0
fightrandom1 = 1
fightrandom2 = 11
ffertig = 0
w = "w"
d = "d"
sch = "sch"
f = "Faehigkeit"
Faehigkeit = "Faehigkeit"
u = ">"
o = "<"
fcount = 0
rcount = 0

# ~ class Fight(threading.Thread):                                          #Fight Mechanic: may never include
    # ~ def __init__(self, r, p="P"):
        # ~ threading.Thread.__init__(self)
        # ~ self.action = r
        # ~ self.pprint = p
        # ~ self.attacks = ["'a'links", "'d'rechts", "'w'oben"]

    # ~ def run(self):
        # ~ if self.action < 10:
            # ~ global verteiyy
            # ~ verteiyy = random.choice(self.attacks)
            # ~ print("Dein Gegner greift " + str(verteiyy) + " an!")
            # ~ print("")
            # ~ print("")
            # ~ global verteixx
            # ~ verteixx = input("Verteitige! >")
        # ~ elif self.action > 10 :
            # ~ time.sleep(1)
            # ~ if verteixx == verteiyy[1]:
                # ~ print("Abgeblockt")
                # ~ global ffertig
                # ~ ffertig = 1
            # ~ else:
                # ~ print("")
                # ~ print("Nicht geblockt! Du bist Tod.")
                # ~ print("GAME OVER")
    
        
   

class Craftingrez():
    string = ["Stock = Kleinholz + Schnitzmesser in Inv", "Kleinholz = Holz + Axt in Inv", "Axt = Stock + Eisen", "Hammer = Stock + Eisen", "Braustand = Kleinholz + Eisen + Hammer in Inv"]
    
    
    def __init__(self, crezept = "r", own = "drei", owninv = "Nein", ):
                self.owncraftingr = own + owninv
                self.craftingr1 = crezept
                self.craftingr2 = crezept
                self.craftingr3 = crezept
                self.craftingrinv1 = crezept
                self.true1 = "owninv"
                self.true2 = "owninv"
                self.true3 = "owninv"
                self.trueinv1 = "owninv"
                
    def showrez(self):
        for r in self.string:
            print(r)
            print("------")
    
    def crafted(self):
        if self.owncraftingr == "einsJa":
            for m in invitems:
                if m == self.craftingr1:
                    self.true1 = "Ja"
                if m == self.craftingrinv1:
                    self.trueinv1 = "Ja"
            if self.true1 == "Ja":
                if self.trueinv1 == "Ja":
                    invitems.append(self.name)
                    invitems.remove(self.craftingr1)
                    print("Herstellung von " + str(self.name) + " erfolgreich!")
                    print(str(self.name) + " wurde in dein Inventar hinzugefuegt. Dein Inventar beinhaltet nun: ")
                    instanzinv.showitems()
                else:
                    print(" ")
                    print("Du brauchst " + str(self.craftingr1) + " und " + str(self.craftingrinv1) + " um " + str(self.name) + " herzustellen.")
            else:
                print(" ")
                print("Du brauchst " + str(self.craftingr1) + " und " + str(self.craftingrinv1) + " um " + str(self.name) + " herzustellen.")
        self.true1 = "Nein"
        self.trueinv1 = "Nein"
        
        if self.owncraftingr == "zweiJa":
            for m in invitems:
                if m == self.craftingr1:
                    self.true1 = "Ja"
                if m == self.craftingr2:
                    self.true2 = "Ja"
                if m == self.craftingrinv1:
                    self.trueinv1 = "Ja"
            if self.true1 == "Ja":
                if self.true2 == "Ja":
                    if self.trueinv1 == "Ja":
                        invitems.append(self.name)
                        invitems.remove(self.craftingr1)
                        invitems.remove(self.craftingr2)
                        print("Herstellung von " + str(self.name) + " erfolgreich!")
                        print(str(self.name) + " wurde in dein Inventar hinzugefuegt. Dein Inventar beinhaltet nun: ")
                        instanzinv.showitems()
                    else:
                        print(" ")
                        print("Du brauchst " + str(self.craftingr1) + " und " + str(self.craftingrinv1) + " um " + str(self.name) + " herzustellen.")
            else:
                print(" ")
                print("Du brauchst " + str(self.craftingr1) + " und " + str(self.craftingrinv1) + " um " + str(self.name) + " herzustellen.")
        self.true1 = "Nein"
        self.true2 = "Nein"
        self.trueinv1 = "Nein"

        if self.owncraftingr == "zweiNein":
            for m in invitems:
                if m == self.craftingr1:
                    self.true1 = "Ja"
                if m == self.craftingr2:
                    self.true2 = "Ja"
            if self.true1 == "Ja":
                if self.true2 == "Ja":
                    invitems.append(self.name)
                    invitems.remove(self.craftingr1)
                    invitems.remove(self.craftingr2)
                    print("Herstellung von " + str(self.name) + " erfolgreich!")
                    print(str(self.name) + " wurde in dein Inventar hinzugefuegt. Dein Inventar beinhaltet nun: ")
                    instanzinv.showitems()
                else:
                    print(" ")
                    print("Du brauchst " + str(self.craftingr1) + " und " + str(self.craftingr2) + " um " + str(self.name) + " herzustellen.")
            else:
                print(" ")
                print("Du brauchst " + str(self.craftingr1) + " und " + str(self.craftingr2) + " um " + str(self.name) + " herzustellen.")
        self.true1 = "Nein"
        self.true2 = "Nein"  
        
class Braustand(Craftingrez):
    beschreibung = "Kann plaziert werden. Wird zum Brauen von Bier Verwendet"
    name = "Braustand"
    
    def __init__(self):
        Craftingrez.__init__(self)
        self.owncraftingr = zwei + Ja
        self.craftingr1 = "Kleinholz"
        self.craftingr2 = "Eisen"
        self.craftingrinv1 = "Hammer"   
        
    def crafted1(self):
        self.crafted()  
        
    def brauen(self):
        instanzinv.showitems()
        w = input("Moechtest du ein Bier brauen fuer: Trockenes Brot, Volle Flasche Wasser? >")
        if w == "Ja":
            instanzcraftingrezbier.brauen()
            
class Zauberaltar():
    beschreibung = "Wird zum verzaubern von Buechern verwendet"
    name = "Zauberaltar"
    
    def __init__(self):
        self.space = ""
        self.zlist = ["Zauberbuch:Astralkoerper", "Zauberbuch:Schnelligkeit1", "Zauberbuch:Schnelligkeit2", "Buch", "Buch"]
        self.rc = ""
    
    def verzaubern(self):
        global invitems
        if self.space == "":
            r = input("Willst du ein Buch platzieren? >")
            if r == "Ja":
                if "Buch" in invitems:
                    invitems.remove("Buch")
                    self.space = "Buch"
                    print("Buch platziert")
                    c = input("Willst du das Buch verzaubern? >")
                    if c == "Ja":
                        self.rc = random.choice(self.zlist)
                        self.space = self.rc
                        v = input("Willst du das Buch entnehmen? >")
                        if v == "Ja":
                            print("Du entnimmst das Buch:{}".format(self.rc))
                            invitems.append(self.rc)
                            self.space = ""
            else:
                print("")
        elif self.space == "Buch":
            c = input("Willst du das Buch verzaubern? >")
            if c == "Ja":
                self.rc = random.choice(self.zlist)
                self.space = self.rc
                v = input("Willst du das Buch entnehmen? >")
                if v == "Ja":
                    print("Du entnimmst das Buch:{}".format(self.rc))
                    invitems.append(self.rc)
                    self.space = ""
        else:
            v = input("Wilsst du das Buch entnehmen? >")
            if v == "Ja":
                print("Du entnimmst das Buch:{}".format(self.rc))
                invitems.append(self.rc)
                self.space = ""
            
class Feuerstelle():
    def __init__(self):
        self.name = "Feuerstelle"
        self.beschreibung = "Bei einer Feuerstelle kannst du kochen"
        self.lit = False
        self.true = True
        
    def kochen(self):
        print("")
        print("Kochen ist noch nicht verfuegbar!")
        print("")
    
    def anzuenden(self):
        print("")
        if self.lit == False:
            if "Feuersteine" in invitems:
                r1 = input("Feuersteine benutzen um Feuer anzuzuenden? >")
                if r1 == "Ja":
                    while self.true == True:
                        print("")
                        r2 = input(">>")
                        if r2 == "stop":
                            break
                        else:
                            if random.random() < 0.3:
                                self.lit = True
                                print("Feuer entzuendet!")
                                break
                            else:
                                print("Nichts passiert")
                                continue
                else:
                    print("")
            else:
                print("Du hast nichts zum anzuenden!")
                print("")
        else:
            self.kochen()
            
class Kiste(Craftingrez):
    beschreibung = "Kann plaziert werden. Man kann Dinge darin Lagern."
    name = "Kiste"
    
    def __init__(self):
        Craftingrez.__init__(self)
        self.owncrafting = zwei + Ja
        self.craftingr1 = "Kleinholz"
        self.craftingr2 = "Eisen"
        self.craftinginv1 = "Hammer"
        self.inhalt = []
    
    def crafted1(self):
        self.crafted()
        
    def fragen(self):
        r = input("Willst du die Truhe oeffnen?")
        if r == "Ja":
            self.showinhalt()
        else:
            print("")
    
    def giveinhalt(self):
        global invitems
        r = input("Was willst du einlagern? >")
        if r == "alles":
            self.inhalt += invitems
            invitems = []
        elif r == "":
            print("")
        else:
            for x in invitems:
                if x == r:
                    self.inhalt.append(x)
                    invitems.remove(x)
                    break
                else:
                    print("Du hast kein(e) {} im Inventar.".format(r))
                    break
            self.giveinhalt()
                
    def nehmen(self):
        global invitems
        r = input("Was willst du nehmen? >")
        if r == "alles":
            invitems += self.inhalt
            self.inhalt = []
        else:
            for x in self.inhalt:
                if x == r:
                    invitems.append(x)
                    self.inhalt.remove(x)
                    break
                else:
                    print("Es gibt kein(e) {} in der Truhe.".format(r))
                    break
            self.nehmen()
            
    def fill(self, x):
        self.inhalt.append(x)
    
    def showinhalt(self):
        print("=========")
        print("Truhe:")
        print("")
        for s in self.inhalt:
            print(s)
            print("------")
        print("")
        r = input("Was willst du tun? (nehmen, lagern)")
        if r == "":
            print("")
        elif r == "lagern":
            self.giveinhalt()
        elif r == "nehmen":
            self.nehmen()
            
class Bier():
    beschreibung = "Kann getrunken werden. Kann betrunken machen."
    name = "Bier"
    
    def __init__(self):
        self.craftingr1 = "Trockenes Brot"
        self.craftingr2 = "Volle Flasche Wasser"
        self.effect = False
        self.true1 = 0
        self.true2 = 0
        
    def brauen(self):
        for i in invitems:
            if i == self.craftingr1:
                self.true1 = True
            if i == self.craftingr2:
                self.true2 = True
        if self.true1 == True:
            if self.true1 == True:
                invitems.append("Bier")
                invitems.remove(self.craftingr1)
                invitems.remove(self.craftingr2)
                print("Herstellung von " + str(self.name) + " erfolgreich!")
                print(str(self.name) + " wurde in dein Inventar hinzugefuegt. Dein Inventar beinhaltet nun: ")
                instanzinv.showitems()
            else:
                print(" ")
                print("Du brauchst " + str(self.craftingr1) + " und " + str(self.craftingr2) + " um " + str(self.name) + " herzustellen.")  
        else:
            print(" ")
            print("Du brauchst " + str(self.craftingr1) + " und " + str(self.craftingr2) + " um " + str(self.name) + " herzustellen.") 
    
    def betrunken(self):
        if random.random() < .4:
            self.effect()
            print("Du bist betrunken!")
            
    def effect():
        self.effect = True
        #W.I.P
        self.effect = False
            
    def drink(self):
        global amounthung
        global amountdurst
        global amountired
        amounthung -= 2
        amountdurst -= 7
        amountired += 4
        self.betrunken()
        
class Stock(Craftingrez):
    beschreibung = "Wird zum Herstellen von vielen anderen Items gebraucht"
    name = "Stock"
    
    def __init__(self):
        Craftingrez.__init__(self)
        self.owncraftingr = eins + Ja
        self.craftingr1 = "Kleinholz"
        self.craftingrinv1 = "Schnitzmesser"
        
    def crafted1(self):
        self.crafted()
        
class Kleinholz(Craftingrez):
    beschreibung = "Wird zum Herstellen von vielen anderen Items gebraucht"
    name = "Kleinholz"
    
    def __init__(self):
        Craftingrez.__init__(self)
        self.owncraftingr = eins + Ja
        self.craftingr1 = "Holz"
        self.craftingrinv1 = "Axt"
        
    def crafted1(self):
        self.crafted()
        
class Axt(Craftingrez):
    beschreibung = "Ein Werkzeug um Items zu bearbeiten"
    name = "Axt"
    
    def __init__(self):
        Craftingrez.__init__(self)
        self.owncraftingr = zwei + Nein
        self.craftingr1 = "Stock"
        self.craftingr2 = "Eisen"
        
    def crafted1(self):
        self.crafted()

class Hammer(Craftingrez):
    beschreibung = "Ein Werkzeug um Items zu bearbeiten"
    name = "Hammer"
    
    def __init__(self):
        Craftingrez.__init__(self)
        self.owncraftingr = zwei + Nein
        self.craftingr1 = "Stock"
        self.craftingr2 = "Eisen"
        
    def crafted1(self):
        self.crafted()

class durst():
    global amountdurst
    amountdurst = 0

class hunger():
    global amounthung
    amounthung = 0
    
class Food():
    string = "Lebensmittel um Hunger zu regenerieren"
        
    def __init__(self, fp=1):
        self.foodpoints = fp
        
    def eat(self): 
        global amounthung
        amounthung -= self.foodpoints
        if amounthung < 0:
            amounthung = 0
        global invitems
        invitems.remove(self.name)
                
class Apfel(Food):
    name = "Apfel"
    
    def __init__(self):
        Food.__init__(self)
        self.foodpoints = 9
    
    def eat1(self):
        self.eat()
        
class Karotte(Food):
    name = "Karotte"
    
    def __init__(self):
        Food.__init__(self)
        self.foodpoints = 9
        
    def eat1(self):
        self.eat()
        
class Erdapfel(Food):
    name = "Erdapfel"
    
    def __init__(self):
        Food.__init__(self)
        self.foodpoints = 10
        
    def eat1(self):
        self.eat()
        
class Schweinefleisch(Food):
    name = "Schweinefleisch"
    
    def __init__(self):
        Food.__init__(self)
        self.foodpoints = 20
        
    def eat1(self):
        self.eat()
        
class Rindfleisch(Food):
    name = "Rindfleisch"
    
    def __init__(self):
        Food.__init__(self)
        self.foodpoints = 20
        
    def eat1(self):
        self.eat()
        
class Maiskolben(Food):
    name = "Maiskolben"
    
    def __init__(self):
        Food.__init__(self)
        self.foodpoints = 11
        
    def eat1(self):
        self.eat()
        
        
class Trockenes_Brot(Food):
    name = "Trockenes Brot"
    
    def __init__(self):
        Food.__init__(self)
        self.foodpoints = 13
    
    def eat1(self):
        self.eat()
        
class Wildfleisch(Food):
    name = "Wildfleisch"
    string = "Ein selbst erlegtes Wild."
    
    def __init__(self):
        Food.__init__(self)
        self.foodpoints = 23
    
    def eat1(self):
        self.eat()
        
class Liquids():
    string = "Getraenke um den Durst zu stillen"
        
    def __init__(self, wp=1):
        self.waterpoints = wp
        
    def drink(self): 
        global amountdurst
        amountdurst -= self.waterpoints
        if amountdurst < 0:
            amountdurst = 0
        global invitems
        invitems.remove(self.name)
        invitems.append("Leere Flasche")

class Water(Liquids):
    name = "Volle Flasche Wasser"
    string = "Ganz normales Wasser"
    waterpoints = 2
    def __init__(self):
        Liquids.__init__(self)
        self.waterpoints = 10
    
    def drink1(self):
        self.drink()

class Saettigungst():
    string = "Ein Trank der dich komplett saettigt."
    name = "Saettigungs-Trank"
        
    def take(self):
        global amounthung
        amounthung = 0
        invitems.remove(self.name)
        
class Magischesquellwasser():
    string = "Ein besonderes Wasser, dass deinen Durst komplett stillt"
    name = "Volle Flasche mit Magischem Quellwasser"
    
    def take(self):
        global amountdurst
        amountdurst = 0
        invitems.remove(self.name)
        invitems.append("Leere Flasche")

class Inventory():
    global invitems
    invitems = ["Fackel", "Schnitzmesser", "Leere Flasche", "Buch", "Schreibfeder", "Zauberbuch:Schnelligkeit2", "Zauberbuch:Meditation"]
    global playergold
    playergold = 0
    
    def showitems(self):
        global playergold
        print("Folgende Sachen befinden sich in deinem Rucksack:")
        if len(invitems) == 0:
            print("dein Rucksack ist leer")
        else:
            print("==========")
            for i in invitems:
                print(i)
                print("----")
            print("")
            print("")
            print("Gold:{}".format(playergold))
            print("==========")     

class Ruestungsinv():
    string = "Hier kannst du deine Ruestungen anziehen oder ablegen"
    space1 = "Nichts"
    space2 = "Nichts"
    
    def __init__(self, h="h", r="r"):
        space1 = h
        space2 = r
        
class faehigkeitcount():
    faehigkeitcount = 0 
    
class Loot():                                                             
    global kindsloot
    kindsloot = ["Buch", "Schreibfeder", "Gold", "Trockenes Brot", "Apfel", "Holz", "Eisen", "Stein", "Feuersteine", 
                 "Knochen", "Kleiderfetzen", "Fackel", "Heiltrank", "Nichts", "Nichts", "Nichts", "Nichts", "Nichts", "Nichts", "Nichts", "Nichts", "Nichts"]
    counting = 13
    global tookloot
    tookloot = random.choice(kindsloot)

class Waffen():
    string = "Waffen um im Kampf mehr Schaden zu machen"
    
    def __init__(self, dg=1):
        self.damage = dg

class Dolch(Waffen):
    string = "Ein ganz normaler Dolch, der zwar wenig Schaden macht, aber mit Gift verstaerkt werden kann."
    name = "Dolch"
    
    def __init__(self):
        Waffen.__init__(self)
        self.damage = 2
    
class Schwert(Waffen):
    string = "Ein ganz normales Schwert aus Eisen, welches verzaubert werden kann."
    name = "Schwert"
    
    def __init__(self):
        Waffen.__init__(self)
        self.damage = 4 
    
class RLives():
    def __init__(self):
        self.rlives = 0

instanzrlives = RLives()

class Ruestung():
    string = "Ruestung um im Kampf mehr Verteidigung zu haben."
    
    def __init__(self, rp=1):
        self.ruestung = rp
        
    def anziehen(self):
        for r in invitems:
            if r == self.name:
                ja = input("Willst du " + "'" + str(self.name) + "'" + " anziehen?")
                if ja == "Ja":
                    if self.classr == "Helm":
                        instanzruestungsinv.space1 = self.name
                        invitems.remove(self.name)
                        print(str(self.name) + " ausgeruestet.")
                        instanzrlives.rlives += self.ruestung
                    if self.classr == "Ruestung":
                        instanzruestungsinv.space2 = self.name
                        invitems.remove(self.name)
                        print(str(self.name) + " ausgeruestet.")

class Helm(Ruestung):
    string = "Ein ganz normaler Helm um dich zu schuetzen"
    classr = "Helm"
    name = "Helm"
    
    def __init__(self):
        self.ruestung = 2
        Ruestung.__init__(self)
        
    def anziehen1(self):
        self.anziehen()
        
    
class Sleep():                                                             
    global chance_to_failsleep
    chance_to_failsleep = ["fehlgeschlagen", "fehlgeschlagen","ruhig","ruhig","ruhig","ruhig","ruhig","ruhig"]
    global testforfailsleep
    testforfailsleep = random.choice(chance_to_failsleep)
    
class Sleepfail():                                                        
    global kindssleepfail
    kindssleepfail = ["Gegner ueberrascht dich", "Etwas gehoert", "Etwas gehoert", "Etwas gehoert", "Unbekannt", "Unbekannt", "Unbekannt"]
    global tooksleepfail
    tooksleepfail = random.choice(kindssleepfail)

class Tired():
    global amountired
    amountired = 0
        
class Fluss():
    beschreibung = "Beim Fluss Kannst du ein Leere Flasche auffuellen."
    chance = ["Ja"]
        
    def begegnung(self):
        true = True
        self.r = random.choice(self.chance)
        if self.r == "Ja":
            if "Leere Flasche" in invitems:
                event1()
                self.x = input("Du bist auf einen Fluss gestossen. Willst du deine Leere Flasche auffuellen? >")
                if self.x  == "Ja":
                    invitems.append("Volle Flasche Wasser")
                    invitems.remove("Leere Flasche")
                    print("Flasche wurde mit Wasser gefuellt")
                elif self.x == "Nein":
                    print("Du gehst weiter")
                    true = False
                while true == True:
                    if "Leere Flasche" in invitems:
                        r = input("Willst du deine Leere Flasche auffuelen? >")
                        if self.x  == "Ja":
                            invitems.append("Volle Flasche Wasser")
                            invitems.remove("Leere Flasche")
                            print("Flasche wurde mit Wasser gefuellt")
                        elif self.x == "Nein":
                            print("Du gehst weiter")
                            break
                    else:
                        break
                    break
        true = True
    
class Haendler():
    def __init__(self):
        self.waehrung = "Gold"
        self.sortiment = ["Hammer: 1", "Axt: 1", "Helm: 2", "Trockenes Brot: 1", "Bier: 2", "Leere Flasche:3", "Apfel: 1", "Buch: 1", "Schreibfeder: 1"]
        
    
    def Haendlerschild(self):
        print("________________________________________________________________")
        print("................................................................|")
        print("................................................................|")
        print("................................................................|")
        print("................................................................|")
        print("................................................................|")
        print("................................................................|")
        print("................................................................|")
        print("................................................................|")
    
    def handeln(self):
        global playergold
        for s in self.sortiment:
            print(s)
        print("-------")
        p = input("Was moechtest du kaufen? >")
        if p == "Hammer":
            if playergold >= 1:
                invitems.append("Hammer")
                playergold -= 1
        elif p == "Axt":
            if playergold >= 1:
                invitems.append("Axt")
                playergold -= 1
        elif p == "Helm":
            if playergold >= 2:
                invitems.append("Helm")
                playergold -= 2
        elif p == "Trockenes Brot":
            if playergold >= 1:
                invitems.append("Trockenes Brot")
                playergold -= 1
        elif p == "Bier":
            if playergold >= 2:
                invitems.append("Bier")
                playergold -= 2
        elif p == "Leere Flasche":
            if playergold >= 3:
                invitems.append("Leere Flasche")
                playergold -= 3
        elif p == "Apfel":
            if playergold >= 1:
                invitems.append("Apfel")
                playergold -= 1
        elif p == "Buch":
            if playergold >= 1:
                invitems.append("Buch")
                playergold -= 1
        elif p == "Schreibfeder":
            if playergold >= 1:
                invitems.append("Schreibfeder")
                playergold -= 1

class Buch():
    def __init__(self):
        self.name = "Buch"
        self.inhalt = ""
        self.zauber = ""
        self.wort = 0
        
    def verwenden(self):
        global invitems
        for b in invitems:
            if b[0:4] == "Buch":
                for az in invitems:
                    if az[0:4] == "Buch":
                        print(az)
                ch = input("Welches buch willst du bearbeiten? >")
                if ch == self.name:
                    r = input("Was moechtest du tun?(schreiben, lesen) >")
                    if r == "lesen":
                        self.lesen()
                    elif r == "schreiben":
                        for b in invitems:
                            if b == "Schreibfeder":
                                self.schreiben()
                                self.wort = 1
                        if self.wort == 0:
                            print("Du brauchst eine Schreibfeder um schreiben zu koennen.")
                else:
                    print("Dieses Buch ist nicht in deinem Inventar vorhanden.")
    
    def lesen(self):
        global invitems
        print("=======")
        print(self.inhalt)
        print("=======")
        if self.name[0:10] == "Zauberbuch":
            instanzspellinv.sinvitems.append(self.zauber)
            invitems.remove(self.name)
        
    def schreiben(self):
        global invitems
        print(self.inhalt)
        r = input(">")
        if r == "Loeschen!":
            p = input("Bist du dir sicher?")
            if p == "Nein":
                self.schreiben()
            else:
                self.inhalt = ""
                self.schreiben()
        elif r == "Stop":
            print("")
            c = input("Titel(Wenn du den Titel festlegst, kannst du das buch nicht mehr bearbeiten): >")
            if c == "Nein":
                print("")
            if c == "":
                self.name = self.name
            else:
                invitems.remove(self.name)
                self.name = "Buch:" + c
                invitems.append(self.name)
        else:
            self.inhalt = self.inhalt + "\n" + r
            self.schreiben()
            
class Mana():
    def __init__(self):
        string = "Mana wird benoetigt um Zauber auszufuehren"
        self.mana = 10
        
class Spellinv():
    def __init__(self):
        self.sinvitems = []

class Spell():
    def __init__(self):
        self.name = ""
        self.string = ""
        self.cost = 0
        
    def trigger(self):
        if instanzmana.mana >= self.cost:
            print(self.name)
            print(self.string)
            print("Kosten: {}".format(self.cost))
            self.effect()
            print("Zauber {} aktiviert!".format(self.name))
        else:
            print("Du hast nicht genug Mana.")
                
class Astralkoerper(Spell):
    def __init__(self):
        Spell.__init__(self)
        self.name = "Astralkoerper"
        self.string = "Mit diesem Zauber wirst du zur Astralgestalt(Du kannst durch Fallen, Waende u.s.w. gehen)"
        self.cost = 5
        self.immune = False
        
    def trigger1(self):
        self.trigger()
    
    def effect(self):
        self.immune = True
        instanzmana.mana -= self.cost
        
class Schnelligkeit1(Spell):
    def __init__(self):
        self.name = "Schnelligkeit1"
        self.string = "Mit diesem Zauber wirst du doppelt so schnell."
        self.cost = 2
        self.doppelt = False
        
    def trigger1(self):
        self.trigger()
        
    def effect(self):
        self.doppelt = True
        instanzmana.mana -= self.cost
        
class Schnelligkeit2(Spell):
    def __init__(self):
        self.name = "Schnelligkeit2"
        self.string = "Mit diesem Zauber wirst du dreimal so schnell."
        self.cost = 5
        self.dreimal = False
        
    def trigger1(self):
        self.trigger()
        
    def effect(self):
        self.dreimal = True
        instanzmana.mana -= self.cost

class Meditation(Spell):
    def __init__(self):
        self.name = "Meditation"
        self.string = "Meditiere um Leben, Hunger, Durst und Müdigkeit zu regenerieren. Drücke [b] um aufzuhören"
        self.cost = 1

    def trigger1(self):
        self.trigger()

    def effect(self):
        true = True
        while true == True:
            global fcount
            global amountdurst
            global amounthung
            global amountired
            if instanzmana.mana > 0:
                instanzmana.mana -= self.cost
                amounthung -= 2
                amountdurst -= 1
                amountired -= 2
                if amounthung < 0:
                    amounthung = 0
                if amountdurst < 0:
                    amountdurst = 0
                if amountired < 0:
                    amountired = 0
            else:
                print("Du hast nicht genug Mana!")
                break
            r = input("Mana: {} h/d/t:{}, {}, {} >".format(instanzmana.mana, amounthung, amountdurst, amountired))
            if r == "b":
                break
            

                
class Zauberbuch(Buch):
    def __init__(self):
        Buch.__init__(self)
        
    def verwenden1(self):
        global invitems
        print("")
        print("============")
        for b in invitems:
            if b[0:10] == "Zauberbuch":
                for az in invitems:
                    if az[0:10] == "Zauberbuch":
                        print(az)
                        print("-----")
                print("============")
                print("")
                ch = input("Welches buch willst du lesen? >")
                if ch in invitems:
                    if ch == "Zauberbuch:Astralkoerper":
                        instanzzauberbuchastralkoerper.verwenden2()
                    elif ch == "Zauberbuch:Schnelligkeit1":
                        instanzzauberbuchschnelligkeit1.verwenden2() 
                    elif ch == "Zauberbuch:Schnelligkeit2":
                        instanzzauberbuchschnelligkeit2.verwenden2()
                    elif ch == "Zauberbuch:Meditation":
                        instanzzauberbuchmedi.verwenden2()
                else:
                    print("Dieses Buch ist nicht in deinem Inventar vorhanden.")
                    

            
class BAstralkoerper(Zauberbuch):
    def __init__(self):
        Zauberbuch.__init__(self)
        self.name = "Zauberbuch:Astralkoerper"
        self.inhalt = "Astralkoerper:\n\nWandle durch den Raum  -  KRARRKZ MAUNFIUH ARHKZ MFUR!"
        self.zauber = "Astralkoerper"
        
    def verwenden2(self):
        self.lesen()
        
class BSchnelligkeit1(Zauberbuch):
    def __init__(self):
        Zauberbuch.__init__(self)
        self.name = "Zauberbuch:Schnelligkeit1"
        self.inhalt = "Schnelligkeit:\n\nLass dich vom Winde tragen - THUUM MHARKZ MARKATRAZH!"
        self.zauber = "Schnelligkeit1"
        
    def verwenden2(self):
        self.lesen()
     
class BSchnelligkeit2(Zauberbuch):
    def __init__(self):
        Zauberbuch.__init__(self)
        self.name = "Zauberbuch:Schnelligkeit2"
        self.inhalt = "Schnelligkeit:\n\nLass dich vom Winde tragen - THUUM MHARKZ MARKATRAZH!"
        self.zauber = "Schnelligkeit2"
        
    def verwenden2(self):
        self.lesen()

class BMeditation(Zauberbuch):
    def __init__(self):
        Zauberbuch.__init__(self)
        self.name = "Zauberbuch:Meditation"
        self.inhalt = "Meditation:\n\nIn der Ruhe liegt die wahre Kraft des Geistes - OOOOOOHHHHMMMMMMM!"
        self.zauber = "Meditation"

    def verwenden2(self):
        self.lesen()
        

class Magier():
    name = "Magier"
    beschreibung = "Ein Magier hat von Anfang an Tranke im Invantar die ihm Boni geben, und kann mit seiner Faehigkeit seine Statuswerte(Hunger, durst, Muedigkeit) regenerieren."  
    faehigkeit = "deine Statuswerte zuruecksetzten"
    
    def giveitems(self):
        invitems.append("Saettigungs-Trank")
        invitems.append("Volle Flasche mit Magischem Quellwasser")
        invitems.remove("Leere Flasche") 
        instanzmana.mana += 10   
        
    def actfaehigkeit(self):
            global amountdurst
            amountdurst = 0
            global amounthung
            amounthung = 0
            global amountired
            amountired = 0
            print("Faehigkeit aktiviert!")  
    
class Jaeger():
    beschreibung = "Ein Jaeger hat eine hoehere Wahrscheinlichkeit beim looten etwas zu finden und auf einen Fluss zu stossen. Mit seiner Faehigkeit jagt er ein Tier und bekommt Fleich."
    beschreibungjonny = "Ein Jaeger hat eine hoehere Wahrscheinlichkeit beim looten etwas zu finden und auf einen Fluss zu stossen(und auch einen Chiwawa zu finden). Mit seiner Faehigkeit jagt er ein Tier und bekommt Fleich."
    name = "Jaeger"
    faehigkeit = "ein Tier jagen um Fleisch zu bekommen und (Coming Soon)Fallen aufdecken"
    global fcount
    
    
    def __init__(self):
        self.tv = 0
    
    def findchance(self):
        instanzfluss.chance.append("Ja")
        kindsloot.remove("Nichts")
        kindsloot.remove("Nichts")
        kindsloot.remove("Nichts")
        
    def actfaehigkeit(self):
        self.tv = 1
        invitems.append("Wildfleisch")
        print("Faehigkeit aktiviert!")
        
class Krieger():
    beschreibung = "Ein Krieger hat von Anfang an ein Schwert und Ruestung im Inventar und kann mit seiner Faehigkeit(coming soon) "
    name = "Krieger"
    faehigkeit = "Coming Soon"
    
    def giveitems(self):
        invitems.append("Schwert des Kriegers")
        invitems.append("Ruestung des Kriegers")
    
class Handwerker():
    beschreibung = "Ein Handwerker hat von Anfang an verschiedene Werkzeuge im Inventar und kann mit seiner Faehigkeit(coming Soon)"
    name = "Handwerker" 
    faehigkeit = "Coming Soon"
    
    def giveitems(self):
        invitems.append("Mauer")
        invitems.append("Mauer")
        invitems.append("Mauer")
        invitems.append("Mauer")
        invitems.append("Mauer")
        invitems.append("Mauer")
        invitems.append("Axt")
        invitems.append("Hammer")
        
class Hacker():
    beschreibung = "010100Ein Hac01er kan1001 a010le000s ma10c00he1n."
    name = "HACKER"
    faehigkeit = "Crash.exe"
    
    def faehigkeit1(self):
        t = True
        while t == True:
            r = random.randint(0, 1)
            print(r)
    
def classquestion():
    global classplayer
    classplayer = input("Welche Klasse willst du annehmen? (Magier, Jaeger, Krieger, Handwerker) ")
    if classplayer == "Magier":
        print("Oho, ein Meister der arkanen Magie!")
    elif classplayer == "Jaeger":
        print("Flink und Leise, diese Jaeger.")
    elif classplayer == "Krieger":
        print("Nichts kann einen maechtigen Krieger bezwingen!")
    elif classplayer == "Handwerker":
        print("Deine Werke sind Legendaer!")
    elif classplayer == "":
        sicher1 = input("Warnung: nur die vorgegebenen Klassen haben spezielle Werte und Kraefte! Willst du trotzdem fortfahren? " )
        if sicher1 == "Nein":
            print("")
            classquestion()
        classplayer = "N/A"
    elif classplayer == "Hacker":
        print(">>Intruder detected")
        print(">>Firewall failed")
        print(">>Permission granted")
    else:
        sicher1 = input("Warnung: nur die vorgegebenen Klassen haben spezielle Werte und Kraefte! Willst du trotzdem fortfahren? " )
        if sicher1 == "Nein":
            print("")
            classquestion()
            
def testforclass():
    if classplayer == "Magier":
        print(instanzmagier.beschreibung)
        instanzmagier.giveitems()
    elif classplayer == "Jaeger":
        if nameplayer[0:5] == "Jonny":
            print(instanzjaeger.beschreibungjonny)
            instanzjaeger.findchance()
        else:
            print(instanzjaeger.beschreibung)
            instanzjaeger.findchance()
    elif classplayer == "Krieger":
        print(instanzkrieger.beschreibung)
        instanzkrieger.giveitems()
    elif classplayer == "Handwerker":
        print(instanzhandwerker.beschreibung)
        instanzhandwerker.giveitems()
    else:
        print("Als " + str(classplayer) + " hast du keine zusaetlichen Faehigkeiten")

def testforfaehigkeit():
    if classplayer == "Magier":
        print("Deine Faehigkeit ist: " + str(instanzmagier.faehigkeit))
        act = input("Willst du deine Faehigkeit aktivieren? ")
        if act == "Ja":
            instanzmagier.actfaehigkeit()
    elif classplayer == "Jaeger":
            print("Deine Faehigkeit ist: " + str(instanzjaeger.faehigkeit))
            act = input("Willst du deine Faehigkeit aktivieren? ")
            if act == "Ja":
                instanzjaeger.actfaehigkeit()
    elif classplayer == "Krieger":
        print("Deine Faehigkeit ist: " + str(instanzkrieger.faehigkeit))
        act = input("Willst du deine Faehigkeit aktivieren? ")
        if act == "Ja":
            print("HI")
    elif classplayer == "Handwerker":
        print("Deine Faehigkeit ist: " + str(instanzhandwerker.faehigkeit))
        act = input("Willst du deine Faehigkeit aktivieren? ")
        if act == "Ja":
            print("HI")
    elif classplayer == "Hacker":
        instanzhacker.faehigkeit1()
    else:
        print("Als " + str(classplayer) + " hast du keine zusaetlichen Faehigkeiten")

def wait(msg="druecke ENTER"):
    a = input(msg)
    
def wait1():
    pass

def loot():
    """erzeuge einen zufaelligen Gegenstand"""
    zeugs = ["Buch", "Schreibfeder", "Heiltrank", "Trockenes Brot", "Apfel", "Holz", "Eisen", "Stein", "Feuersteine", "Knochen", "Kleiderfetzen", "Fackel"]
    return random.choice(zeugs)   

def hilfe():
    """zeigt hilfstext, wartet auf ENTER Taste"""
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("Befehle:")
    print("[w] [a] [s] [d]......steuere den Spieler")
    print("[<] [>]..............Level rauf / Level runter")
    print("[i]..................zeige Rucksack (inventory)")
    print("[si].................zeige Zauber (spell inventory)")
    print("[sch]................Schlafen")
    print("[auf]................aufbleiben (wenn du im Schlaf aufwachst)")
    print("[l]..................looten")
    print("[z]..................zaubern")
    print("[r]..................Ruestung anzeigen")
    print("[e]..................essen")
    print("[t]..................trinken")
    print("[f]..................Faehigkeit aktivieren")
    print("[c]..................Herstellung (craften)")
    print("[p]..................Bauen (place)")
    print("[reden]..............Reden")
    print("[quit] [exit] [Q]....Spiel verlassen")        
    print("[?] [help]...........diesen Hilfstext anzeigen")
    # ~ print("[q]..................Heiltrank trinken (quaff potion)")
    print("[Enter]..............eine Runde warten")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("Legende(Level):")
    print("[#]..................Mauer")
    print("[.]..................Boden")
    print("[M]..................Monster")
    print("[k]..................Schluessel (key)")
    print("[L]..................Gegenstand (loot)")
    print("[Y]..................Super Gegenstantd (loot)")
    print("[H]..................Haendler")
    print("[A]..................Zauberaltart")
    print("[D]..................Tuere (door)")
    print("[!]..................Schild")
    print("[U]..................Braustand")
    print("[c]..................Truhe")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("Legende(Werte):")
    print("[h/d/t/f]............Hunger, Durst, Muedigkeit, Faehigkeit(Anzahl der Aktivierungen)")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    wait()

def kampfrunde(m1, m2):
    txt = []         # """ Spieler kaempft gegen Monster Object"""
    if m1.hitpoints > 0 and m2.hitpoints > 0:
        txt.append("{} ({} hp) schlaegt nach {} ({} hp)".format(m1.name, m1.hitpoints, m2.name, m2.hitpoints))
        if "Schwert" in m1.rucksack:      # and rucksack["Waffe"] >0:
            damage = random.randint(1, 4)
            waffe = "Schwert"
        elif "Taschenmesser" in m1.rucksack: 
            damage = random.randint(1, 3)
            waffe = "Taschenmesser"
        else:
            damage = random.randint(1, 2)
            waffe = "Faust"
        txt.append("{} attackiert {} mit {} fuer {} Schaden".format(
              m1.name, m2.name, waffe, damage))
        if "Ruestung" in m2.rucksack: 
            damage -= 1
            txt.append("Ruestung von {} absorbiert einen Schadenspunkt".format(m2.name))
        if "Schild" in m2.rucksack:
            damage -= 1
            txt.append("Schild von {} aborbiert einen Schadenspunkt".format(m2.name))
        if damage > 0:
            m2.hitpoints -= damage
            txt.append("{} verliert {} hitpoints ({} hp uebrig)".format(m2.name, damage, m2.hitpoints))
        else:
            txt.append("{} bleibt unverletzt".format(m2.name))
    for line in txt:
        print(line)
    wait()


class Monster(object):
    def __init__(self, x, y, hp=0):
        if hp == 0:
            self.hitpoints = random.randint(5, 10)
        else:
            self.hitpoints = hp
        self.x = x
        self.y = y
        self.name = "Monster"
        self.rucksack = {}
        for z in ["Taschenmesser", "Schwert", "Schild", "Ruestung"]:
            if random.random() < 0.1:  # 10% Chance
                self.rucksack[z] = 1
                
class NPCinvItems():
    def __init__(self, n, s, c):
        self.name = n
        self.string = s
        self.cost = c
        
class NPCinvItemsChooser():
    def __init__(self):
        self.list = []
        self.i1 = ["Apfel", "Ein guter, leckerer Apfel", 1]
        self.i2 = ["Schnitzmesser", "Ein Schnitzmesser kann man immer brauchen", 3]
        self.i3 = ["Holz", "Ein Holz in Ehren, kann niemand verwehren", 2]
        self.i4 = ["Stock", "Ein Stock vielleicht?", 1]
        self.i5 = ["Kleidung", "Etwas abgetragen aber es geht", 3]
        self.i6 = ["Fell", "Beste Qualitaet", 3]
        self.ilist = [self.i1, self.i2, self.i3, self.i4, self.i5, self.i6]

        
    def chooser(self):
        self.i = random.choice(self.ilist)
        self.n = self.i[0]
        self.b = self.i[1]
        self.c = self.i[2]
        self.list.append(NPCinvItems(self.n, self.b, self.c))
        
    def isitem(self):
        for npcitem in self.list:
            return npcitem

class NPC():
    def __init__(self, x, y, hp=0):
        if hp == 0:
            self.hitpoints = random.randint(2, 5)
        else:
            self.hitpoints = hp
        self.x = x
        self.y = y
        self.greetings = ["Guten Morgan", "Guten Morgen", "Servus", "Gries Di", "Hallo", "Guten Abend"]
        self.greet = random.choice(self.greetings)
        self.namelist = ["Karl", "Huber", "Hans", "Paul", "Markus", "Martin", "Xava", "Matthias", "Jonathan", "Jonny", "Franz", "Ferdinand", "Leopold", "Gernot", "Gergard", "Marianne", "Anna", "Blanka", "Lea", "Margarethe", "Glothilde", "Waltdraud", "Hildegard"]
        self.name = random.choice(self.namelist)
        self.rucksack = []
        self.gold = random.randint(3, 11)
        self.status = ""
        self.angesprochen = 0
        self.satz1list = ["Wie kann ich dir weiterhelfen?", "Was kann ich fuer dich tun?", "Was gibt's denn?", "Wos is los?", "Wos is passiert?", "Ja?"]
        self.satzwaslist = ["Wie bitte?", "Ich habe dich nicht verstanden, kannst du das bitte noch einmal sagen?", "Was?", "Was hast du gesagt?", "Wos host gsogt?", "Wos is los?"]
        self.satzwas = ""
        self.satz1 = ""
        self.abschlist = ["Tschau!", "Tschuess!", "Baba!", "Pfier Di!", "Auf Wiedersehen!", "Schoenen Tag noch!"]
        self.absch = random.choice(self.abschlist)
        self.hauslist = [2, 3]
        self.haus = random.choice(self.hauslist)
        if self.haus in self.hauslist:
            self.hauslist.remove(self.haus)
        self.visit = False
        
    def reden(self):
        self.status = "{}:{} {}!".format(self.name, self.greet, nameplayer)
        self.angesprochen += 1
            
    def hausbesuch(self):
        if random.random() < 0.5:
            print("[{}]:Komm mit! Ich zeige dir mein Haus.".format(self.name))
            self.visit = True
        else:
            print("[{}]:Nein.".format(self.name))
            self.visit = False
            
    def abschied(self):
        print("[{}]:{}".format(self.name, self.absch))
        
    def betteln(self):
        if random.random() < 0.5:
            if self.gold > 0:
                print("Hier hast du etwas.")
                invitems.append("Gold")
                self.gold -= 1
                print("Gold + 1")
            else:
                print("Tut mir Leid. Ich habe selbst nicht genug Gold.")
        else:
            print("Nein")
            
    def addrucksackitem(self):
        self.times = random.randint(0, 6)
        while self.times > 0:    
            rucksackitemchooser = NPCinvItemsChooser()
            rucksackitemchooser.chooser()
            rucksackitems = rucksackitemchooser.isitem()
            self.rucksack.append(rucksackitems)
            self.times -= 1
        self.times = 0
        
    def handeln(self):
        self.addrucksackitem()
        print("")
        if self.rucksack == []:
            print("Ich habe nichts zu verkaufen.")
        else:
            print("=============")
            print("[{}]:Das kann ich verkaufen:".format(self.name))
            print("")
            for nitem in self.rucksack:
                print("{}:{}   Kosten:{}".format(nitem.name, nitem.string, nitem.cost))
                print("----")
            print("")
            print("=============")
            print("")
            r = input("Was moechtest du kaufen?")
            global playergold
            for nitem in self.rucksack:
                if r == nitem.name:
                    if playergold >= nitem.cost:
                        playergold -= nitem.cost
                        invitems.append(nitem.name)
                        self.rucksack.remove(nitem)
                        self.gold += nitem.cost
                        print("{} gekauft!".format(nitem.name))
                    else:
                        print("Du hast nicht genug Gold!")
                else:
                    break
        
    def weiter(self):
        self.satz1 = random.choice(self.satz1list)
        self.satzwas = random.choice(self.satzwaslist)
        print("")
        print("===========")
        print("")
        print("[{}]:{}".format(self.name, self.satz1))
        print("")
        r = input("[{}]:".format(nameplayer))
        if "handeln" in r:
            self.handeln()
        elif "Haus" in r:
            self.hausbesuch()
        elif r == "":
            self.abschied()
        elif "Gold" in r:
            self.betteln()
        else:
            print("[{}]:{}".format(self.name, self.satzwas))
        time.sleep(0.3)
        


    
   
        
class Player(Monster):
    def __init__(self, x, y, hp=25):
        Monster.__init__(self, x, y, hp)
        global nameplayer
        # self.rucksack = {}   # loesche zufallsausruestung von class Monster
        self.name = nameplayer
        self.keys = 0
        self.z = 0             # 0 ist der erste Level, 1 ist der 2. Level usw.

    def zeige_rucksack(self):
        """Zeigt Anzahl und Art von Gegenstaenden im Rucksack"""
        print("Folgende Sachen befinden sich in deinem Rucksack:")
        if len(self.rucksack) == 0:
            print("Dein Rucksack ist leer")
        else:
            print("Anzahl, Gegenstand")
            print("==================")
            for ding in self.rucksack:
                print(self.rucksack[ding], ding)
                
    def nimm(self, zeug):
        """Erhoeht Anzahl von Gegenstaenden im Rucksack"""
        global invitems
        invitems.append(zeug)
        
class Tier(Monster):
    def __init__(self, n, hp, x, y):
        self.name = n
        self.hitpoints = hp
        self.x = x
        self.y = y
        self.z = 0
    

class Item(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Trap(Item):
    def __init__(self, x, y):
        Item.__init__(self, x, y)
        self.level = random.randint(1,6)
        self.visible = 0
        self.hitpoints = 2 * self.level
        
    def damage(self):
        damage = 0
        for _ in range(self.level):
            damage += random.randint(1,6)
        return damage

class Level(object):
    def __init__(self, dateiname):
        """liest den dateinamen ein und erzeugt ein Level-Object"""
        self.lines = []
        self.schilder = {}       # schildnummer: schildtext
        self.traps = []
        self.monsters = []
        self.npcs = []
        self.sichtweite = 10
        self.immune = False
        with open(dateiname) as f:
            y = 0
            for line in f:
                goodline = ""
                if line[0] in "123456789":
                    self.schilder[line[0]] = line[1:-1]
                    continue
                elif line.strip() == "":
                    continue
                else: 
                    x = 0
                    for char in line[:-1]:
                        if char == "M" or char == "B" or char =="S":
                            self.monsters.append(Monster(x, y))
                            goodline += "."
                        elif char == "N":
                            self.npcs.append(NPC(x, y))
                            goodline += "."
                        elif char == "T":
                            self.traps.append(Trap(x,y))
                            goodline += "."
                        else:
                            goodline += char
                        x += 1
                self.lines.append(goodline)
                y += 1
    
    def update(self):
        """loescht alle Monster die keine hitpoints mehr haben"""
        self.monsters = [m for m in self.monsters if m.hitpoints > 0]
        self.traps = [t for t in self.traps if t.hitpoints > 0]
        self.npcs = [n for n in self.npcs if n.hitpoints > 0]
                    
    def ersetze(self, x, y, new="."):
        """ersetzt ein Zeichen in einem Level durch das new Zeichen"""
        self.lines[y] = self.lines[y][:x]+new+self.lines[y][x+1:] 
    
    def is_monster(self, x, y):
        """testet ob sich an einer stelle ein monster befindet"""
        for monster in self.monsters:
            if monster.hitpoints > 0 and monster.x == x and monster.y == y:
                return monster
        return False
        
    def is_npc(self, x, y):
        """testet ob sich an einer stelle ein monster befindet"""
        for npc in self.npcs:
            if npc.hitpoints > 0 and npc.x == x and npc.y == y:
                return npc
        return False
        
    def is_visible_trap(self,x,y):
        for trap in self.traps:
            if trap.hitpoints >0 and trap.x == x and trap.y == y and trap.visible:
                return trap
        return False
        
    def is_trap(self, x,y):
        for trap in self.traps:
            if trap.hitpoints >0 and trap.x == x and trap.y == y:
                return trap
        return False
        
    def move_monster(self, player):
        """bewegt Monster zufaellig (oder gar nicht)"""
        for monster in self.monsters:
            x, y = monster.x, monster.y
            dirs = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0),
                    (-1, -1), (0, -1), (1, -1)]
            dx, dy = random.choice(dirs)
            if self.is_monster(x + dx, y + dy):
                continue
            if x+dx == player.x and y+dy == player.y:
                kampfrunde(monster, player)
                kampfrunde(player, monster)
                continue     # Monster wuerde in player hineinlaufen
            wohin = self.lines[y+dy][x+dx]
            if wohin in "#TD":
                continue     # Monster wuerde in Falle oder Mauer oder Tuer laufen
            monster.x += dx
            monster.y += dy 
            
    def move_npc(self, player):
        """bewegt Monster zufaellig (oder gar nicht)"""
        for npc in self.npcs:
            x, y = npc.x, npc.y
            dirs = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0),
                    (-1, -1), (0, -1), (1, -1)]
            dx, dy = random.choice(dirs)
            if self.is_npc(x + dx, y + dy):
                continue
            if x+dx == player.x and y+dy == player.y:
                continue     # Monster wuerde in player hineinlaufen
            wohin = self.lines[y+dy][x+dx]
            if wohin in "#TD":
                continue     # Monster wuerde in Falle oder Mauer oder Tuer laufen
            npc.x += dx
            npc.y += dy 
    
    def paint(self, px, py):
        """druckt den Level und die Position des spielers (px,py)"""
        y = 0
        for line in self.lines:
            x = 0
            for char in line:
                if x == px and y == py:
                    print("@", end="")
                elif self.is_monster(x, y):
                    print("M", end="")
                elif self.is_npc(x, y):
                    print("N", end="")
                elif self.is_visible_trap(x, y):
                    print("T", end="")
                elif char in "123456789":
                    print("!", end="")
                else:
                    print(char, end="")
                x += 1
            print()
            y += 1
            
    def place(self, px, py):
        global invitems
        self.s = input("Was willst du platzieren? >")
        wo = self.lines[py][px] 
        if wo == "<":
            r = input("Auf der Stelle, wo du etwas platzieren willst, steht schon etwas!\n\nWillst du trotzdem plazieren?")
            if r == "Nein":
                self.s = "Nein"
        elif wo == ">":
            r = input("Auf der Stelle, wo du etwas platzieren willst, steht schon etwas!\n\nWillst du trotzdem plazieren?")
            if r == "Nein":
                self.s = "Nein"
        if self.s == "#":
            if "Mauer" in invitems:
                new = "#"
                self.lines[py] = self.lines[py][:px]+new+self.lines[py][px+1:]
                self.immune = True
                invitems.remove("Mauer")
            else:
                print("Du brauchst eine Mauer um [#] plazieren zu koennen")
        elif self.s == "Braustand":
            if "Braustand" in invitems:
                new = "U"
                self.lines[py] = self.lines[py][:px]+new+self.lines[py][px+1:]
                self.immune = True
                invitems.remove("Braustand")
            else:
                print("Du brauchst einen Braustand um [U] plazieren zu koennen")
        elif self.s == "Feuerstelle":
            c = 0
            if "Holz" in invitems:
                for holz in invitems:
                    if holz == "Holz":
                        c += 1
                if c >= 3:
                    new = "F"
                    self.lines[py] = self.lines[py][:px]+new+self.lines[py][px+1:]
                    self.immune = True
                    invitems.remove("Holz")
                    invitems.remove("Holz")
                    invitems.remove("Holz")
                else:
                    print("Du brauchst mehr(3) Holz um eine Feuerstelle zu errichten.")
                    c = 0
            else:
                print("Du brauchst Holz(3) um eine Feuerstell zu errichten.")
            
  
instanzloot = Loot()                                                        #instanzen fur die Klassen
instanzsleep = Sleep()
instanzsleepfail = Sleepfail()
instanzinv = Inventory()
instanzfood = Food()
instanzfoodapfel = Apfel()
instanzhung = hunger()
instanzdurst = durst()
instanzfoodtrocken = Trockenes_Brot()
instanzfoodwildfleisch = Wildfleisch()
instanzliq = Liquids()
instanzliqwater = Water()
instanzsaettigungstrank = Saettigungst()
instanzquellwasser = Magischesquellwasser()
instanzcraftingrez = Craftingrez()
instanzzauberaltar = Zauberaltar()
instanzfeuerstelle = Feuerstelle()
instanztruhe = Kiste()
instanzkarotte = Karotte()
instanzerdapfel = Erdapfel()
instanzschweinefleisch = Schweinefleisch()
instanzrindfleisch = Rindfleisch()
instanzmaiskolben = Maiskolben()
instanzcraftingrezstock = Stock()
instanzcraftingrezkleinholz = Kleinholz()
instanzcraftingrezaxt = Axt()
instanzcraftingrezhammer = Hammer()
instanzcraftingrezbraustand = Braustand()
instanzcraftingrezbier = Bier()
instanzmana = Mana()
instanzspellinv = Spellinv()
instanzbuch = Buch()
instanzzauberbuch = Zauberbuch()
instanzzauberbuchastralkoerper = BAstralkoerper()
instanzzauberbuchschnelligkeit1 = BSchnelligkeit1()
instanzzauberbuchschnelligkeit2 = BSchnelligkeit2()
instanzzauberbuchmedi = BMeditation()
instanzfluss = Fluss()
instanzmagier = Magier()
instanzspell = Spell()
instanzspellastralkoerper = Astralkoerper()
instanzschnelligkeit1 = Schnelligkeit1()
instanzschnelligkeit2 = Schnelligkeit2()
instanzmedi = Meditation()
instanzjaeger = Jaeger()
instanzkrieger = Krieger()
instanzhandwerker = Handwerker()
instanzhacker = Hacker()
instanzhaendler = Haendler()
instanzwaffe = Waffen()
instanzwaffedolch = Dolch()
instanzwaffeschwert = Schwert()
instanzruestung = Ruestung()
instanzruestunghelm = Helm()
instanzruestungsinv = Ruestungsinv()
# ~ instanzangriff1 = Fight(1, "p")
# ~ instanztimer1 = Fight(11, "p")

def equipruestung():
    print("Du hast")
    print("Helm: " + str(instanzruestungsinv.space1))
    print("Ruestung: " + str(instanzruestungsinv.space2))
    print("ausgeruestet.")
    print("")
    instanzinv.showitems()
    print("")
    ja = input("Moechtest du etwas ausruesten?")
    if ja == "Ja":
        was = input("Was moechtest du anziehen? ")
        if was == "Helm":
            instanzruestunghelm.anziehen1()

def Faehigkeit():
    testforfaehigkeit()
            
def fight():
    print("===============")
    print("Ein Kampf beginnt")
    print("===============")
    print("")
    fightorflee()
    
    
def fightorflee():
    ff = input("Was willst du tun? (kaempfen, fliehen) ")
    if ff == "kaempfen":
        print("Du kaempfst.")
        instanzangriff1.start()
        instanztimer1.start()
    if ff == "fliehen":
        print("Du versuchst zu fliehen")
        r = random.randint(0, 1)
        if r == 0:
            print("Flucht erfolgreich!")
        if r == 1:
            print("Flucht gescheitert!")
            instanzangriff1.start()
            instanztimer1.start()

def crafting():
    instanzcraftingrez.showrez()
    rezpick = input("Was willst du herstellen? ")
    if rezpick == "Stock":
        print(" ")
        instanzcraftingrezstock.crafted1()
    if rezpick == "Axt":
        instanzcraftingrezaxt.crafted1()
    if rezpick == "Kleinholz":
        instanzcraftingrezkleinholz.crafted1()
    if rezpick == "Braustand":
        instanzcraftingrezbraustand.crafted1()
    if rezpick == "Hammer":
        instanzcraftingrezhammer.crafted1()
        
def event1():
    print(" ")
    print("__________________________")
    print(" EVENT! ")
    print("__________________________")



def drinking():
    print(" ")
    instanzinv.showitems()
    print(" ")
    for Liquid in invitems:
        if Liquid == "Volle Flasche Wasser":
            print("Volle Flasche Wasser: " + str(instanzliqwater.string) + " Regeneration: " + str(instanzliqwater.waterpoints))
            lpick = input("Moechtest du das Wasser trinken? ")
            if lpick == "Ja":
                instanzliqwater.drink1()
        if Liquid == "Saettigungs-Trank":
            print("Saettigungs-Trank: " + str(instanzsaettigungstrank.string))
            lpick = input("Moechtest du den Saettigungs-Trank trinken? ")
            if lpick == "Ja":
                instanzsaettigungstrank.take()
        if Liquid == "Volle Flasche mit Magischem Quellwasser":
            print("Volle Flasche mit Magischem Quellwasser: " + str(instanzquellwasser.string))
            lpick = input("Moechtest du das Magische Quellwasser trinken? ")
            if lpick == "Ja":
                instanzquellwasser.take()
        if Liquid == "Bier":
            print("Bier: {}".format(instanzcraftingrezbier.beschreibung))
            lpick = input("Moechtest du das Bier trinken? >")
            if lpick == "Ja":
                instanzcraftingrezbier.drink()
            
        
def eating():
    print(" ")
    instanzinv.showitems()
    print(" ")
    for Food in invitems:
        if Food == "Apfel":
            print("Ein Apfel: " + str(instanzfoodapfel.string) + " Regeneration: " + str(instanzfoodapfel.foodpoints))
            fpick = input("Moechtest du den Apfel essen? ")
            if fpick == "Ja":
                instanzfoodapfel.eat1()

        if Food == "Trockenes Brot":
            print("Trockenes Brot: " + str(instanzfoodtrocken.string) + " Regeneration: " + str(instanzfoodtrocken.foodpoints)) 
            fpick = input("Moechtest du das Trockene Brot essen? ")
            if fpick == "Ja":
                instanzfoodtrocken.eat1()
        if Food == "Wildfleisch":
            print("Wildfleisch: " + str(instanzfoodwildfleisch.string) + " Regeneration: " + str(instanzfoodwildfleisch.foodpoints))
            fpick = input("Moechtest du das Wildfleisch essen? ")
            if fpick == "Ja":
                instanzfoodwildfleisch.eat1()
        if Food == "Karotte":
            print("Eine Karotte: " + str(instanzfoodapfel.string) + " Regeneration: " + str(instanzfoodapfel.foodpoints))
            fpick = input("Moechtest du die Karotte essen? ")
            if fpick == "Ja":
                instanzkarotte.eat1()
        if Food == "Erdapfel":
            print("Ein Erdapfel: " + str(instanzfoodapfel.string) + " Regeneration: " + str(instanzfoodapfel.foodpoints))
            fpick = input("Moechtest du den Erdapfel essen? ")
            if fpick == "Ja":
                instanzerdapfel.eat1()
        if Food == "Schweinefleisch":
            print("Schweinefleisch: " + str(instanzfoodapfel.string) + " Regeneration: " + str(instanzfoodapfel.foodpoints))
            fpick = input("Moechtest du das Schweinefleisch essen? ")
            if fpick == "Ja":
                instanzschweinefleisch.eat()
        if Food == "Rindfleisch":
            print("Rindfleisch: " + str(instanzfoodapfel.string) + " Regeneration: " + str(instanzfoodapfel.foodpoints))
            fpick = input("Moechtest du das Rindfleisch essen? ")
            if fpick == "Ja":
                instanzrindfleisch.eat1()
        if Food == "Maiskolben":
            print("Ein Maiskolben: " + str(instanzfoodapfel.string) + " Regeneration: " + str(instanzfoodapfel.foodpoints))
            fpick = input("Moechtest du den Maiskolben essen? ")
            if fpick == "Ja":
                instanzmaiskolben.eat1()
                

def looting():                                                                                  #Vorgange beim looten
    if tookloot == "Nichts":
            print(str(tookloot) + " gefunden. Vielleicht spaeter")
    else:
        print(" ")
        print(str(tookloot) + " gefunden!")
        invitems.append(str(tookloot))
        print(" ")
        
def superloot():
    global sloot
    sloot = ["Gold"]
    r = random.choice(sloot)
    print(" ")
    print(str(tookloot) + " gefunden!")
    invitems.append(str(tookloot))
    print(" ")
    instanzinv.showitems()
    
        
def sleeping():                                                                                 #Vorgange beim Schlafen
    if testforfailsleep == "fehlgeschlagen":
            if tooksleepfail == "Gegner ueberrascht dich":
                print("Ein Gegner hat dich ueberfallen. Du bist Tod")
                death()
                sys.exit()
            elif tooksleepfail == "Etwas gehoert":
                wastunsleep = input("Du hast irgendetwas gehoert. Was willst du tun? (schlafen, aufbleiben) ")
                if wastunsleep == "schlafen":
                    print("Du schlaefst weiter")
                    kons = random.choice(chance_to_failsleep)
                    if kons == "fehlgeschlagen":
                        print("Ein Gegner hat dich ueberfallen. Du bist Tod")
                        death()
                        sys.exit()
                    if kons == "ruhig":
                        print("Dein Schlaf war ruhig")
                if wastunsleep == "aufbleiben":
                    global amountired
                    amountired -= 10
            #   elif wastunsleep
            elif tooksleepfail == "Unbekannt":
                wastunsleep = input("Du bist aus irgeneinem Grund aufgewacht. Was willst du tun? (schlafen, aufbleiben) ")
                if wastunsleep == "schlafen":
                    print("Du schlaefst weiter")
                    kons = random.choice(chance_to_failsleep)
                    if kons == "fehlgeschlagen":
                        print("Ein Gegner hat dich ueberfallen. Du bist Tod")
                        death()
                        sys.exit()
                    if kons == "ruhig":
                        print("Dein Schlaf war ruhig")
    elif testforfailsleep == "ruhig":
        time.sleep(1)
        wait1()
        time.sleep(1)
        wait1()
        time.sleep(1)
        wait1()
        time.sleep(1)
        print("Dein Schlaf verlief ohne Stoerungen")
        

def verwenden():
    global invitems
    f = input("Was moechtest du verwenden? >")
    if f == "Buch":
        instanzbuch.verwenden()
    if f == "Zauberbuch":
        instanzzauberbuch.verwenden1()
            
def zaubern():
    z = 0
    print("=========")
    for s in instanzspellinv.sinvitems:
        print(s)
        print("-------")
        z += 1
    if z == 0:
        print("Du hast keine Zauber")
    print("=========")
    z = 0
    print("")
    r = input("Welchen Zauber willst du aktivieren? >")
    if r in instanzspellinv.sinvitems:
        if r == "Astralkoerper":
            instanzspellastralkoerper.trigger1()
        elif r == "Schnelligkeit1":
            instanzschnelligkeit1.trigger1()
        elif r == "Schnelligkeit2":
            instanzschnelligkeit2.trigger1()
        elif r == "Meditation":
            instanzmedi.trigger1()
   
cheatkeys = 0     
            
def cheatlist():
    global playergold
    global cheatkeys
    global invitems
    zeugs = loot()
    cc = True
    liste = ["stop", "exit", "Gold Rush", "Shop", "River", "giveItem", "ResetStats"]
    print("============================")
    for c in liste:
        print(c)
        print("--")
    print("============================")
    print("")
    while cc == True:
        r = input(">>")
        if r == "exit":
            sys.exit()
        elif r == "stop":
            break
        elif r == "Gold Rush":
            invitems.append("Gold")
            invitems.append("Gold")
            invitems.append("Gold")
        elif r == "Shop":
            print(instanzhaendler.sortiment)
            instanzhaendler.handeln()
        elif r == "River":
            instanzfluss.begegnung()
        elif r == "giveItem":
            c = input("Item: ")
            ca = input("Amount: ")
            try: 
                if c == "key":
                    cheatkeys += int(ca)
                elif c == "Gold":
                    playergold += int(ca)
                elif c == "Loot":
                    while int(ca) > 0:
                        ca = int(ca)
                        loot()
                        invitems.append(zeugs)
                        ca -= 1
                        if int(ca) == 0:
                            break
            except ValueError:
                print("[ERROR]:'{}' IS NO VALID COUNT".format(ca))
                cheatlist()
            ca = 0
        elif r == "ResetStats":
            amounthung == 0
            amountdurst == 0
            amountired == 0
            fcount == 0
            instanzmana.mana == 10       

def cheat():
    print("ACTIVATE CHEATS")
    time.sleep(1)
    print("FAILED")
    time.sleep(0.3)
    print("PASSWORD NEEDED")
    r = input("TYPE PASSWORD >>")
    if r == "Jonny_hat_Chiwawas_im_Keller":
        time.sleep(1.2)
        print("PERMISSION GRANTED")
        cheatlist()
    else:
        time.sleep(1.3)
        print("WRONG PASSWORD")
        print("PERMISSION DENIED")
        print("")
        print("")
        print("")
        print("BYE BYE")
        sys.exit()
        
    

def kampf():
    time.sleep(1)   
    fight()
    

            
# ~ while Ende == 0:                                                                                #Wiederholung
    # ~ game()
    # ~ print(" ")
    # ~ print("__________________________")
    # ~ print("Name des Spielers: " + str(nameplayer))
    # ~ print("Spielerklasse: " + str(classplayer))
    # ~ print("Leben: " + str(instanzleben.leben))
    # ~ print("Tag: " + str(tag))
    # ~ print("Zeit: " + str(time1))
    # ~ print("Hunger: " + str(amounthung) + " ,Ist 10 erreicht, stirbst du.")
    # ~ print("Durst: " + str(amountdurst) + " ,Ist 7 erreicht, stirbst du")
    # ~ print("Muedigkeit: " + str(amountired))
    # ~ print("__________________________")
    # ~ print(" ")
    # ~ end = input("weiterspielen? (Ja, Nein) ")
    # ~ print(" ")
    # ~ if end == Nein:
        # ~ Ende = 1
    # ~ if end == food_express:
        # ~ invitems.append("Trockenes Brot")
        # ~ print("Item Trockenes Bort erhalten!")
    # ~ if end == water_express:
        # ~ invitems.append("Wasser")
        # ~ print("Item Wasser erhalten")
    # ~ if end == resetstats:
        # ~ amounthung = 0
        # ~ amountdurst = 0
        # ~ amountired = 0
        # ~ print("Statuswerte zurueckgesetzt!")
    # ~ if amounthung == 10:
        # ~ stathung = "Tod"
        # ~ print("Du Verhungerst")
        # ~ death()
        # ~ sys.exit()
    # ~ if amountdurst >= 7:
        # ~ statdurst = "Tod"
        # ~ print("Du Verdurstest")
        # ~ death()
        # ~ sys.exit()
    # ~ if instanzleben.leben <= 0:
        # ~ print("Du hast keine Leben mehr")
        # ~ death()
        # ~ sys.exit()
    # ~ if time1 >= 24:
        # ~ tag += 1
        # ~ time1 = 0
    # ~ tookloot = random.choice(kindsloot)
    # ~ testforfailsleep = random.choice(chance_to_failsleep)
    # ~ tooksleepfail = random.choice(kindssleepfail)
    # ~ fightrandom1 = random.randint(-1000,9)
    # ~ fightrandom2 = random.randint(11, 1000)
            

def goldconvert():
    global playergold
    for gold in invitems:
        if gold == "Gold":
            playergold += 1
            invitems.remove("Gold")

def welcome():                                                                    
    print(" ")
    print(" ")
    print("_____________________________________________________________________________________________________________________________________________")
    print("|....|..____|.........../ __ \.........|  \............./  |...|  _____|........./  ____  \...\ \............./ /...|  _____|...|  ___  \....|")
    print("|....| |.............../ /..\ \........| | \.........../ | |...| |...............| |....| |....\ \.........../ /....| |.........| |...| |....|")
    print("|....| |___.........../ /____\ \.......| |\ \........./ /| |...| |____...........| |....| |.....\ \........./ /.....| |____.....| |___/ |....|")
    print("|....| .___|........./ ________ \......| |.\ \......./ /.| |...|  ____|..........| |....| |......\ \......./ /......|  ____|....| |____/.....|")
    print("|....| |............/ /........\ \.....| |..\ \...../ /..| |...| |...............| |....| |.......\ \...../ /.......| |.........|   \........|")
    print("|....| |.........../ /..........\ \....| |...\ \.../ /...| |...| |...............| |....| |........\ \.../ /........| |.........| |\ \ ......|")
    print("|....| |___......./ /............\ \...| |....\ \_/ /....| |...| |_____..........| |____| |.........\ \_/ /.........| |_____....| |.\ \......|")
    print("|....\______...../_/..............\_\..|_|.....\___/.....|_|...|_______|.........\________/..........\___/..........|_______|...|_|..\_\.....|")
    print("|_____________________________________________________________________________________________________________________________________________")
    print(" ")
    print(" ")

def death():                                                                    
    print(" ")
    print(" ")
    print("_____________________________________________________________________________________________________________________________________________")
    print("|..../  ______|........./ __ \.........|  \............./  |...|  _____|........./  ____  \...\ \............./ /...|  _____|...|  ___  \....|")
    print("|....| /.............../ /..\ \........| | \.........../ | |...| |...............| |....| |....\ \.........../ /....| |.........| |...| |....|")
    print("|....| |............../ /____\ \.......| |\ \........./ /| |...| |____...........| |....| |.....\ \........./ /.....| |____.....| |___/ |....|")
    print("|....| |............./ ________ \......| |.\ \......./ /.| |...|  ____|..........| |....| |......\ \......./ /......|  ____|....| |____/.....|")
    print("|....| |..__......../ /........\ \.....| |..\ \...../ /..| |...| |...............| |....| |.......\ \...../ /.......| |.........|   \........|")
    print("|....| |.|_ \....../ /..........\ \....| |...\ \.../ /...| |...| |...............| |....| |........\ \.../ /........| |.........| |\ \ ......|")
    print("|....| |__| |...../ /............\ \...| |....\ \_/ /....| |...| |_____..........| |____| |.........\ \_/ /.........| |_____....| |.\ \......|")
    print("|....\_____|...../_/..............\_\..|_|.....\___/.....|_|...|_______|.........\________/..........\___/..........|_______|...|_|..\_\.....|")
    print("|_____________________________________________________________________________________________________________________________________________")
    print(" ")
    print(" ")

def difficult():
    print("")
    print("Mit welcher Schwierigkeit willst du spielen?")
    print("")
    print("[easy]    [hard]")
    print("")
    r = input(">>")
    if r == "easy":
        global difficulty
        difficulty = "easy"
    elif r == "hard":
        difficulty = "hard"
    elif r == "?":
        print("")
        print("[easy]:")
        print("Der Spieler muss nicht essen, trinken, und schlafen")
        print("")
        print("[hard]:")
        print("Der Spieler muss essen, trinken, schlafen, sonst stirbt er")
        print("")
        difficult()
    else:
        print("Das ist kein gueltiger Schwierigkeitsgrad.")
        difficult()
    print("")
    print("")

def roundend():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
difficult()


print(" ")
print("===================================================================================================================")
print("Willkommen. Du bist ein Reisender und bist in einem fremden Land nach Ausschau auf verborgene Schaetze.")    #einfuhrung
print("Als du dich eines Nachts schlafen legst, erwachst du in einem Dungeon. Finde jetzt den Weg hinaus.Viel Glueck!")
print("===================================================================================================================")
print(" ")
nameplayer = input("Wie lautet dein Name? ")
if nameplayer == "":
    nameplayer = "Unbekannt"
if nameplayer[0:5] == "Jonny":
    print("Hi Jonny, Viel Spass!")
classquestion()                                             #Frage des Name                                                 #Ausgabe des Namen

if nameplayer[0:5] == "Jonny":
    if classplayer == "Jaeger":
        print("")
        print("Wieder am Chiwawa jagen Jonny? ")
        print("")

print(" ")                                                                                      #Daten des Spiels
print("Name des Spielers: " + str(nameplayer))
print("Spielerklasse: " + str(classplayer)) 

testforclass()
    
print("Tag Nr.:" + str(tag))
print(" ")
print(" ")


def game(levels , playerx=1, playery=1, playerhp=50):
    difficult1 = difficult
    p = Player(playerx, playery, playerhp)              # Spieler startet mit 50 hitpoints auf Position x:1,y:1
    status = ""
    while p.hitpoints > 0:            # so lange der player mehr als null hitpoints hat
        global cheatkeys
        global nameplayer
        global classplayer
        global amountired
        global tookloot
        global tooksleepfail
        global testforfailsleep
        global amounthung
        global amountdurst
        global time1
        global tag
        global fcount
        global rcount
        global difficulty
        level = levels[p.z]
        level.paint(p.x, p.y)
        print(status)               
        dx, dy = 0, 0
        ddx, ddy = 0, 0
        npcx = 0.3
        if instanzspellastralkoerper.immune == True:
            level.immune = True
            instanzspellastralkoerper.immune = False
        if amounthung >= 27:
            if difficulty == "hard":
                print("")
                print("Du bist verhungert")
                break
        if amountdurst >= 24:
            if difficulty == "hard":
                print("")
                print("Du bist verdurstet")
                break
        if amountired >= 30:
            if difficulty == "hard":
                print("")
                print("Du stirbst an Erschoepfung")
                break
        status = ""                   # ----------- ask ----------------------  
        print("Tag:{}, Zeit:{}, Name:{}, {} ".format(time1, tag, nameplayer, classplayer))
        print("_____")
        wastun = input("hp:{} Mana: {} keys:{} h/d/t/f:{}, {}, {}, {} was nun?>".format(p.hitpoints, instanzmana.mana, p.keys, amounthung, amountdurst, amountired, fcount))
        if wastun == "looten":
            if amountired <= 17:
                looting()
                time1 += random.randint(2, 5)
                amounthung += 1 
                amountdurst += 1
                amountired += 1
                instanzfluss.begegnung()
                tookloot = random.choice(kindsloot)
                testforfailsleep = random.choice(chance_to_failsleep)
                tooksleepfail = random.choice(kindssleepfail)
            else:
                print("Du bist zu muede um zu looten")
                continue
        elif wastun == "l":
            if amountired <= 17:
                looting()
                time1 += 3
                amounthung += 1 
                amountdurst += 1
                amountired += 1
                instanzfluss.begegnung()
                tookloot = random.choice(kindsloot)
                testforfailsleep = random.choice(chance_to_failsleep)
                tooksleepfail = random.choice(kindssleepfail)
            else:
                print("Du bist zu muede um zu looten")
                continue
        elif wastun == "Activate Cheat-Console":
            cheat()
        elif wastun == "z":
            zaubern()
        elif wastun == "reden":
            print("Hier ist niemand mit dem du reden kannst.")
        elif wastun == "si":
            z = 0
            print("")
            print("=======")
            for b in instanzspellinv.sinvitems:
                print(b)
                print("----")
                z += 1
            if z == 0:
                print("Du hast keine Zauber.")
            print("=======")
            print("")
            z = 0
        elif wastun == "v":
            verwenden()
        elif wastun == "p":
            level.place(p.x, p.y)
        elif wastun == "schlafen":
            tookloot = random.choice(kindsloot)
            testforfailsleep = random.choice(chance_to_failsleep)
            tooksleepfail = random.choice(kindssleepfail)
            sleeping()
            tag += 1
            amounthung += 2 
            amountdurst += 2
            amountired = 0
        elif wastun == "sch":
            sleeping()
            tag += 1
            amounthung += 2 
            amountdurst += 2
            amountired = 1
            tookloot = random.choice(kindsloot)
            testforfailsleep = random.choice(chance_to_failsleep)
            tooksleepfail = random.choice(kindssleepfail)
        elif wastun == "inventar":
            print(" ")
            instanzinv.showitems()
            print(" ") 
            time1 += 1
            continue
        elif wastun == "i":
            print(" ")
            instanzinv.showitems() 
            print(" ")
            time1 += 1
            continue
        elif wastun == "essen":
            eating()
        elif wastun == "e":
            eating()
        elif wastun == "trinken":
            drinking()
        elif wastun == "t":
            drinking()
        elif wastun == "craften":
            crafting()
        elif wastun == "c":
            crafting()
        elif wastun == "Faehigkeit":
            if fcount <= 3:
                Faehigkeit()
                fcount += 1
            else:
                print("Du hast deine Faehigkeit bereits 3 Mal eingesetzt.")
        elif wastun == "f":
            if fcount <= 2:
                Faehigkeit()
                fcount += 1
            else:
                print("Du hast deine Faehigkeit bereits 3 Mal eingesetzt.")
        elif wastun == "Ruestung":
            equipruestung()
        elif wastun == "r":
            equipruestung()
      #  else:
      #      print("Dein Input wurde nicht erkannt, bitte schreibe die Vorschlaege in der Klammer oder deren Anfangsbuchstaben")
      #      continue
        elif wastun == "exit" or a == "quit" or a == "Q":  # ----- quit ------
            break    
        # ~ elif wastun == "i":                # --------- inventory --------
            # ~ p.zeige_rucksack()
            # ~ wait()
            # ~ continue
        elif wastun == "?" or a == "help":  # ---- help -------
            hilfe()
            continue
        elif wastun == "a":                   # ------------- Bewegung ---------
            dx -= 1
            amounthung += 1 
            amountdurst += 1
            amountired += 1
            time1 += 1
        elif wastun == "d":
            dx += 1
            amounthung += 1 
            amountdurst += 1
            amountired += 1
            time1 += 1
        elif wastun == "w":
            dy -= 1
            amounthung += 1 
            amountdurst += 1
            amountired += 1
            time1 += 1
        elif wastun == "s":
            dy += 1
            amounthung += 1 
            amountdurst += 1
            amountired += 1
            time1 += 1
        elif wastun == "aa":
            if instanzschnelligkeit1.doppelt == True:
                dx -= 1
                amounthung += 1 
                amountdurst += 1
                amountired += 1
                time1 += 1
                rcount += 1
                ddx -= 1
            elif instanzschnelligkeit2.dreimal == True:
                dx -= 1
                amounthung += 1 
                amountdurst += 1
                amountired += 1
                time1 += 1
                rcount += 1
                ddx -= 2
            else:
                time1 += random.randint(2, 5)
                amounthung += 1 
                amountdurst += 1
                amountired += 1
                wait()
        elif wastun == "ww":
            if instanzschnelligkeit1.doppelt == True:
                dy -= 1
                amounthung += 1 
                amountdurst += 1
                amountired += 1
                time1 += 1
                rcount += 1
                ddy -= 1
            elif instanzschnelligkeit2.dreimal == True:
                dy -= 1
                amounthung += 1 
                amountdurst += 1
                amountired += 1
                time1 += 1
                rcount += 1
                ddy -= 2
            else:
                time1 += random.randint(2, 5)
                amounthung += 1 
                amountdurst += 1
                amountired += 1
                wait()
        elif wastun == "dd":
            if instanzschnelligkeit1.doppelt == True:
                dx += 1
                amounthung += 1 
                amountdurst += 1
                amountired += 1
                time1 += 1
                rcount += 1
                ddx += 1
            elif instanzschnelligkeit2.dreimal == True:
                dx += 1
                amounthung += 1 
                amountdurst += 1
                amountired += 1
                time1 += 1
                rcount += 1
                ddx += 2
            else:
                time1 += random.randint(2, 5)
                amounthung += 1 
                amountdurst += 1
                amountired += 1
                wait()
        elif wastun == "ss":
            if instanzschnelligkeit1.doppelt == True:
                dy += 1
                amounthung += 1 
                amountdurst += 1
                amountired += 1
                time1 += 1
                rcount += 1
                ddy += 1
            elif instanzschnelligkeit2.dreimal == True:
                dy += 1
                amounthung += 1 
                amountdurst += 1
                amountired += 1
                time1 += 1
                rcount += 1
                ddy += 2
            else:
                time1 += random.randint(2, 5)
                amounthung += 1 
                amountdurst += 1
                amountired += 1
                wait()
        elif wastun == "o":                 # ------ level up
            if level.lines[p.y][p.x] != "<":
                status = "Du musst erst eine Stiege nach oben finden [<]"
                continue
            elif p.z == 0:
                print("Du verlaesst den Dungeon und kehrst zurueck an die Oberflaeche")
                break
            p.z -= 1
        elif wastun == "u":                  # ------ level down
            if level.lines[p.y][p.x] != ">":
                status = "Du musst erst eine Stiege nach unten finden [>]"
                continue
            p.z += 1
        elif wastun == "q":                  # --------- Heiltrank ------------
            if "Heiltrank" in p.rucksack and p.rucksack["Heiltrank"] > 0:
                p.rucksack["Heiltrank"] -= 1
                effekt = random.randint(2, 5)
                p.hitpoints += effekt
                status = "Du trinkst einen Heiltrank und erhaelst {} hitpoints".format(effekt)
            else:
                status = "in Deinem Rucksack befindet sich kein Heiltrank. Sammle Loot!"
        else:
            time1 += random.randint(2, 5)
            amounthung += 1 
            amountdurst += 1
            amountired += 1
            wait()

        wohin = level.lines[p.y+dy][p.x+dx] # ----- testen ob spieler gegen Wand, Monster oder Tuer laeuft ----
        monster = level.is_monster(p.x+dx, p.y+dy)
        npc = level.is_npc(p.x+dx, p.y+dy)
        if monster:
            if level.immune == False:
                kampfrunde(p, monster)
                kampfrunde(monster, p)
            elif level.immune == True:
                p.x += dx
                p.y += dy
                p.x += ddx
                p.y += ddy
                level.immune == False
        elif npc:
            if level.immune == False:
                npc.reden()
                status = npc.status
                cbc = input(">")
                if cbc == "reden":
                    npc.weiter()
                    if npc.visit == True:
                        safez = p.z
                        safex = p.x
                        safey = p.y
                        p.z = npc.haus
                npc.visit == False
                npcx = 0.0
            elif level.immune == True:
                p.x += dx
                p.y += dy 
                p.x += ddx
                p.y += ddy
                level.immune = False
        elif wohin == "#":
            if level.immune == False:         # in die Wand gelaufen?
                status = "aua, nicht in die Wand laufen!"
                p.hitpoints -= 1
                if p.hitpoints == 0:
                    print("Du bist an einer Wand gestorben. Gluekwuensch!")
                    print("")
            elif level.immune == True:
                p.x += dx
                p.y += dy
                p.x += ddx 
                p.y += ddy
                level.immune = False
        elif wohin == "F":
            if level.immune == False:
                status = "Feuerstelle wird benutzt"
                instanzfeuerstelle.anzuenden()
            else:
                p.x += dx
                p.y += dy
                p.x += ddx
                p.y += ddy
                level.immune = False
        elif wohin == "c":
            if level.immune == False:
                status = "Truhe wird benutzt!"
                instanztruhe.fragen()
        elif wohin == "A":
            if level.immune == False:
                status = "Zauberaltar wird benutzt!"
                instanzzauberaltar.verzaubern()
            else:
                p.x += dx
                p.y += dy
                p.x += ddx
                p.y += ddy
                level.immune = False
        elif wohin == "U":
            if level.immune == False:
                status = "Braustand wird benutzt!"
                instanzcraftingrezbraustand.brauen()
            elif level.immune == True:
                p.x += dx
                p.y += dy
                p.x += ddx
                p.y += ddy
                level.immune = False
        elif wohin == "H":
            instanzhaendler.handeln()
        elif wohin == "D":
            if level.immune == False:
                if p.z >= 2:
                    r = input("Willst du das Haus verlassen? >")
                    if r == "Ja":
                        p.z = safez
                        p.x = safex
                        p.y = safey
                        continue
                if p.keys > 0:
                    p.keys -= 1
                    status = "Tuere aufgesperrt (1 Schluessel verbraucht)"
                    level.ersetze(p.x+dx, p.y+dy, ".") 
                elif p.keys < 0:
                    status = "Aua! Du knallst gegen eine versperrte Tuere"
                    p.hitpoints -= 1
            elif level.immune == True:
                p.x += dx
                p.y += dy
                p.x += ddx
                p.y += ddy
                level.immune = False
        else:
            p.x += dx
            p.y += dy 
            p.x += ddx
            p.y += ddy  # ----------------- spieler ist an einer neuen position --------
        wo = level.lines[p.y][p.x]                # wo bin ich jetzt
        trap = level.is_trap(p.x, p.y)
        if level.immune == False:
            if trap:
                #elif wo == "T":                           # in die Falle gelaufen?
                schaden = trap.damage()
                status = "aua, in die Falle gelaufen. {} Schaden!".format(schaden)
                p.hitpoints -= schaden
                trap.hitpoints -= random.randint(1,4)
                trap.visible = 0
        elif level.immune == True:
            p.x += dx
            p.y += dy
            p.x += ddx
            p.y += ddy

        for dx, dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            trap =  level.is_trap(p.x+dx, p.y+dy)
            if trap:
                
                if classplayer == "Jaeger":
                    if random.random() < .4:  # 40% chance
                        trap.visible = True
                else:
                    if random.random() < .1:  # 10% chance
                        trap.visible = True
                    
        
        if wo in "123456789":
                status = "hier steht: " + level.schilder[wo]
        elif wo == "k":                           # schluessel gefunden? 
            status = "Schluessel gefunden!"
            p.keys += 1
            level.ersetze(p.x, p.y, ".")
        elif wo == "L":                           # Loot gefunden ?
            p.nimm(loot())
            level.ersetze(p.x, p.y, ".")
        elif wo == "Y":                           # Loot gefunden ?
            superloot()
            level.ersetze(p.x, p.y, ".")
        elif wo == "<":
            status = "Stiege rauf: [o] druecken und [Enter] zum raufgehen"
        elif wo == ">":
            status = "Stiege runter: [u] druecken und [Enter] zum runtergehen"
        goldconvert()
        level.update()                             # tote monster loeschen
        level.move_monster(p)                     # lebende monster bewegen
        if random.random() < npcx:
            level.move_npc(p)
        if rcount == 6:
            instanzschnelligkeit1.doppelt = False
            instanzschnelligkeit2.dreimal = False
            status = "Zauber Schnelligkeit ist verflogen"
            rcount = 0
        p.keys += cheatkeys
        cheatkeys = 0
#        roundend()
    print("Game Over. Hitpoints: {}".format(p.hitpoints))
    if p.hitpoints < 1:
        print("Du bist tot")
    instanzinv.showitems()
    print("")
    death()



if __name__ == "__main__":
    # Spieler startet in level1.txt auf position x1,y1 mit 50 hitpoints
    game([Level("level1demo.txt"), Level("level2demo.txt"), Level("Room1.txt"), Level("Room2.txt")], 1, 1, 50)
