import random, time, sys

def warte(t):
	time.sleep(t)
	
def zufaellig(w, v):
	y = random.randint(w, v)
	return y
	
def sag(s):
	print(s)
	
def sagab(s):
	for a in s:
		print(a)
	
def sagnotab(s, c=""):
	print(s, end=c)
	
def chance(w):
	if random.random() < w:
		return True
		
def ende():
	sys.exit()
	
def pause():
	w = input("")
	
def schreibe(w, x):
	w = input(x)
	
	
liste = ["1", "m", "n"]
sagab("qwer")

# ~ sag("Hallo!")
# ~ warte(2)
# ~ sag("Ich bin ein Genius")
# ~ warte(1)
# ~ x = zufaellig(1, 10)
# ~ sag(x)
# ~ pause()
# ~ if chance(.5):
	# ~ sag("End")
	# ~ ende()

# ~ sag("Ich bin ein Genius")

class Line():
	def __init__(self, i, c):
		self.inhalt = i
		self.count = c
	def __str__(self):
		return self.inhalt

x = True
lines = []
lcount = 0
strlines = []



def suchen():
	global lines
	global strlines
	z = 0
	for linie in lines:
		strlines.append(linie.inhalt)
	print("")
	print("- - - - - - -")
	r = input("Suche:")
	for search in strlines:
		z += 1
		if search == r:
			print("{} in Zeile {}".format(search, z))
	z = 0
		
	

def schreiben():
	global lines
	global lcount
	x = True
	titel = input("Titel: ")
	print("")
	while x == True:
		r = input("")
		if r == "":
			lcount += 1
			lines.append(Line(r, lcount))
			continue
		elif r == "l":
			lines.remove(lines[-1])
			print("")
			print("- - - - - - - - - - - -")
			print(titel)
			print("")
			for linie in lines:
				print(linie.inhalt)
		elif r == "@Suchen":
			suchen()
			print("")
			print("- - - - - - - - - - - -")
			print(titel)
			print("")
			for linie in lines:
				print(linie.inhalt)
		elif r == "@Speichern":
			textname = input("Wie willst du deine Datei benennen? >")
			if textname == "":
				continue
			textname += ".txt"
			text = open(textname, "w")
			text.write(titel)
			text.write("\n")
			for textlinie in lines:
				text.write("\n" + str(textlinie.inhalt))
			break
		elif r == "@stop":
			break
		else:
			lcount += 1
			lines.append(Line(r, lcount))
			
def bearbeiten():
	global lines
	global lcount
	global datei
	new = True
	x = True
	print("")
	titel = ""
	for linie in lines:
		print(linie.inhalt, end="")
	print("\n")
	while x == True:
		r = input("")
		if r == "":
			lcount += 1
			lines.append(Line(r, lcount))
			continue
		elif r == "l":
			try:
				lines.remove(lines[-1])
				print("")
				print("- - - - - - - - - - - -")
				for linie in lines:
					print(linie.inhalt, end="")
					print("")
			except IndexError:
				print("Es gibt nichts, was du loeschen kannst!")
		elif r == "@Speichern":
			textname = input("Wie willst du deine Datei benennen? >")
			if textname == "":
				textname = datei
				text = open(textname, "w")
				text.write("\n")
				for textlinie in lines:
					text.write("\n" + str(textlinie.inhalt))
				break
			else:
				textname += ".txt"
				text = open(textname, "w")
				text.write(titel)
				text.write("\n")
				for textlinie in lines:
					text.write("\n" + str(textlinie.inhalt))
				break
		elif r == "@stop":
			break
		else:
			lcount += 1
			lines.append(Line(r, lcount))
	

def oeffnen():
	global lines
	global lcount
	global datei
	datei = input("Dateiname:(ohne dateibezeichnung) >")
	datei += ".txt"
	try:
		text = open(datei, "r+")
		for line in text:
			lcount += 1
			lines.append(Line(line, lcount))
		print("=================")
		for linie in lines:
			print(linie.inhalt, end="")
		print("\n")
		print("=================")
		r = input("Willst du {} bearbeiten? >".format(datei))
		if r == "Ja":
			bearbeiten()
	except FileNotFoundError:
		print("")
		print("Die Datei {} wurde nicht gefunden!".format(datei))
		print("")
		oeffnen()
	



print("=========================================================")
print("Dies ist ein Text-Editor basierend auf python 3.")
print("=========================================================")
print("")
print("Datei oeffnen oder Neue Datei erstellen?")
print("")
print("[oeffnen]     [neu]")
f = input(">>")
if f == "neu":
	schreiben()
elif f == "oeffnen":
	oeffnen()













