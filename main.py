import random

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

def listGen(numberPlayers, numChars, notUsing):
	if numberPlayers == 1:
		charChoose = []

		while len(charChoose) < numChars:
			ran = random.randint(0, len(characters) - 1)

			if characters[ran][0] not in notUsing and characters[ran] not in charChoose:
				charChoose.append(characters[ran])

		return charChoose
	else:
		charChoose = []
		charChoose.append(listGen(1, numChars, notUsing))
		charChoose.append(listGen(1, numChars, notUsing))
		return charChoose

def outAnswers(num, names, ansCha):
	print()
	if num == 1:
		for cha in ansCha:
			print(names[0] + " chooses " + cha[1] + "!")
	else:
		for cha in ansCha[0]:
			print(names[0] + " chooses " + cha[1] + "!")
		print()
		for cha2 in ansCha[1]:
			print(names[1] + " chooses " + cha2[1] + "!")
	print()

def main():
	numPlay = -1
	while numPlay < 1 or numPlay > 2:
		numPlay = int(input("Are 1 or 2 people playing Smash? > "))
	
	numCharChoice = 1
	while numCharChoice != 5 and numCharChoice != 3:
		numCharChoice = int(input("Would you like 3 or 5 characters? > "))
	
	notUse = []
	specChar = [["mii_brawler", 'H'], ["mii_swordfighter", 'H'], ["mii_gunner", 'H'], ["piranha_plant", 'H'], ["joker", 'H'], ["hero", 'H'], ["banjo_kazooie", 'H'], ["terry", 'H'], 
	["byleth", 'H'], ["min_min", 'H'], ["steve", 'H']]

	for askChar in specChar:
		charName = None
		for charAc in characters:
			if askChar[0] == charAc[0]:
				charName = charAc[1]
		while askChar[1] != 'Y' and askChar[1] != 'N':
			askChar[1] = input("Do you have " + charName + " unlocked?\n    Please use Y or N > ")

		if askChar[1] == 'N':
			notUse.append(askChar[0])


	namesList = []

	while len(namesList) == 0:
		nameInput = input("Please enter the name of P1 > ")
		if nameInput is not None:
			namesList.append(nameInput)

	if numPlay == 2:
		while len(namesList) < 2:
			nameInput = input("Please enter the name of P2 > ")
			if nameInput is not None:
				namesList.append(nameInput)
	
	ansCha = listGen(numPlay, numCharChoice, notUse)
	outAnswers(numPlay, namesList, ansCha)

	tryAgainAns = 'H'
	while tryAgainAns != 'Y' and tryAgainAns != 'N':
		tryAgainAns = input("Do you want to try a new team(s)?\n    Please use Y or N > ")
		if tryAgainAns == 'Y':
			ansCha = listGen(numPlay, numCharChoice, notUse)
			outAnswers(numPlay, namesList, ansCha)
			tryAgainAns = 'H'


if __name__ == "__main__":
	main()