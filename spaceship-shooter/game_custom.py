"""
author: Horst JENS
email: horstjens@gmail.com
contact: see http://spielend-programmieren.at/de:kontakt
license: gpl, see http://www.gnu.org/licenses/gpl-3.0.de.html
download: https://github.com/horstjens/feuerwerk/blob/master/vectortemplate2d.py
idea: clean python3/pygame template using pygame.math.vector2

"""
import pygame
import random
import os
import time


ROT = [255, 0, 0]
GRUN = [0, 255, 0]
BLAU = [0, 0, 255]
TURKIS = [0, 255, 255]
ORANGE = [255, 145, 0]
GELB = [255, 255, 0]
LILA = [255, 0, 255]
GRAU = [64, 64, 64] 

farblist = [ROT, GRUN, BLAU, TURKIS, ORANGE, GELB, LILA]

ERDE = pygame.image.load("planet_erde.png")
BIG = pygame.image.load("planet_big.png")
VENUS = pygame.image.load("planet_venus.png")
SONNE = pygame.image.load("planet_sun.png")


crosshairs = None

def cleanbyte(number):
    """makes sure the entered number is in the range of 0-255 and returns an integer in this range"""
    if number< 0:
        return 0
    elif number > 255:
        return 255
    else:
        return int(number)


def randomize_color(color, delta=50):
    d=random.randint(-delta, delta)
    color = color + d
    color = min(255,color)
    color = max(0, color)
    return color


def make_text(msg="pygame is cool", fontcolor=(255, 0, 255), fontsize=42, font=None):
    """returns pygame surface with text. You still need to blit the surface."""
    myfont = pygame.font.SysFont(font, fontsize)
    mytext = myfont.render(msg, True, fontcolor)
    mytext = mytext.convert_alpha()
    return mytext

