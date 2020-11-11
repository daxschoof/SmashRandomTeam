import random
import tkinter as tk
import sys
import requests
from tkinter import font

# Sets initial HEIGHT and WIDTH
HEIGHT = 450 
WIDTH = 600

# A list of the characters, both with their image/character identifiers, and their full names as tuples - e.g. (name_name, Name Name)
# All icons from https://www.mariowiki.com/Gallery:Super_Smash_Bros._Ultimate
characters = [("mario", "Mario"), ("donkey_kong", "Donkey Kong"), ("link", "Link"), ("samus", "Samus"), ("dark_samus", "Dark Samus"), ("yoshi", "Yoshi"), ("kirby", "Kirby"), ("fox", "Fox"), 
("pikachu", "Pikachu"), ("luigi", "Luigi"), ("ness", "Ness"), ("captain_falcon", "Captain Falcon"), ("jigglypuff", "JigglyPuff"), ("peach", "Peach"), ("daisy", "Daisy"), ("bowser", "Bowser"), 
("ice_climbers", "Ice Climbers"), ("sheik", "Sheik"), ("zelda", "Zelda"), ("dr_mario", "Dr. Mario"), ("pichu", "Pichu"), ("falco", "Falco"), ("marth", "Marth"), ("lucina", "Lucina"), 
("young_link", "Young Link"), ("ganondorf", "Ganondorf"), ("mewtwo", "Mewtwo"), ("roy", "Roy"), ("chrom", "Chrom"), ("mr_game_watch", "Mr. Game & Watch"), ("meta_knight", "Meta Knight"), 
("pit", "Pit"), ("dark_pit", "Dark Pit"), ("zero_suit_samus", "Zero Suit Samus"), ("wario", "Wario"), ("snake", "Snake"), ("ike", "Ike"), ("pokemon_trainer", "Pokemon Trainer"), 
("diddy_kong", "Diddy Kong"), ("lucas", "Lucas"), ("sonic", "Sonic"), ("king_dedede", "King Dedede"), ("olimar", "Olimar"), ("lucario", "Lucario"), ("rob", "R.O.B."), 
("toon_link", "Toon Link"), ("wolf", "Wolf"), ("villager", "Villager"), ("mega_man", "Mega Man"), ("wii_fit_trainer", "Wii Fit Trainer"), ("rosalina_luma", "Rosalina & Luma"),
("little_mac", "Little Mac"), ("greninja", "Greninja"), ("mii_brawler", "Mii Brawler"), ("mii_swordfighter", "Mii Swordfighter"), ("mii_gunner", "Mii Gunner"), ("palutena", "Palutena"), 
("pac_man", "Pac-Man"), ("robin", "Robin"), ("shulk", "Shulk"), ("bowser_jr", "Bowser Jr."), ("duck_hunt", "Duck Hunt"), ("ryu", "Ryu"), ("ken", "Ken"), ("cloud", "Cloud"), 
("corrin", "Corrin"), ("bayonetta", "Bayonetta"), ("inkling", "Inkling"), ("ridley", "Ridley"), ("simon", "Simon"), ("richter", "Richter"), ("king_k_rool", "King K. Rool"),
("isabelle", "Isabelle"), ("incineroar", "Incineroar"), ("piranha_plant", "Piranha Plant"), ("joker", "Joker"), ("hero", "Hero"), ("banjo_kazooie", "Banjo & Kazooie"), ("terry", "Terry"), 
("byleth", "Byleth"), ("min_min", "Min Min"), ("steve", "Steve")]

# Initializes the character count, player count, list of player names, and list of not characters not bein used to nothing
charCount = None 
playerCount = None
specCount = 0
nameList = []
notUsing = []
specChar = ["mii_brawler", "mii_swordfighter", "mii_gunner", "piranha_plant", "joker", "hero", "banjo_kazooie", "terry", "byleth", "min_min", "steve"] # List of characters to ask about

def listGen(numChars, notUsing):
	charChoose = []

	while len(charChoose) < numChars: # While the characters chosen are less than number of characters to choose
		ran = random.randint(0, len(characters) - 1) # Chooses a new character from list index

		if characters[ran][0] not in notUsing and characters[ran] not in charChoose: # If the character chosen is not being not used and the character hasn't been chosen already
			charChoose.append(characters[ran]) # Add this character to the chosen list

	return charChoose # Returns a single array of numChars characters
	
