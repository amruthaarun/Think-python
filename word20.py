fin=open('word.txt')
for line in fin:
	i=0
	for word in line.split():
		l=len(word)-1
		if l>20:
			print word
		

