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

cont = "y"

while cont == "y":
	gib1 = input("Enter your first Gibberish syllable (* for vowel substitute): ")
	gib1 = inputcheck(gib1)

	gib2 = input("Enter your second Gibberish syllable (* for vowel substitute): ")
	gib2 = inputcheck(gib2)

	word = input("Please enter a word you want to translate: ")
	word = inputcheck(word)

	newword = ""
	syllable = gib1

	for letter in word:
		if letter in vowels:
			for character in syllable:
				if character == "*":
					newword += letter
				else:
					newword += character
			newword += letter
			syllable = gib2
		else:
			newword += letter

	print("Your final word:\n" + newword)

	cont = input("Play again? (y/n) ")
	while cont not in "yn":
		cont = input("Please enter y to continue or n to quit: ")

print("Thanks for playing!")
