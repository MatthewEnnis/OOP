alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*"
vowels = "aeiouAEIOU"

def alphabetcheck(word):
	for letter in word:
		if letter not in alphabet:
			return False
	return True

def inputcheck(word):
	while not alphabetcheck(word):
		word = input("Invalid input, please try again: ")
	return word

def fileread(filename):
	while True:
		try:
			with open(filename, "r") as file:
				text = file.read()
		except FileNotFoundError:
			filename = input("Invalid file, please try again: ")
		else:
			return text

def newfilename(oldfilename):
	dotspot = -(oldfilename[::-1].find(".")+1)
	return oldfilename[:dotspot] + "Gibberish" + oldfilename[dotspot:]

cont = "y"

while cont == "y":
	gib1 = input("Enter your first Gibberish syllable (add * for the vowel substitute): ")
	gib1 = inputcheck(gib1)

	gib2 = input("Enter the second Gibberish syllable (* for vowel substitute): ")
	gib2 = inputcheck(gib2)
	
	filename = input("Please enter a file you want to translate:\n--> ")

	text = fileread(filename)
	
	newtext = ""
	syllable = gib1
	previousconsonant = True

	for letter in text:
		if previousconsonant and letter in vowels:
			for character in syllable:
				if character == "*":
					newtext += letter
				else:
					newtext += character
			newtext += letter
			syllable = gib2
			previousconsonant = False
		else:
			newtext += letter
			previousconsonant = True
			if letter == " ":
				syllable = gib1
	
	outputfilename = newfilename(filename)
	with open(outputfilename, "w") as outputfile:
		outputfile.write(newtext)
	
	print("Your final text is:\n" + newtext)
	
	print("\nResults can be seen in file " + outputfilename)
	
	cont = input("Play again? (y/n) ")
	while cont not in "yn":
		cont = input("Please enter y to continue or n to quit: ")

print("\nThanks for playing!")
