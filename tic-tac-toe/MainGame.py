import pygame, time, random, sys

#Test Game to try out pygame for python 3
#Game: Tic Tac Toe
#
#Known problems: event keys doesn't work, how to show input text?

print("")
print("Wähle Symbol für Player 1. [X] [O]")
playersymbol = input(">>")


pygame.init()    #calls pygame
screen = pygame.display.set_mode((500, 500))   #screen has 500*500 pixel
pygame.display.set_caption("First Game")       #name of pygame screen
clock = pygame.time.Clock()                    #clock

CLEAN = pygame.image.load("clear_field.png")     #Load Images
X = pygame.image.load("X-character.png")
O = pygame.image.load("Kreis.png")
SEL = pygame.image.load('select.png')

sx = 0    # x and y position of Selection
sy = 0
xx = 0    # x and y of field on Selection
yy = 0

mir1 = None
mir2 = None
mir3 = None
winsym = None
unentschieden = None

marked = {"00" : "not", "01" : "not", "02" : "not",         # shows on wich field is a 'X' or an 'O'
          "10" : "not", "20" : "not", 
          "11" : "not", "12" : "not",
          "21" : "not", "22" : "not"}

co = {"00" : "0 0", "01" : "0 175", "02" : "0 350",         # coordinates of the relative field coordinates (xx, yy)
      "10" : "175 0", "20" : "350 0",
      "11" : "175 175", "12" : "175 350",
      "21" : "350 175", "22" : "350 350"}
      
fields = {"00" : "1", "10" : "2", "20" : "3",
          "01" : "4", "11" : "5", "21" : "6",
          "02" : "7", "12" : "8", "22" : "9"}

reihe1 = ["1", "2", "3"]
reihe2 = ["4", "5", "6"]
reihe3 = ["7", "8", "9"]
reihe4 = ["1", "4", "7"]
reihe5 = ["2", "5", "8"]
reihe6 = ["3", "6", "9"]
reihe7 = ["1", "5", "9"]
reihe8 = ["3", "5", "7"]

#plate:   ["1", "2", "3"]

#         ["4", "5", "6"]

#         ["7", "8", "9"]
          
reihen = [reihe1, reihe2, reihe3, reihe4, reihe5, reihe6, reihe7, reihe8] 

