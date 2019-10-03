import random

text = input("Type the text to be scrambled and hit enter: ")
wordlist = []
scrambledlist = []
punctuation = [',', '\'', '.', '?', '!', '-']

#find each word by using the spaces to tell where a word ends
start = 0
while text.find(" ",start) != -1:
	end = text.find(" ",start)
	wordlist.append(text[start:end])
	start = end + 1
#don't forget to add the last word
wordlist.append(text[start:])

for word in wordlist:
	#check if there's a punctuation mark at the end and account for it
	pnct = 0
	if word[-1] in punctuation:
		pnct = 1
	#make a miniword out of everything but the first and last letter
	miniword = word[1:-(1+pnct)]
	#if the miniword is long enough, swap some of the letters around
	if len(miniword) > 2:
		for i in range(len(word)):
			x = random.randrange(len(miniword))
			y = random.randrange(len(miniword))
			if x != y:
				if x < y:
					miniword = miniword[:x] + miniword[y] + miniword[x+1:y] + miniword[x] + miniword[y+1:]
				else:
					miniword = miniword[:y] + miniword[x] + miniword[y+1:x] + miniword[y] + miniword[x+1:]
	#if there are only 2 letters to swap, swap them
	elif len(miniword) == 2:
		miniword = miniword[::-1]
	#reform the full word
	scrambledword = word[0] + miniword + word[-(1+pnct):]
	#add it to the list
	scrambledlist.append(scrambledword)

#print the new sentence
for word in scrambledlist:
	print(word, end = ' ')