def write(background, text, x=50, y=150, color=(0,0,0),
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

def elastic_collision(sprite1, sprite2):
        """elasitc collision between 2 VectorSprites (calculated as disc's).
           The function alters the dx and dy movement vectors of both sprites.
           The sprites need the property .mass, .radius, pos.x pos.y, move.x, move.y
           by Leonard Michlmayr"""
        if sprite1.static and sprite2.static:
            return 
        dirx = sprite1.pos.x - sprite2.pos.x
        diry = sprite1.pos.y - sprite2.pos.y
        sumofmasses = sprite1.mass + sprite2.mass
        sx = (sprite1.move.x * sprite1.mass + sprite2.move.x * sprite2.mass) / sumofmasses
        sy = (sprite1.move.y * sprite1.mass + sprite2.move.y * sprite2.mass) / sumofmasses
        bdxs = sprite2.move.x - sx
        bdys = sprite2.move.y - sy
        cbdxs = sprite1.move.x - sx
        cbdys = sprite1.move.y - sy
        distancesquare = dirx * dirx + diry * diry
        if distancesquare == 0:
            dirx = random.randint(0,11) - 5.5
            diry = random.randint(0,11) - 5.5
            distancesquare = dirx * dirx + diry * diry
        dp = (bdxs * dirx + bdys * diry) # scalar product
        dp /= distancesquare # divide by distance * distance.
        cdp = (cbdxs * dirx + cbdys * diry)
        cdp /= distancesquare
        if dp > 0:
            if not sprite2.static:
                sprite2.move.x -= 2 * dirx * dp
                sprite2.move.y -= 2 * diry * dp
            if not sprite1.static:
                sprite1.move.x -= 2 * dirx * cdp
                sprite1.move.y -= 2 * diry * cdp


class Explosion():
    """emits a lot of sparks, for Explosion or Spaceship engine"""
    def __init__(self, posvector, minangle=0, maxangle=360, maxlifetime=3,
                 minspeed=5, maxspeed=150, red=255, red_delta=0, 
                 green=225, green_delta=25, blue=0, blue_delta=0,
                 minsparks=5, maxsparks=20):
        for s in range(random.randint(minsparks,maxsparks)):
            v = pygame.math.Vector2(1,0) # vector aiming right (0°)
            a = random.randint(minangle,maxangle)
            v.rotate_ip(a)
            speed = random.randint(minspeed, maxspeed)
            duration = random.random() * maxlifetime # in seconds
            red   = randomize_color(red, red_delta)
            green = randomize_color(green, green_delta)
            blue  = randomize_color(blue, blue_delta)
            Spark(pos=pygame.math.Vector2(posvector.x, posvector.y),
                  angle= a, move=v*speed, max_age = duration, 
                  color=(red,green,blue), kill_on_edge = True)

                      
        
class Flytext(pygame.sprite.Sprite):
    def __init__(self, x, y, text="hallo", color=(255, 0, 0),
                 dx=0, dy=-50, duration=2, acceleration_factor = 1.0, delay = 0, fontsize=22):
        """a text flying upward and for a short time and disappearing"""
        self._layer = 7  # order of sprite layers (before / behind other sprites)
        pygame.sprite.Sprite.__init__(self, self.groups)  # THIS LINE IS IMPORTANT !!
        self.text = text
        self.r, self.g, self.b = color[0], color[1], color[2]
        self.dx = dx
        self.dy = dy
        self.x, self.y = x, y
        self.duration = duration  # duration of flight in seconds
        self.acc = acceleration_factor  # if < 1, Text moves slower. if > 1, text moves faster.
        self.image = make_text(self.text, (self.r, self.g, self.b), fontsize)  # font 22
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.time = 0 - delay

    def update(self, seconds):
        self.time += seconds
        if self.time < 0:
            self.rect.center = (-100,-100)
        else:
            self.y += self.dy * seconds
            self.x += self.dx * seconds
            self.dy *= self.acc  # slower and slower
            self.dx *= self.acc
            self.rect.center = (self.x, self.y)
            if self.time > self.duration:
                self.kill()      # remove Sprite from screen and from groups

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, radius = 50, color=(255,0,0), x=320, y=240,
                    startx=100,starty=100, control="mouse", ):
        """create a (black) surface and paint a blue Crosshair on it"""
        self._layer=10
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.radius = radius
        self.color = color
        self.startx=startx
        self.starty=starty
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
        self.delta = -10
        self.age = 0
        self.pos = pygame.mouse.get_pos()
        self.move = 0
        self.tail=[]
        self.create_image()
        self.rect = self.image.get_rect()
        self.control = control # "mouse" "keyboard1" "keyboard2"
        self.pushed = False

    def create_image(self):

        self.image = pygame.surface.Surface((self.radius*0.5, self.radius*0.5))
        delta1 = 12.5
        delta2 = 25
        w = self.radius*0.5 / 100.0
        h = self.radius*0.5 / 100.0
        # pointing down / up
        for y in (0,2,4):
            pygame.draw.line(self.image,(self.r-delta2,self.g,self.b),
                         (35*w,0+y),(50*w,15*h+y),2)
            pygame.draw.line(self.image,(self.r-delta2,self.g,self.b),
                         (50*w,15*h+y),(65*w,0+y),2)
    
            pygame.draw.line(self.image,(self.r-delta2,self.g,self.b),
                         (35*w,100*h-y),(50*w,85*h-y),2)
            pygame.draw.line(self.image,(self.r-delta2,self.g,self.b),
                         (50*w,85*h-y),(65*w,100*h-y),2)
        # pointing right / left                 
        for x in (0,2,4):
            pygame.draw.line(self.image,(self.r-delta2,self.g,self.b),
                         (0+x,35*h),(15*w+x,50*h),2)
            pygame.draw.line(self.image,(self.r-delta2,self.g,self.b),
                         (15*w+x,50*h),(0+x,65*h),2)
            
            pygame.draw.line(self.image,(self.r-delta2,self.g,self.b),
                         (100*w-x,35*h),(85*w-x,50*h),2)
            pygame.draw.line(self.image,(self.r-delta2,self.g,self.b),
                         (85*w-x,50*h),(100*w-x,65*h),2)
        self.image.set_colorkey((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.center = self.x, self.y

    def update(self, seconds):
        if self.control == "mouse":
            self.x, self.y = pygame.mouse.get_pos()
        elif self.control == "keyboard1":
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LSHIFT]:
                delta = 2
            else:
                delta = 9
            if pressed[pygame.K_w]:
                self.y -= delta
            if pressed[pygame.K_s]:
                self.y += delta
            if pressed[pygame.K_a]:
                self.x -= delta
            if pressed[pygame.K_d]:
                self.x += delta
        elif self.control == "keyboard2":
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_RSHIFT]:
                delta = 2
            else:
                delta = 9
            if pressed[pygame.K_UP]:
                self.y -= delta
            if pressed[pygame.K_DOWN]:
                self.y += delta
            if pressed[pygame.K_LEFT]:
                self.x -= delta
            if pressed[pygame.K_RIGHT]:
                self.x += delta
        elif self.control == "joystick1":
            pass
        elif self.control == "joystick2":
            pass
        if self.x < 0:
            self.x = 0
        elif self.x > PygView.width:
            self.x = PygView.width
        if self.y < 0:
            self.y = 0
        elif self.y > PygView.height:
            self.y = PygView.height
        self.tail.insert(0,(self.x,self.y))
        self.tail = self.tail[:128]
        self.rect.center = self.x, self.y
        self.r += self.delta   # self.r can take the values from 255 to 101
        if self.r < 151:
            self.r = 151
            self.delta = 10
        if self.r > 255:
            self.r = 255
            self.delta = -10
        self.create_image()