# Handler for player number button
def playCountHandler(butNum):
	global playerCount
	global charCount

	# If this is for the player count, it will not be enabled yet
	if playerCount is None:
		# Setting the question label to ask about # of characters
		ques_label.config(text = 'How many characters are you playing with?')

		# Setting the buttons to ask about # of characters
		button1.config(text = '3 Characters')
		button2.config(text = '5 Characters')

		# Saving number of players
		playerCount = butNum 
	
	# If this is for character count, player count will be enabled
	else:
		# If it is 1, the '3' button was pushed, if 2, '5' button
		if butNum == 1:
			charCount = 3
		else:
			charCount = 5

		for i in range(charCount):
			results1fr.append(tk.Frame(root, bg='#0000FF', bd=5))
			results2fr.append(tk.Frame(root, bg='#FF0000', bd=5))
			results1.append(tk.Label(results1fr[i], text='', justify='c', font=('Courier', 12), bg='#ffffff', bd=1))
			results2.append(tk.Label(results2fr[i], text='', justify='c', font=('Courier', 12), bg='#ffffff', bd=1))

		# Removing player buttons
		button1.place_forget() 
		button2.place_forget()

		# Sets the question text to ask about name(s) depending on # of players
		if playerCount == 1:
			ques_label.config(text = 'What is our hero\'s name?')
		else:
			ques_label.config(text = 'What are our two warrior\'s names?')

		# Placing the first name entry
		entry_frame1.place(relx=.275, rely=.65, relheight=.1, relwidth=.15, anchor='nw')
		entryName1.place(relwidth=1, relheight=1)

		# If there is 1 player, place the button on the right of entry
		if playerCount == 1:
			buttonName1.place(relx=.575, rely=.65, relheight=.1, relwidth=.15, anchor='nw')
		# If there are 2 players, place the second name entry on right of first, put button for submit below
		else:
			buttonName2.place(relx=.425, rely=.8, relheight=.1, relwidth=.15, anchor='nw')
			entry_frame2.place(relx=.575, rely=.65, relheight=.1, relwidth=.15, anchor='nw')
			entryName2.place(relwidth=1, relheight=1)


# Handler for name entry
def nameHandler(name1, name2):
	global button1
	global button2
	# If name2 is None, there is only one player
	removed = False
	if name2 is None:
		# If the name1 box is filled, add to nameList and remove 1 player widgets
		if name1 != '':
			nameList.append(name1)
			nameList.append("CPU")

			entryName1.place_forget()
			entry_frame1.place_forget()
			buttonName1.place_forget()
			
			removed = True
	# If name2 is not None, there are 2 players
	else:
		# If name1 and name2 are filled, add to nameList and remove 2 player widgets
		if name1 != '' and name2 != '':
			nameList.append(name1)
			nameList.append(name2)

			nameList.append(name1)
			entryName1.place_forget()
			entry_frame1.place_forget()
			buttonName1.place_forget()
			buttonName2.place_forget()
			entry_frame2.place_forget()
			entryName2.place_forget()

			removed = True

	if removed:
		ques_label.config(text = 'Are you using Mii Brawler?')

		# Button for 1 player
		button1 = tk.Button(canvas, text='Yes', bg='#DE5B5B', fg='#1D0F7A', command=lambda: specHandler('y')) 
		button1.place(relx=.275, rely=.65, relheight=.1, relwidth=.15, anchor='nw')
		
		# Button for 2 players
		button2 = tk.Button(canvas, text='No', bg='#DE5B5B', fg='#1D0F7A', command=lambda: specHandler('n')) 
		button2.place(relx=.575, rely=.65, relheight=.1, relwidth=.15, anchor='nw')

def specHandler(yesnoval):
	global specCount
	global button1
	global button2
	if yesnoval == 'n':
		notUsing.append(specChar[specCount])
	specCount += 1

	if specCount == len(specChar):
		button1.place_forget()
		button2.place_forget()

		ques_label.config(text = 'Are you ready to get your teams?')

		button1 = tk.Button(canvas, text='Generate', bg='#DE5B5B', fg='#1D0F7A', command=lambda: generateTeam()) 
		button1.place(relx=.425, rely=.65, relheight=.1, relwidth=.15, anchor='nw')
	else:
		charName = 'Are you using '
		for i in range(len(characters)):
			if characters[i][0] == specChar[specCount]:
				charName += characters[i][1]

		charName += '?'
		ques_label.config(text=charName)

