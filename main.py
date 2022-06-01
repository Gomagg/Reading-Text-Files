def read_file_content(filename):
	#Answer
	with open("./story.txt", "r") as openfile:
		read_the_file = openfile.read()
	return read_the_file
	
def countwords():
	#Answer
	text = read_file_content("./story.txt")
	print(text)
	split_text = text.split()
	count = {}
	for n in split_text:
		if n in count:
			count[n] += 1
		else:
			count[n] = 1
	return count
	
print(countwords())