class VectorSprite(pygame.sprite.Sprite):
    """base class for sprites. this class inherits from pygames sprite class"""
    number = 0
    numbers = {} # { number, Sprite }

    def __init__(self, **kwargs):
        self._default_parameters(**kwargs)
        self._overwrite_parameters()
        pygame.sprite.Sprite.__init__(self, self.groups) #call parent class. NEVER FORGET !
        self.number = VectorSprite.number # unique number for each sprite
        VectorSprite.number += 1
        VectorSprite.numbers[self.number] = self
        self.create_image()
        self.distance_traveled = 0 # in pixel
        self.rect.center = (-300,-300) # avoid blinking image in topleft corner
        if self.angle != 0:
            self.set_angle(self.angle)

    def _overwrite_parameters(self):
        """change parameters before create_image is called""" 
        pass

    def _default_parameters(self, **kwargs):    
        """get unlimited named arguments and turn them into attributes
           default values for missing keywords"""

        for key, arg in kwargs.items():
            setattr(self, key, arg)
        if "layer" not in kwargs:
            self._layer = 4
        else:
            self._layer = self.layer
        if "static" not in kwargs:
            self.static = False
        if "pos" not in kwargs:
            self.pos = pygame.math.Vector2(random.randint(0, PygView.width),-50)
        if "move" not in kwargs:
            self.move = pygame.math.Vector2(0,0)
        if "radius" not in kwargs:
            self.radius = 5
        if "width" not in kwargs:
            self.width = self.radius * 2
        if "height" not in kwargs:
            self.height = self.radius * 2
        if "color" not in kwargs:
            #self.color = None
            self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        if "hitpoints" not in kwargs:
            self.hitpoints = 100
        self.hitpointsfull = self.hitpoints # makes a copy
        if "mass" not in kwargs:
            self.mass = 10
        if "damage" not in kwargs:
            self.damage = 10
        if "bounce_on_edge" not in kwargs:
            self.bounce_on_edge = False
        if "kill_on_edge" not in kwargs:
            self.kill_on_edge = False
        if "angle" not in kwargs:
            self.angle = 0 # facing right?
        if "max_age" not in kwargs:
            self.max_age = None
        if "max_distance" not in kwargs:
            self.max_distance = None
        if "picture" not in kwargs:
            self.picture = None
        if "bossnumber" not in kwargs:
            self.bossnumber = None
        if "kill_with_boss" not in kwargs:
            self.kill_with_boss = False
        if "sticky_with_boss" not in kwargs:
            self.sticky_with_boss = True
        if "mass" not in kwargs:
            self.mass = 15
        if "speed" not in kwargs:
            self.speed = None
        if "age" not in kwargs:
            self.age = 0 # age in seconds
        if "warp_on_edge" not in kwargs:
            self.warp_on_edge = False

    def kill(self):
        if self.number in self.numbers:
           del VectorSprite.numbers[self.number] # remove Sprite from numbers dict
        pygame.sprite.Sprite.kill(self)

    def create_image(self):
        if self.picture is not None:
            self.image = self.picture.copy()
        else:
            self.image = pygame.Surface((self.width,self.height))
            self.image.fill((self.color))
        self.image = self.image.convert_alpha()
        self.image0 = self.image.copy()
        self.rect= self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

    def rotate(self, by_degree):
        """rotates a sprite and changes it's angle by by_degree"""
        self.angle += by_degree
        oldcenter = self.rect.center
        self.image = pygame.transform.rotate(self.image0, self.angle)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = oldcenter

    def set_angle(self, degree):
        """rotates a sprite and changes it's angle to degree"""
        self.angle = degree
        oldcenter = self.rect.center
        self.image = pygame.transform.rotate(self.image0, self.angle)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = oldcenter

    def update(self, seconds):
        """calculate movement, position and bouncing on edge"""
        # ----- kill because... ------
        if self.hitpoints <= 0:
            self.kill()
            return
        if self.max_age is not None and self.age > self.max_age:
            self.kill()
            return
        if self.max_distance is not None and self.distance_traveled > self.max_distance:
            self.kill()
            return
            
        # ---- movement with/without boss ----
        if self.bossnumber is not None:
            if self.kill_with_boss:
                if self.bossnumber not in VectorSprite.numbers:
                    self.kill()
                    return
            if self.sticky_with_boss:
                boss = VectorSprite.numbers[self.bossnumber]
                #self.pos = v.Vec2d(boss.pos.x, boss.pos.y)
                self.pos = pygame.math.Vector2(boss.pos.x, boss.pos.y)
        self.pos += self.move * seconds
        self.distance_traveled += self.move.length() * seconds
        self.age += seconds
        self.wallbounce()
        self.rect.center = ( round(self.pos.x, 0), -round(self.pos.y, 0) )

    def wallbounce(self):
        # ---- bounce / kill on screen edge ----
        # ------- left edge ----
        if self.pos.x < 0:
            if self.kill_on_edge:
                self.kill()
            elif self.bounce_on_edge:
                self.pos.x = 0
                self.move.x *= -1
            elif self.warp_on_edge:
                self.pos.x = PygView.width 
        # -------- upper edge -----
        if self.pos.y  > 0:
            if self.kill_on_edge:
                self.kill()
            elif self.bounce_on_edge:
                self.pos.y = 0
                self.move.y *= -1
            elif self.warp_on_edge:
                self.pos.y = -PygView.height
        # -------- right edge -----                
        if self.pos.x  > PygView.width:
            if self.kill_on_edge:
                self.kill()
            elif self.bounce_on_edge:
                self.pos.x = PygView.width
                self.move.x *= -1
            elif self.warp_on_edge:
                self.pos.x = 0
        # --------- lower edge ------------
        if self.pos.y   < -PygView.height:
            if self.kill_on_edge:
                self.kill()
            elif self.bounce_on_edge:
                self.pos.y = -PygView.height
                self.move.y *= -1
            elif self.warp_on_edge:
                self.pos.y = 0