def generateTeam():
	global button1, welcome_label, ques_label, frame_ques, frame_text
	ques_label.place_forget()
	button1.place_forget()
	welcome_label.place_forget()
	frame_ques.place_forget()
	frame_text.place_forget()

	for val in range(len(results1fr)):
		results1fr[val].place_forget()
		results1[val].place_forget()
		results2fr[val].place_forget()
		results2[val].place_forget()

	p1Frame = tk.Frame(root, bg='#0000FF', bd=5)
	p2Frame = tk.Frame(root, bg='#FF0000', bd=5)
	
	p1Text = tk.Label(p1Frame, text=nameList[0], justify='c', font=('Courier', 14), bg='#ffffff', bd=1)
	p2Text = tk.Label(p2Frame, text=nameList[1], justify='c', font=('Courier', 14), bg='#ffffff', bd=1)

	p1Frame.place(relx=.075, rely=.1, relheight = .1, relwidth=.35, anchor='nw')
	p2Frame.place(relx=.575, rely=.1, relheight = .1, relwidth=.35, anchor='nw')

	p1Text.place(relwidth=1, relheight=1, anchor='nw')
	p2Text.place(relwidth=1, relheight=1, anchor='nw')

	button1 = tk.Button(canvas, text='Generate New Teams', bg='#DE5B5B', fg='#1D0F7A', command=lambda: generateTeam()) 
	button1.place(relx=.35, rely=.75, relheight=.07, relwidth=.3, anchor='nw')
	
	button2 = tk.Button(canvas, text='Exit', bg='#DE5B5B', fg='#1D0F7A', command=lambda: sys.exit()) 
	button2.place(relx=.35, rely=.85, relheight=.07, relwidth=.3, anchor='nw')

	team1 = listGen(charCount, notUsing)
	team2 = listGen(charCount, notUsing)

	for i in range(len(results1)):
		results1fr[i].place(relx=.1, rely=.25 + .1*i, relheight=.07, relwidth=.3, anchor='nw')
		results1[i].place(relwidth=1, relheight=1, anchor='nw')
		results1[i].config(text=team1[i][1])

		results2fr[i].place(relx=.6, rely=.25 + .1*i, relheight=.07, relwidth=.3, anchor='nw')
		results2[i].place(relwidth=1, relheight=1, anchor='nw')
		results2[i].config(text=team2[i][1])


# Creates the window, sets the window name to Smash Finder, sets the window icon, and making the window not resizable
root = tk.Tk() 
root.title("SmashRandomTeam")  
root.iconbitmap('Assets/super_mario_question_box.ico') # https://findicons.com/search/super-smash-bros
root.resizable(False, False) 

# Creates canvas to set
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)  
canvas.pack()

# Uploads background image from https://www.ssbwiki.com/Battlefield_(SSBU), then sets the image/label to the background image then places it
background_image = tk.PhotoImage(file='Assets/smash_background.png') 
background_label = tk.Label(canvas, image=background_image, anchor='n') 
background_label.place(relwidth=1, relheight=1)

# Creates a frame for the welcome text
frame_text = tk.Frame(root, bg='#FF0000', bd=5) 
frame_text.place(relx=.1, rely=.1, relwidth=.8, relheight=.25)

# Defining the text to go into the welcome text
welcome_text = 'Hello! Welcome to SmashRandomTeam! We are going to get you the best random team, but first we do need some info from you.'
welcome_text = welcome_text + ' Please click on the button that applies for your teams, and we can get started!'

# Makes a label for the welcome text
welcome_label = tk.Label(frame_text, bg='#ffffff', bd=1, text=welcome_text, wraplength=460, font=('Courier', 13)) 
welcome_label.place(relwidth=1, relheight=1)

# Adds a frame for the text asking the question relating to the button
frame_ques = tk.Frame(root, bg='#FF0000', bd=5) 
frame_ques.place(relx=.2, rely=.4, relwidth=.6, relheight=.1)

# Adds question text
ques_label = tk.Label(frame_ques, bg='#ffffff', bd=1, text='How many players do you have?', wraplength=400, font=('Courier', 12)) 
ques_label.place(relwidth=1, relheight=1)

# Button for 1 player
button1 = tk.Button(canvas, text='1 Hero', bg='#DE5B5B', fg='#1D0F7A', command=lambda: playCountHandler(1)) 
button1.place(relx=.275, rely=.65, relheight=.1, relwidth=.15, anchor='nw')

# Button for 2 players
button2 = tk.Button(canvas, text='2 Warriors', bg='#DE5B5B', fg='#1D0F7A', command=lambda: playCountHandler(2)) 
button2.place(relx=.575, rely=.65, relheight=.1, relwidth=.15, anchor='nw')

# Name entry widgets for one character
entry_frame1 = tk.Frame(canvas, bg='#DE5B5B', bd=5)
entryName1 = tk.Entry(entry_frame1, bg='#FFFFFF', fg='#222225', justify='c', font=('Courier', 10)) 
buttonName1 = tk.Button(canvas, text='Enter', bg='#DE5B5B', fg='#1D0F7A', command=lambda: nameHandler(entryName1.get(), None))

#Name entry widgets for two characters
entry_frame2 = tk.Frame(canvas, bg='#DE5B5B', bd=5)
entryName2 = tk.Entry(entry_frame2, bg='#FFFFFF', fg='#222225', justify='c', font=('Courier', 10))
buttonName2 = tk.Button(canvas, text='Enter', bg='#DE5B5B', fg='#1D0F7A', command=lambda: nameHandler(entryName1.get(), entryName2.get())) 

results1 = []
results1fr = []
results2 = []
results2fr = []

root.mainloop()