def write(background, text, x=50, y=150, color=(0,0,0),             # write function to show text    Made by: Horst Jens on Github
          fontname="mono", fontsize=None, center=False):
        """write text on pygame surface. """
        if fontsize is None:
            fontsize = 24
        font = pygame.font.SysFont(fontname, fontsize, bold=True)
        fw, fh = font.size(text)
        surface = font.render(text, True, color)
        if center: # center text around x,y
            background.blit(surface, (x-fw//2, y-fh//2))
        else:      # topleft corner is x,y
            background.blit(surface, (x,y))

def quitt():                                    # event quit
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def test_marked_in_reihe(coord):
    for fm in marked.items():
        if coord == fm[0]:
            if fm[1] == "markedO":
                return "O"
            elif fm[1] == "markedX":
                return "X"
            else:
                return "not"
            break
    

def test_o_or_x(cord, times):
    global mir1
    global mir2
    global mir3
    if times == 0:
        if test_marked_in_reihe(cord) == "O":
            mir1 = "O"
        elif test_marked_in_reihe(cord) == "X":
            mir1 = "X"
        elif test_marked_in_reihe(cord) == "not":
            mir1 = "not"
    elif times == 1:
        if test_marked_in_reihe(cord) == "O":
            mir2 = "O"
        elif test_marked_in_reihe(cord) == "X":
            mir2 = "X"
        elif test_marked_in_reihe(cord) == "not":
            mir2 = "not"
    elif times == 2:
        if test_marked_in_reihe(cord) == "O":
            mir3 = "O"
        elif test_marked_in_reihe(cord) == "X":
            mir3 = "X"
        elif test_marked_in_reihe(cord) == "not":
            mir3 = "not"
    print(str(cord) + " " + str(times))
        

def win(sym):
    global winsym
    winsym = sym
    
def unentschieden_run():
    global unentschieden
    unentschieden = True
    for m in marked.items():
        if m[1] == "not":
            unentschieden = False
            break

def test_reihe():
    for reihe in reihen:
        t = 0
        for feld in reihe:
            t = 0
            for z in fields.items():
                if feld == z[1]:
                    m = z[0]
                    test_o_or_x(m, t)
                    t += 1
                    if mir1 == "O" and mir2 == "O" and mir3 == "O":
                        win("O")
                    elif mir1 == "X" and mir2 == "X" and mir3 == "X":
                        win("X")


        

def draw_symbol():                     # draws symbol on marked field
    ssx = ""
    ssy = ""
    for m in marked.items():
        if m[1] == "markedO":              # draws 'O'
            z = list(m[0])
            z1 = str(z[0])
            z2 = str(z[1])
            for w in co.items():
                if w[0] == z1 + z2:
                    pas = False
                    for i in w[1]:
                        if pas == True:
                            ssy += i
                        elif i != " ":
                            ssx += i
                        else:
                            pas = True
            screen.blit(O, (int(ssx), int(ssy)))
            ssx = ""
            ssy = ""
        elif m[1] == "markedX":           # draws 'X'
            z = list(m[0])
            z1 = str(z[0])
            z2 = str(z[1])
            for w in co.items():
                if w[0] == z1 + z2:
                    pas = False
                    for i in w[1]:
                        if pas == True:
                            ssy += i
                        elif i != " ":
                            ssx += i
                        else:
                            pas = True
            screen.blit(X, (int(ssx), int(ssy)))
            ssx = ""
            ssy = ""

def draw():           # draws all and update display
    global sx
    global sy
    screen.fill((0, 0, 0))
    screen.blit(CLEAN, (0, 0))
    screen.blit(SEL, (sx, sy))
    draw_symbol()
    pygame.display.update()
    
def test_keydown():                                  # functions to test if a key is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        return "left"
    elif keys[pygame.K_RIGHT]:
        return "right"
    elif keys[pygame.K_DOWN]:
        return "down"
    elif keys[pygame.K_UP]:
        return "up"
    elif keys[pygame.K_SPACE]:
        return "space"
    elif keys[pygame.K_o]:
        return "o"
    elif keys[pygame.K_x]:
        return "x"
        
def move_sel():                           # function to move the selection rectangle
    global sx
    global sy
    global xx
    global yy
    if test_keydown() == "left" and sx != 0:
        sx -= 175      # change coordinate of selection
        xx -= 1        # change coordinate 
    elif test_keydown() == "right" and sx < 200:
        sx += 175
        xx += 1
    elif test_keydown() == "up" and sy != 0:
        sy -= 175
        yy -= 1
    elif test_keydown() == "down" and sy < 200:
        sy += 175
        yy += 1
        
def place(): 
    global playersymbol
    if playersymbol == "X":                            # function to place symbol at th selected field
        if test_keydown() == "space":
            if marked[str(xx) + str(yy)] == "not":
                marked[str(xx) + str(yy)] = "markedX"   # change the selected field on 'xx' and 'yy' in the 'marked' dictionary to marked
                playersymbol = "O"
            else:
                pass
    
    elif playersymbol == "O":                            # function to place symbol at th selected field
        if test_keydown() == "space":
            if marked[str(xx) + str(yy)] == "not":
                marked[str(xx) + str(yy)] = "markedO" 
                playersymbol = "X"
            else:
                pass
 

 
def run(): 
    global mir1
    global mir2
    global mir3
    global winsym  
    global unentschieden                         # run
    running = True
    while running:
        unentschieden = False
        winsym = False
        mir1 = 0
        mir2 = 0
        mir3 = 0
        clock.tick(10)
        draw()
        quitt()
        test_keydown()
        move_sel()
        place()
        test_reihe()
        print(str(mir1) + " " + str(mir2) + " " + str(mir3))
        if winsym != False:
            draw()
            time.sleep(0.5)
            break
        unentschieden_run()
        if unentschieden == True:
            draw()
            break
    if unentschieden == False:
        return winsym

if __name__ == "__main__":
    print("- - - - - - - - - - -")
    print("Game Tic Tac Toe")
    print("- - - - - - - - - - -")        
    run()

if unentschieden == False:    
    print("\n\n\n\n\n\n")
    print("- - - - - - - - - - - - - - - - - - - - - - - -")    
    print("Das Symbol {} hat gewonnen!".format(winsym))
    print("- - - - - - - - - - - - - - - - - - - - - - - -")

elif unentschieden == True:
    print("\n\n\n\n\n\n")
    print("- - - - - - - - - - - - - - - - - - - - - - - -")    
    print("Unentschieden!")
    print("- - - - - - - - - - - - - - - - - - - - - - - -")
    
    

