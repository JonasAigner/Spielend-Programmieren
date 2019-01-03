import sys, random, time

def sagab(s):
    for a in s:
        print(a)
        
def sagabno(s, x=""):
    for a in s:
        print(a, end=x)
        
def showhelp():
    print("")
    print("============================================")
    print("[ENTER].....................Runde beginnen")
    print("'stop'......................Spiel beenden")
    print("'help', '?', 'help'.........Hilfstext anzeigen")
    print("============================================")
        
def new():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

class Image():
    def __init__(self, n, x):
        self.name = n
        self.x = x
        self.list = []
        
    def setpicture(self):
        y = open(self.x, "r")
        for line in y:
            self.list.append(line)
            
class Reihe():
    def __init__(self):
        self.reihe = []
        self.symbols = ["Geldsack", "Nix", "Nix", "Nix"]
        self.z = ""
        self.freihe = []
        
    def build(self):
        self.freihe = []
        self.reihe = []
        while len(self.reihe) < 4:
            self.z = random.choice(self.symbols)
            self.reihe.append(self.z)
        for geld in self.reihe:
            if geld == "Geldsack":
                self.freihe.append(Geldsack)
            elif geld == "Nix":
                self.freihe.append(Nix)
            
Geldsack = Image("Geldsack", "Geldsack.txt")
Nix = Image("Nix", "Nichts.txt")
TTTNix = Image("tttnix", "TTTNix.txt")
TTTKreis = Image("tttkreis", "TTTKreis.txt")
TTTIX = Image("tttix", "TTTIX.txt")
Reihe = Reihe()

Geldsack.setpicture()
Nix.setpicture()
TTTNix.setpicture()
TTTKreis.setpicture()
TTTIX.setpicture()

geld = 50

class TTT():
    def __init__(self):
        self.symbols = ["Nix", "Kreis", "IX"]
        self.reihe = []
        self.freihe = []

    def buildclean(self):
        self.reihe = []
        self.freihe = []
        while len(self.reihe) < 9:
            self.reihe.append("Nix")


    def build(self):
        pass

    def round(self):
        global geld
        geld -= 10
        new()





class Versuch():
    def __init__(self):
        self.gewinn = False
        self.reihe = []
        self.geldsack = 0
        self.z = 0
        self.r1 = []
        self.r2 = []
        self.r3 = []
        self.r4 = []
        self.r5 = []
        self.r6 = []
        self.r7 = []
        self.r8 = []
        self.r9 = []
    
    
    def build(self):
        print("========================================================================================")
        for linie in self.reihe:
            self.r1.append(linie.list[self.z])
        self.z += 1
        rr1 = str(self.r1)
        n1r1 = rr1.replace("[", "")
        n2r1 = n1r1.replace("]", "")
        n3r1 = n2r1.replace("\\n", "")
        n4r1 = n3r1.replace(",", "")
        n5r1 = n4r1.replace("'", "")
        print(n5r1)
        
        for linie in self.reihe:
            self.r2.append(linie.list[self.z])
        rr2 = str(self.r2)
        n1r2 = rr2.replace("[", "")
        n2r2 = n1r2.replace("]", "")
        n3r2 = n2r2.replace("\\n", "")
        n4r2 = n3r2.replace(",", "")
        n5r2 = n4r2.replace("'", "")
        print(n5r2)
        self.z += 1
        
        for linie in self.reihe:
            self.r3.append(linie.list[self.z])
        rr3 = str(self.r3)
        n1r3 = rr3.replace("[", "")
        n2r3 = n1r3.replace("]", "")
        n3r3 = n2r3.replace("\\n", "")
        n4r3 = n3r3.replace(",", "")
        n5r3 = n4r3.replace("'", "")
        print(n5r3)
        self.z += 1
        
        for linie in self.reihe:
            self.r4.append(linie.list[self.z])
        rr4 = str(self.r4)
        n1r4 = rr4.replace("[", "")
        n2r4 = n1r4.replace("]", "")
        n3r4 = n2r4.replace("\\n", "")
        n4r4 = n3r4.replace(",", "")
        n5r4 = n4r4.replace("'", "")
        print(n5r4)
        self.z += 1
        
        for linie in self.reihe:
            self.r5.append(linie.list[self.z])
        rr5 = str(self.r5)
        n1r5 = rr5.replace("[", "")
        n2r5 = n1r5.replace("]", "")
        n3r5 = n2r5.replace("\\n", "")
        n4r5 = n3r5.replace(",", "")
        n5r5 = n4r5.replace("'", "")
        print(n5r5)

        self.z += 1
        for linie in self.reihe:
            self.r6.append(linie.list[self.z])
        rr6 = str(self.r6)
        n1r6 = rr6.replace("[", "")
        n2r6 = n1r6.replace("]", "")
        n3r6 = n2r6.replace("\\n", "")
        n4r6 = n3r6.replace(",", "")
        n5r6 = n4r6.replace("'", "")
        print(n5r6)

        self.z += 1
        for linie in self.reihe:
            self.r7.append(linie.list[self.z])
        rr7 = str(self.r7)
        n1r7 = rr7.replace("[", "")
        n2r7 = n1r7.replace("]", "")
        n3r7 = n2r7.replace("\\n", "")
        n4r7 = n3r7.replace(",", "")
        n5r7 = n4r7.replace("'", "")
        print(n5r7)

        self.z += 1
        for linie in self.reihe:
            self.r8.append(linie.list[self.z])
        rr8 = str(self.r8)
        n1r8 = rr8.replace("[", "")
        n2r8 = n1r8.replace("]", "")
        n3r8 = n2r8.replace("\\n", "")
        n4r8 = n3r8.replace(",", "")
        n5r8 = n4r8.replace("'", "")
        print(n5r8)
        print("========================================================================================")
        self.z = 0
        self.r1 = []
        self.r2 = []
        self.r3 = []
        self.r4 = []
        self.r5 = []
        self.r6 = []
        self.r7 = []
        self.r8 = []
        self.r9 = []
        

        
    
    def round(self):
        global geld
        geld -= 10
        new()
        Reihe.build()
        self.reihe = Reihe.freihe
        self.build()
        self.z = 0
        for geldsack in self.reihe:
            if geldsack.name == "Geldsack":
                self.geldsack += 1
        print("")
        print("Geldsaecke:{}".format(self.geldsack))
        gewinn()
        self.geldsack = 0
        self.reihe = []
        print(Reihe.freihe)
        
        
        