class Spark(VectorSprite):
    
    def _overwrite_parameters(self):
        self._layer = 2
        self.kill_on_edge = True
    
    def create_image(self):
        r,g,b = self.color
        r = randomize_color(r,50)
        g = randomize_color(g,50)
        b = randomize_color(b,50)
        self.image = pygame.Surface((10,10))
        pygame.draw.line(self.image, (r,g,b), 
                         (10,5), (5,5), 3)
        pygame.draw.line(self.image, (r,g,b),
                          (5,5), (2,5), 1)
        self.image.set_colorkey((0,0,0))
        self.rect= self.image.get_rect()
        self.image0 = self.image.copy()    

class Spaceship(VectorSprite):
    
    
    def _overwrite_parameters(self):
        self.friction = 0.980  #1.0 = no friction
        self.radius = 8
        self.mass = 3000
        self.supershoot = False
    
    def fire(self):
        v = pygame.math.Vector2(188,0)
        v.rotate_ip(self.angle)
        v += self.move # adding speed of spaceship to rocket
        ## create a new vector (a copy, but not the same, as the pos vector of spaceship)
        p = pygame.math.Vector2(self.pos.x, self.pos.y)
        a = self.angle
        # launch rocktet not from middle of spaceship, but from it's nose (rightmost point)
        # we know that from middle of spaceship to right edge ("nose") is 25 pixel
        t = pygame.math.Vector2(25,0)
        t.rotate_ip(self.angle)
        Rocket(pos=p+t, move=v, angle=a)
        
    def supershot(self):
        PygView.fps = 5
        self.supershoot = True
        
        
    
    def update(self, seconds):
       # print(PygView.allgroup)
        VectorSprite.update(self, seconds)
        if self.supershoot == True:
            ch = PygView.crosshairgroup[0]
            diffvector = ch.pos - self.pos
            a = pygame.math.Vector2.angle_to(diffvector)
            print("hi")
            

    def strafe_left(self):
        v = pygame.math.Vector2(50, 0)
        v.rotate_ip(self.angle + 90)   # strafe left!!
        self.move += v
        
    def strafe_right(self):
        v = pygame.math.Vector2(50, 0)
        v.rotate_ip(self.angle - 90)   # strafe right!!
        self.move += v
        
    
    def move_forward(self, speed=1):
        v = pygame.math.Vector2(speed,0)
        v.rotate_ip(self.angle)
        self.move += v
        # --- engine glow ----
        #p = pygame.math.Vector2(-30,0)
        #p.rotate_ip(self.angle)
        #Muzzle_flash(pos=pygame.math.Vector2(self.pos.x, self.pos.y) + p, max_age=0.1, angle = self.angle+180)
        
        
    def move_backward(self, speed=1):
        v = pygame.math.Vector2(speed,0)
        v.rotate_ip(self.angle)
        self.move += -v
        
    def turn_left(self, speed=3):
        self.rotate(speed)
        
    def turn_right(self, speed=3):
        self.rotate(-speed)    
    
    def create_image(self):
        self.image = pygame.Surface((50,50))
        pygame.draw.polygon(self.image, (0,0,255), ((0,0),(50,25),(0,50),(25,25)))
        self.image.set_colorkey((0,0,0))
        self.image.convert_alpha()
        self.image0 = self.image.copy()
        self.rect = self.image.get_rect()
        


