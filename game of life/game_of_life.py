import random, time, sys


#Conways Game of Live
#Made by Hiheat
#Github Username: Hiheat
#W.I.P.
#NOTE: This game is made by a beginner.

print("")
print("- - - - - - - - - - - - - - -")
print("E: Conway's Game of Life")
print("")
print("DE: Conways Spiel des Lebens")
print("- - - - - - - - - - - - - - -")
print("")

class Live():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.deathcount = 0
		self.livecount = 0
		self.live = True
		
class Death():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.livecount = 0
		self.live = False

class Grid():
	def __init__(self, dname):
		self.live = []
		self.death = []
		self.lines = []
		with open(dname) as fil:
			y = 0
			for line in fil:
				gl = ""
				if line.strip() == "":
					continue
				else:
					x = 0
					for char in line[:-1]:
						if char == "O":
							self.live.append(Live(x, y))
							gl += "."
						elif char == "#":
							self.death.append(Death(x, y))
							gl += "."
						else:
							gl += char
						x += 1
				self.lines.append(gl)
				y += 1
				
	def test_live(self, x, y):
		for live in self.live:
			if live.x == x and live.y == y:
				return live
		return False
		
	def test_death(self, x, y):
		for death in self.death:
			if death.x == x and death.y == y:
				return death
		return False
		
	def update(self):
		for live in self.live:
			x, y = live.x, live.y
			for dx, dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
				death = self.test_death(x + dx, y + dy)
				if death:
					live.deathcount += 1
					
		for live in self.live:
			x, y = live.x, live.y
			for dx, dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
				live = self.test_live(x + dx, y + dy)
				if live:
					live.livecount += 1
					
		for death in self.death:
			x, y = death.x, death.y
			for dx, dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
				live = self.test_live(x + dx, y + dy)
				if live:
					death.livecount += 1
		
		
	def liveordead(self):
		for death in self.death:
			x, y = death.x, death.y
			if death.live == True:
				self.death.remove(death)
				self.live.append(Live(x, y)) 
		
		for live in self.live:
			x, y = live.x, live.y
			if live.live == False:
				self.live.remove(live)
				self.death.append(Death(x, y))
				
		for live in self.live:
			live.livecount = 0
			live.deathcount = 0
		
		for death in self.death:
			death.livecount = 0
				
				# ~ self.lines[y] = self.lines[y][:x]+new+self.lines[y][x+1:] 
				
	def rules(self):
		for live in self.live:
			if live.livecount < 2:
				live.live = False
			elif live.livecount == 2 or live.livecount == 3:
				pass
			elif live.livecount > 3:
				live.live = False
		for death in self.death:
			if death.livecount == 3:
				death.live = True

		
	def paintme(self):
		y = 0
		for line in self.lines:
			x = 0
			for char in line:
				if self.test_live(x, y):
					print("O", end="")
				elif self.test_death(x, y):
					print(".", end="")
				x += 1
			print()
			y += 1
			
			
def gameround():
	print("Wie lange sollen die Generationen dauern?(Empfohlen:0.3)")
	c = input(">>")
	t = float(c)
	grid = Grid("grid1.txt")
	grid.paintme()
	r = input(">")
	true = True
	while true == True:
		grid.update()
		grid.rules()
		grid.liveordead()
		grid.paintme()
		time.sleep(t)
		print("\n\n\n\n\n\n\n")
	
					
gameround()

	
