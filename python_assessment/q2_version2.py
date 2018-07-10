w={}
inp = open("input.txt","r")
text = inp.read()
for word in text.split(" "):
	if not word.isalnum():
		continue
	if word in w:
		w[word] += 1
	else:
		w[word] = 1
inp.close()

inp= open("output.txt","w")

for key,value in sorted(w.items()):
	print str(key) + " " + str(value)
	inp.write(str(key) + " " + str(value) + "\n")