class Smoke(VectorSprite):

    def create_image(self):
        self.image = pygame.Surface((50,50))
        pygame.draw.circle(self.image, self.color, (25,25),
                           int(self.age*3))
        self.image.set_colorkey((0,0,0))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

    def update(self, seconds):
        VectorSprite.update(self, seconds)
        if self.gravity is not None:
            self.move += self.gravity * seconds
        self.create_image()
        self.rect=self.image.get_rect()
        self.rect.center=(self.pos.x, self.pos.y)
        c = int(self.age * 100)
        c = min(255,c)
        self.color=(c,c,c)



class Rocket(VectorSprite):


    def _overwrite_parameters(self):
        self._layer = 1 
        self.kill_on_edge = True

    def create_image(self):
        #self.image = PygView.images["bullet"]
        self.image = pygame.Surface((10,5))
        #pygame.draw.rect(self.image, (255,255,0), (0,2, 8,3),0)
        #pygame.draw.line(self.image, (220,220,0), (0,3),(10,3),2)
        pygame.draw.polygon(self.image, (255,255,0), 
                            [(0,0), (7,0), (9,2), (9,3), (7, 4), (0,4)]
                           ) 
        #self.image.fill((255,255,0))
        self.image.set_colorkey((0,0,0))
        self.image.convert_alpha()
        self.image0 = self.image.copy()
        self.rect = self.image.get_rect()
        

