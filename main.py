import random

characters = [("mario", "Mario"), ("dk", "Donkey Kong"), ("link", "Link"), ("samus", "Samus"), ("drksam", "Dark Samus"), ("yoshi", "Yoshi"), ("kirby", "Kirby"), ("fox", "Fox"), 
("pika", "Pikachu"), ("luigi", "Luigi"), ("ness", "Ness"), ("capfal", "Captain Falcon"), ("jiggly", "JigglyPuff"), ("peach", "Peach"), ("daisy", "Daisy"), ("bowser", "Bowser"), 
("ice", "Ice Climbers"), ("sheik", "Sheik"), ("zelda", "Zelda"), ("drmar", "Dr. Mario"), ("pichu", "Pichu")]

def list(numberPlayers, numChars, notUsing):
	if numberPlayers == 1:
		charChoose = []

		for i in range(0, numChars):
			ran = random.randint(0, len(characters) - 1)
			if characters[ran][0] not in notUsing:
				charChoose.append(characters[ran])
		return charChoose	


def main():
	ansCha = list(1, 3, [])
	for cha in ansCha:
		print(cha[1] + " is chosen!")

if __name__ == "__main__":
	main()