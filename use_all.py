def use_all(word,letter):
	i=0
	f=1
	count=0
	for w in word.split():
		while i<len(letter):
			v=w.find(letter[i])
			if v==-1:
				f=0
				break
			else:
				f=1
			i=i+1
		if f==1:
			count=count+1
	if f==1	:
		print count
		return True
	else:
		return False
word=raw_input("enter word\n")
print use_all(word,'aeiou')
print use_all(word,'aeiouy')

