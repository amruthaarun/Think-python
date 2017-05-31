def is_anagram(f='words.txt'):
	fin=open(f)
	d={}
	for line in fin:
		for word in line.split():
			s=list(word)
			s.sort()
			s1=''.join(s)
			if s1 not in d:
				d[s1]=[word]
			else:
				d[s1].append(word)
	for word in d.keys():
		s=list(word)
		s.sort()
		s1=''.join(s)
		val=d[s1]
		if len(val)<=1:
			del d[s1]
	return d

d=is_anagram()

def swap_count(w1,w2):
	if len(w1)==len(w2):
		c=0
		i=0
		while i<len(w1):
			if w1[i]!=w2[i]:
				c+=1
			i+=1
		return c
	return 0

def metathesis(d):
	vals=[]
	i=0
	c=0
	for words in d.itervalues():
		for word in words:
			vals.append(word)
	"""for v in vals:
		print v"""
	while i<len(vals)-1:
		c=swap_count(vals[i],vals[i+1])
		if c==2:
			print vals[i],vals[i+1]
		i+=1
	print "exit"

		
metathesis(d)
	
