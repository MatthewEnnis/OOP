import string

def cleanup(text):
	for i in string.punctuation:
		text = text.replace(i,"").lower()
	return text.split()

def makedict(wordlist):
	dict = {}
	with open("stopwords.txt") as stopwordsfile:
		stopwords = stopwordsfile.read().split()
	for word in wordlist:
		if word in stopwords:
			continue
		if word in dict:
			dict[word] += 1
		else:
			dict[word] = 1
	return dict

def makepage(words):
	with open("cloud.html", "w") as file:
		file.write("<!DOCTYPE html><html><head lang=\"en\"><meta charset=\"UTF-8\">\n\
					<title>Tag Cloud Generator</title></head><body>\n\
					<div style=\"text-align: center; vertical-align: middle;font-family: arial;\
					color: white; background-color: black; border: 1px solid black\">\n")
		for word,size in words.items():
			file.write("<span style=\"font-size: "+str(size*10)+"px\"> "+word+" </span>\n")
		file.write("</div></body></html>")


with open("gettysburg.txt") as file:
	makepage(makedict(cleanup(file.read())))