def read(filename='words.txt'):
	words=[]
	fin=open(filename)
	for line in fin:
		for word in line.split():
			words.append(word.lower())
	words.sort()
	return words

def interlock2():
	words=read()
	for word in words:
		check=split(word,words)
		if check is True:
			print word,word[::2],word[1::2]


def interlock3():
	words=read()
	for word in words:
		check=three_split(word,words)
		if check is True:
			print word,word[::3],word[1::3],word[2::3]
		
			
def split(word,words):
	w1=word[::2]
	w2=word[1::2]
	#print w1,w2
	c1=bisec(w1,words)
	c2=bisec(w2,words)
	li=[(w1,w2)]
	if c1==True and c2==True:
		return True
	return False
	
def three_split(word,words):
	w1=word[::3]
	w2=word[1::3]
	w3=word[2::3]
	#print w1,w2
	c1=bisec(w1,words)
	c2=bisec(w2,words)
	c3=bisec(w3,words)
	if c1==True and c2==True and c3==True:
		return True
	return False			

def bisec(w,words):
	beg=0
	end=len(words)-1
	mid=(end+beg)/2
	while beg<end:
		if w<words[mid]:
			end=mid-1
			mid=(end+beg)/2
		elif w>words[mid]:
			beg=mid+1
			mid=(end+beg)/2
		elif w==words[mid]:
			#print "word found"
			return True
	return False
print "\nTWO WAY INTERLOCK\n"
interlock2()
print "\nTHREE WAY INTERLOCK\n"
interlock3()