class Star(VectorSprite):


    def _overwrite_parameters(self):
        self._layer = 1 
        self.kill_on_edge = True
        x = random.randint(0, PygView.width)
        y = random.randint(100, 200)
        self.pos = pygame.math.Vector2(x, -1)
        self.move = pygame.math.Vector2(0, -y)

    def create_image(self):
        bunt = False
        if random.random() < 0.3:
            bunt = True
        if bunt == True:
            f = random.choice(farblist)
            r = f[0]
            g = f[1]
            b = f[2]
        else:
            r = 255
            g = 255
            b = 255
        self.image = pygame.Surface((5,5))
        pygame.draw.circle(self.image, (r,g,b), [2,2], random.randint(1, 3)) 
        self.image.set_colorkey((0,0,0))
        self.image.convert_alpha()
        self.image0 = self.image.copy()
        self.rect = self.image.get_rect()
        
class Bubble(VectorSprite):


    def _overwrite_parameters(self):
        self._layer = 2 
        self.kill_on_edge = True
        x = random.randint(0, PygView.width)
        y = random.randint(50, 100)
        self.pos = pygame.math.Vector2(x, -1)
        self.move = pygame.math.Vector2(0, -y)
        self.r, self.g, self.b = random.choice(farblist)
        self.radius = random.randint(4, 50)

    def create_image(self):
        self.image = pygame.Surface((100, 100))
        pygame.draw.circle(self.image, (self.r,self.g,self.b), [50,50], self.radius)
        self.image.set_colorkey((0,0,0))
        self.image.convert_alpha()
        self.image0 = self.image.copy()
        self.rect = self.image.get_rect()
        
class Planet(VectorSprite):


    def _overwrite_parameters(self):
        self._layer = 1 
        self.kill_on_edge = False
        x = random.randint(0, PygView.width)
        y = random.randint(20, 40)
        self.pos = pygame.math.Vector2(x, 500)
        self.move = pygame.math.Vector2(0, -y)
        self.r, self.g, self.b = random.choice(farblist)
        self.picture = random.choice((ERDE, VENUS, BIG))
        if self.pos[1] < -1100:
            self.kill_on_edge = True
            
  #  def create_image(self):
  #      self.image = pygame.Surface((100,100))
  #      pygame.draw.circle(self.image, (255,255,255), [2,2], 50) 
  #      self.image.set_colorkey((0,0,0))
  #      self.image.convert_alpha()
  #      self.image0 = self.image.copy()
  #      self.rect = self.image.get_rect() 



