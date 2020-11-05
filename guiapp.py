import random
import tkinter as tk
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
("toon_link", "Toon Link"), ("wolf", "Wolf"), ("villager", "Villager"), ("mega_man", "Mega Man"), ("wii_fit_trainer", "Wii Fit Trainer"), ("rosalina_luma", "Rosaline & Luma"),
("little_mac", "Little Mac"), ("greninja", "Greninja"), ("mii_brawler", "Mii Brawler"), ("mii_swordfighter", "Mii Swordfighter"), ("mii_gunner", "Mii Gunner"), ("palutena", "Palutena"), 
("pac_man", "Pac-Man"), ("robin", "Robin"), ("shulk", "Shulk"), ("bowser_jr", "Bowser Jr."), ("duck_hunt", "Duck Hunt"), ("ryu", "Ryu"), ("ken", "Ken"), ("cloud", "Cloud"), 
("corrin", "Corrin"), ("bayonetta", "Bayonetta"), ("inkling", "Inkling"), ("ridley", "Ridley"), ("simon", "Simon"), ("richter", "Richter"), ("king_k_rool", "King K. Rool"),
("isabelle", "Isabelle"), ("incineroar", "Incineroar"), ("piranha_plant", "Piranha Plant"), ("joker", "Joker"), ("hero", "Hero"), ("banjo_kazooie", "Banjo & Kazooie"), ("terry", "Terry"), 
("byleth", "Byleth"), ("min_min", "Min Min"), ("steve", "Steve")]

# Initializes the character count, player count, list of player names, and list of not characters not bein used to nothing
charCount = None 
playerCount = None
nameList = []
notUsing = []
specChar = ["mii_brawler", "mii_swordfighter", "mii_gunner", "piranha_plant", "joker", "hero", "banjo_kazooie", "terry", "byleth", "min_min", "steve"] # List of characters to ask about

# Handler for player number button
def charCountHandler(butNum):
	# Saving number of players
	playerCount = butNum 
	
	# Removing player buttons
	button1.place_forget() 
	button2.place_forget()

	# Adding buttons for 3 or 5 characters and placing them where button1 and button2 were
	button3 = tk.Button(canvas, text='3 Characters', bg='#DE5B5B', fg='#1D0F7A', command=lambda: charCountHandler(1))
	button3.place(relx=.275, rely=.65, relheight=.1, relwidth=.15, anchor='nw')

	button4 = tk.Button(canvas, text='5 Characters', bg='#DE5B5B', fg='#1D0F7A', command=lambda: charCountHandler(2))
	button4.place(relx=.575, rely=.65, relheight=.1, relwidth=.15, anchor='nw')

	# Setting the question label to ask about # of characters
	ques_label.config(text = 'How many characters are you playing with?')

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
frame_text.place(relx=.15, rely=.15, relwidth=.7, relheight=.15)

# Defining the text to go into the welcome text
welcome_text = 'Hello! Welcome to SmashRandomTeam! We are going to get you the best random team, but first we do need some info from you.'
welcome_text = welcome_text + ' Please click on the button that applies for your teams, and we can get started!'

# Makes a label for the welcome text
welcome_label = tk.Label(frame_text, bg='#ffffff', bd=1, text=welcome_text, wraplength=400, font=('Courier', 8)) 
welcome_label.place(relwidth=1, relheight=1)

# Adds a frame for the text asking the question relating to the button
frame_ques = tk.Frame(root, bg='#FF0000', bd=5) 
frame_ques.place(relx=.225, rely=.4, relwidth=.55, relheight=.1)

# Adds question text
ques_label = tk.Label(frame_ques, bg='#ffffff', bd=1, text='How many players do you have?', wraplength=400, font=('Courier', 8)) 
ques_label.place(relwidth=1, relheight=1)

# Button for 1 player
button1 = tk.Button(canvas, text='1 Hero', bg='#DE5B5B', fg='#1D0F7A', command=lambda: charCountHandler(1)) 
button1.place(relx=.275, rely=.65, relheight=.1, relwidth=.15, anchor='nw')

# Button for 2 players
button2 = tk.Button(canvas, text='2 Warriors', bg='#DE5B5B', fg='#1D0F7A', command=lambda: charCountHandler(2)) 
button2.place(relx=.575, rely=.65, relheight=.1, relwidth=.15, anchor='nw')

root.mainloop()