import random

# A list of the characters, both with their image/character identifiers, and their full names as tuples - e.g. (name_name, Name Name)
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

# The function to generate the list given number of characters, number of players, and the characters not being used
def listGen(numberPlayers, numChars, notUsing):
	if numberPlayers == 1: # If there is only one player
		charChoose = []

		while len(charChoose) < numChars: # While the characters chosen are less than number of characters to choose
			ran = random.randint(0, len(characters) - 1) # Chooses a new character from list index

			if characters[ran][0] not in notUsing and characters[ran] not in charChoose: # If the character chosen is not being not used and the character hasn't been chosen already
				charChoose.append(characters[ran]) # Add this character to the chosen list

		return charChoose # Returns a single array of numChars characters
	else:
		charChoose = []
		charChoose.append(listGen(1, numChars, notUsing)) # Recursively get two random lists and add them to a bigger list
		charChoose.append(listGen(1, numChars, notUsing))
		return charChoose # Returns a double array of lists of numChars characters

# Prints out the lists based on the number of players, names of said player(s), and generated list(s)
def outAnswers(num, names, ansCha):
	print()
	if num == 1: # If there is only one player, ansCha is a single array of characters
		for cha in ansCha:
			print(names[0] + " chooses " + cha[1] + "!") # For all characters in array, print the name of player with the charater name
	else: # If there are two players, ansCha is double array of list of characters
		for cha in ansCha[0]: 
			print(names[0] + " chooses " + cha[1] + "!") # For all characters in list for p1, print name of p1 with each character name
		print()
		for cha2 in ansCha[1]:
			print(names[1] + " chooses " + cha2[1] + "!") # For all characters in list for p2, print name of p2 with each character name
	print()

def main():
	numPlay = -1
	while numPlay < 1 or numPlay > 2:
		numPlay = int(input("Are 1 or 2 people playing Smash? > ")) # Get the input of number of people playing smash (1 or 2)
	
	numCharChoice = 1
	while numCharChoice != 5 and numCharChoice != 3:
		numCharChoice = int(input("Would you like 3 or 5 characters? > ")) # Get input of number of characters playing with
	
	notUse = [] # List of characters
	specChar = [["mii_brawler", 'H'], ["mii_swordfighter", 'H'], ["mii_gunner", 'H'], ["piranha_plant", 'H'], ["joker", 'H'], ["hero", 'H'], ["banjo_kazooie", 'H'], ["terry", 'H'], 
	["byleth", 'H'], ["min_min", 'H'], ["steve", 'H']] # List of characters to ask about

	for askChar in specChar: # For all characters to ask about
		charName = None
		for charAc in characters:
			if askChar[0] == charAc[0]: # Finding the name of the characters
				charName = charAc[1] # If found, set name to A[1]
		while askChar[1] != 'Y' and askChar[1] != 'N':
			askChar[1] = input("Do you have " + charName + " unlocked?\n    Please use Y or N > ") # Get input for Y or N if they have the character

		if askChar[1] == 'N':
			notUse.append(askChar[0]) # If they don't add it to list to not use


	namesList = [] # List of character names

	while len(namesList) == 0:
		nameInput = input("Please enter the name of P1 > ") # Get p1 name
		if nameInput is not None:
			namesList.append(nameInput)

	if numPlay == 2:
		while len(namesList) < 2:
			nameInput = input("Please enter the name of P2 > ") # If 2 characters, get p2 name
			if nameInput is not None:
				namesList.append(nameInput)
	
	ansCha = listGen(numPlay, numCharChoice, notUse) # Generate list with recieved values
	outAnswers(numPlay, namesList, ansCha) # Print said list with recieved values

	tryAgainAns = 'H'
	while tryAgainAns != 'Y' and tryAgainAns != 'N':
		tryAgainAns = input("Do you want to try a new team(s)?\n    Please use Y or N > ") # Finding if they want another list
		if tryAgainAns == 'Y':
			ansCha = listGen(numPlay, numCharChoice, notUse) # If they want another list, get and print another list
			outAnswers(numPlay, namesList, ansCha)
			tryAgainAns = 'H'


if __name__ == "__main__":
	main()