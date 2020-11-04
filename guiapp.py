import random
import tkinter as tk
import requests
from tkinter import font

HEIGHT = 675 # Sets initial HEIGHT and WIDTH
WIDTH = 800

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

charCount = None # Initializes the character count, player count, list of player names, and list of not characters not bein used to nothing
playerCount = None
nameList = []
notUsing = []
specChar = ["mii_brawler", "mii_swordfighter", "mii_gunner", "piranha_plant", "joker", "hero", "banjo_kazooie", "terry", "byleth", "min_min", "steve"] # List of characters to ask about

root = tk.Tk() # Creates the window
root.title("SmashFinder") # Sets the window name to Smash Finder
root.iconbitmap('Assets/super_mario_question_box.ico') # Sets the window icon - from https://findicons.com/search/super-smash-bros
root.resizable(False, False) # Makes the window not resizable

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH) # Creates canvas to set 
canvas.pack()

background_image = tk.PhotoImage(file='Assets/smash_background.png') # Uploads background image from https://www.ssbwiki.com/Battlefield_(SSBU)
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

root.mainloop()