Versuch = Versuch()


def gewinn():
    global geld
    if Versuch.geldsack == 0:
        print("Du hast leider nichts gewonnen. Probier es noch mal!")
    elif Versuch.geldsack == 1:
        print("Du hast leider nichts gewonnen. Probier es noch mal!")
    elif Versuch.geldsack == 2:
        print("Du hast leider nichts gewonnen. Probier es noch mal!")
    elif Versuch.geldsack == 3:
        print("")
        print("- - - - - - - - - - - -")
        print("Glueckwunsch! Du hast 100 Euro gewonnen!")
        print("- - - - - - - - - - - -")
        print("")
        geld += 100
    elif Versuch.geldsack == 4:
        print("")
        print("")
        print("=====================================")
        print("JACKPOT!!!!!! DU hast 250 Euro gewonnen!")
        print("=====================================")
        print("")
        print("")
        geld += 250
    print("Geld:{}".format(str(geld)))
    r = input(">>")
    Versuch.geldsack = 0
    if r == "":
        Versuch.round()
    elif r == "stop":
        print("Dein Geld:{} (Anfangs 50 Euro)".format(geld))
        sys.exit()
    else:
        Versuch.round()

def Automat():
    print("=============================================================")
    print("WILKOMMEN BEIM RANDOMATOR 3000!!")
    print("=============================================================")
    print("")
    print("                   ##")
    print("                   # ##")
    print("                   #  ##")
    print("####################   ##")
    print("#                       ##")
    print("#                        ##")
    print("#                       ##")
    print("#                      ##")
    print("####################  ##")
    print("                   # ##")
    print("                   ###")
    print("                   ##")
    r = input(">>")
    if r == "":
        Versuch.round()
    elif r == "Stop":
        print("Dein Geld:{} (Anfangs 50 Euro)".format(geld))
        sys.exit()
    elif r == "help":
        showhelp()
        Versuch.round()
    elif r == "?":
        showhelp()
        Versuch.round()
    elif r == "hilfe":
        showhelp()
        Versuch.round()
    else:
        Versuch.round()

def Lotto():
    print("Zahlen von 1 - 20")
    global geld
    true = True
    while true == True:
        geld -= 5
        print("Geld:{}".format(str(geld)))
        r = input("Gib deine Zahl ein! >>")
        z = random.randint(1, 20)
        try:
            if int(r) == z:
                print("")
                print("")
                print("===================")
                print("GEWONNEN!!!")
                print("===================")
                print("")
                print("")
                geld += 400
        except ValueError:
                print("Bitte gib ein Zahl ein!")
                continue
        if r == "stop":
            print("Dein Geld:{} (Anfangs 50 Euro)".format(geld))
            sys.exit()
        else:
            print("Leider nicht gewonnen. Die Zahl war {}".format(z))

def STP():
    global geld
    true = True
    glist = ["Schere", "Stein", "Papier"]
    while true == True:
        print("Geld:{}".format(str(geld)))
        ex = ""
        print("")
        print("    [Schere]    [Stein]    [Papier]")
        r = input(">>")
        if r == "Schere":
            ex = "Schere"
        elif r == "Stein":
            ex = "Stein"
        elif r == "Papier":
            ex = "Papier"
        else:
            print("Gib [Schere] [Stein] oder [Papier] ein!")
            STP()
        gex = random.choice(glist)
        print("Gegner hat {}".format(gex))
        if gex == ex:
            print("Unentschieden!")
            continue
        elif gex == "Stein" and ex == "Schere":
            print("Du hast leider verloren")
            geld -= 20
        elif gex == "Stein" and ex == "Papier":
            print("Du hast gewonnen!")
            geld += 20
        elif gex == "Schere" and ex == "Papier":
            print("Du hast leider verloren")
            geld -= 20
        elif gex == "Schere" and ex == "Stein":
            print("Du hast gewonnen!")
            geld += 20
        elif gex == "Papier" and ex == "Schere":
            print("Du hast gewonnen!")
            geld += 20
        elif gex == "Papier" and ex == "Stein":
            print("Du hast leider verloren")
            geld -= 20
        else:
            print("Fehler!")

def tictacto():
    ttt.build()
    if random.random() < 0.5:
        print("Du bist am Zug!")
        ttt.zug()
    else:
        print("Der Gegner ist am Zug!")
        ttt.gzug()

g = input("Was willst du spielen? [Lotto, Automat, STP] >")
if g == "Lotto":
    Lotto()
elif g == "Automat":
    Automat()
elif g == "STP":
    STP()
else:
    print("OK")
        