class PygView(object):
    width = 0
    height = 0
    images = {}

    def __init__(self, width=640, height=400, fps=30):
        """Initialize pygame, window, background, font,...
           default arguments """
        pygame.init()
        PygView.width = width    # make global readable
        PygView.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((0,0,0)) # fill background black
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.crosshairgroup = None
        # ------ background images ------
        self.backgroundfilenames = [] # every .jpg file in folder 'data'
        try:
            for root, dirs, files in os.walk("data"):
                for file in files:
                    if file[-4:] == ".jpg" or file[-5:] == ".jpeg":
                        self.backgroundfilenames.append(file)
            random.shuffle(self.backgroundfilenames) # remix sort order
        except:
            print("no folder 'data' or no jpg files in it")
        #if len(self.backgroundfilenames) == 0:
        #    print("Error: no .jpg files found")
        #    pygame.quit
        #    sys.exit()
        PygView.bombchance = 0.015
        PygView.rocketchance = 0.001
        PygView.wave = 0
        self.age = 0
        # ------ joysticks ----
        pygame.joystick.init()
        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        for j in self.joysticks:
            j.init()
        self.prepare_sprites()
        self.loadbackground()

    def loadbackground(self):
        
        try:
            self.background = pygame.image.load(os.path.join("data",
                 self.backgroundfilenames[PygView.wave %
                 len(self.backgroundfilenames)]))
        except:
            self.background = pygame.Surface(self.screen.get_size()).convert()
            self.background.fill((0,0,0)) # fill background white
            
        self.background = pygame.transform.scale(self.background,
                          (PygView.width,PygView.height))
        self.background.convert()
        

    def prepare_sprites(self):
        """painting on the surface and create sprites"""
        # --- sprites in the allgroup will be visible each frame ---
        self.allgroup =  pygame.sprite.LayeredUpdates() # for drawing
        # --- additional groups for collision detection ----
        self.crosshairgroup = pygame.sprite.Group()
        self.rocketgroup = pygame.sprite.Group()
        self.playergroup = pygame.sprite.Group()
        self.bubblegroup = pygame.sprite.Group()
        self.planetgroup = pygame.sprite.Group()
        # ---- assign sprite groups to the Sprite classes ----
        VectorSprite.groups = self.allgroup
        Flytext.groups = self.allgroup
        Crosshair.groups = self.allgroup, self.crosshairgroup
        Rocket.groups = self.allgroup, self.rocketgroup
        Spaceship.groups = self.allgroup, self.playergroup
        Spark.groups = self.allgroup
        Star.groups = self.allgroup
        Bubble.groups = self.allgroup, self.bubblegroup
        Planet.groups = self.allgroup, self.planetgroup
        
        
        
   
        # ------ player1,2,3: mouse, keyboard, joystick ---
        self.mouse1 = Crosshair(control="mouse", color=(255,0,0))
        self.mouse2 = Crosshair(control='keyboard1', color=(255,255,0))
        self.mouse3 = Crosshair(control="keyboard2", color=(255,0,255))
        self.mouse4 = Crosshair(control="joystick1", color=(255,128,255))
        self.mouse5 = Crosshair(control="joystick2", color=(255,255,255))

        self.player1 =  Spaceship(warp_on_edge=True, pos=pygame.math.Vector2(PygView.width/2,-PygView.height/2))
        self.player2 =  Spaceship(warp_on_edge=True, pos=pygame.math.Vector2(PygView.width/2+100,-PygView.height/2))
        
        global crosshairs
        crosshairs = self.crosshairgroup
   
    def movement_indicator(self, vehicle, pygamepos, color=(0,200,0)):
        """draw circle with move direction of vehicle"""    
       # pygame.draw.circle(self.screen, color, pygamepos, 100,1)
        #glitter = (0, random.randint(128, 255), 0)
        if vehicle.move.x == 0 and vehicle.move.y == 0:
            return
        #l = min(vehicle.move.length, 100)
        #w = max(1, vehicle.move.length - 100)
        l = vehicle.move.length()
        w = int(l)
        target = pygamepos + vehicle.move
        target = (int(target[0]), int(target[1]))
       # pygame.draw.line(self.screen, color, pygamepos, target, w)
                        
        
   
    def run(self):
        """The mainloop"""
        running = True
        pygame.mouse.set_visible(False)
        oldleft, oldmiddle, oldright  = False, False, False
        self.snipertarget = None
        gameOver = False
        exittime = 0
        while running:
            milliseconds = self.clock.tick(self.fps) #
            seconds = milliseconds / 1000
            self.playtime += seconds
            if gameOver:
                if self.playtime > exittime:
                    break
            #Game over?
            #if not gameOver:
            # -------- events ------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # ------- pressed and released key ------
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        print("Quit")
                    # ---- shooting rockets for player1 ----
                    if event.key == pygame.K_TAB:
                        self.player1.fire()
                        
                    # ---- shooting rockets for player2 ----
                    if event.key == pygame.K_m:
                        self.player2.fire()
                        
                    # ---- self destroying for player 1 ----
                    if event.key == pygame.K_c:
                        Explosion(self.player1.pos)
                        self.player1.kill()
                        
                    # ---- self destroying for player 2 ----
                    if event.key == pygame.K_i:
                        Explosion(self.player2.pos)
                        self.player2.kill()
                        
                    # ---- super shot for player 1 ----
                    if event.key == pygame.K_b:
                        print("ka")
                        self.player1.supershot()
                        
                    # ---- super shot for player 2 ----
                    if event.key == pygame.K_p:
                        self.player2.supershot()
                
                    # ---- stop movement for self.player1 -----
                    #if event.key == pygame.K_r:
                    #    self.player1.move *= 0.1 # remove 90% of movement
                    
   
            # delete everything on screen
            self.screen.blit(self.background, (0, 0))
            
            Star()
            if random.random() < 0.04:
                Bubble()
            plane = False
            for plan in self.planetgroup:
                plane = True
            if random.random() < 0.09 and plane == False:
                Planet()
            
            
            # --- line from eck to mouse ---
            pygame.draw.line(self.screen, (random.randint(200,250),0,0), (self.player1.pos.x, -self.player1.pos.y), (self.mouse1.x, self.mouse1.y))

            # ------------ pressed keys ------
            pressed_keys = pygame.key.get_pressed()
            

            # --- movement for player 1 --------
            if pressed_keys[pygame.K_a]:
                self.player1.turn_left()
            if pressed_keys[pygame.K_d]:
                self.player1.turn_right()
            if pressed_keys[pygame.K_w]:
                self.player1.move_forward()
            if pressed_keys[pygame.K_s]:
                self.player1.move_backward()
                
            # --- movement for player 2 --------
            if pressed_keys[pygame.K_LEFT]:
                self.player2.turn_left()
            if pressed_keys[pygame.K_RIGHT]:
                self.player2.turn_right()
            if pressed_keys[pygame.K_UP]:
                self.player2.move_forward()
            if pressed_keys[pygame.K_DOWN]:
                self.player2.move_backward()
    
            
            # ------ mouse handler ------
            left,middle,right = pygame.mouse.get_pressed()
            #if oldleft and not left:
            #    self.launchRocket(pygame.mouse.get_pos())
            #if right:
            #    self.launchRocket(pygame.mouse.get_pos())
            oldleft, oldmiddle, oldright = left, middle, right

            # ------ joystick handler -------
            mouses = [self.mouse4, self.mouse5]
            for number, j in enumerate(self.joysticks):
                if number == 0:
                   x = j.get_axis(0)
                   y = j.get_axis(1)
                   mouses[number].x += x * 20 # *2 
                   mouses[number].y += y * 20 # *2 
                   buttons = j.get_numbuttons()
                   for b in range(buttons):
                       pushed = j.get_button( b )
                       #if b == 0 and pushed:
                       #        self.launchRocket((mouses[number].x, mouses[number].y))
                       #elif b == 1 and pushed:
                       #    if not self.mouse4.pushed: 
                       #        self.launchRocket((mouses[number].x, mouses[number].y))
                       #        mouses[number] = True
                       #elif b == 1 and not pushed:
                       #    mouses[number] = False
            pos1 = pygame.math.Vector2(pygame.mouse.get_pos())
            pos2 = self.mouse2.rect.center
            pos3 = self.mouse3.rect.center
            
            # write text below sprites
            write(self.screen, "FPS: {:8.3},  hp1: {}    hp2: {}".format(
                self.clock.get_fps(), self.player1.hitpoints, self.player2.hitpoints ), x=10, y=10, color=(255, 255, 255))
            self.allgroup.update(seconds)

            # --------- collision detection between one player (p) and many rockets (r) -----
            # iterate over all players in the playergroup
            for p in self.playergroup:
                # build a crashgroup containing all rockets that currently hit the player. 
                # do not kill them (False)
                crashgroup = pygame.sprite.spritecollide(p, self.rocketgroup,
                             False, pygame.sprite.collide_mask)
                             # also try: collide_circle, collide_rect, collide_mask
                # iterate over all rockets in the crashgroup
                for r in crashgroup:
                    # only react on rockets from another player. Ignore you own rockets
                    if r.bossnumber != p.number:
                         p.hitpoints -= r.damage  # subtract damage
                         Explosion(r.pos)
                         r.kill()
            
            # ----------- clear, draw , update, flip -----------------
            self.allgroup.draw(self.screen)

            # ----- movement indicators ---------
            self.movement_indicator(self.player1, (105,105))
            self.movement_indicator(self.player2, (1320, 105))
            
            # --- Martins verbesserter Crosshairtail -----
            for mouse in self.crosshairgroup:
                if len(mouse.tail)>2:
                    for a in range(1,len(mouse.tail)):
                        r,g,b = mouse.color
                        pygame.draw.line(self.screen,(r-a,g,b),
                                     mouse.tail[a-1],
                                     mouse.tail[a],10-a*10//10)
            
            # -------- next frame -------------
            pygame.display.flip()
        #-----------------------------------------------------
        pygame.mouse.set_visible(True)    
        pygame.quit()

if __name__ == '__main__':
    PygView(1430,800).run() # try PygView(800,600).run()
