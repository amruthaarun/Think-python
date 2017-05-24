import random
def sort_by_length(words):
	t = []
	for word in words:
		t.append((len(word),random.random(),word))
	t.sort(reverse=True)
	#print t
	res = []
	for length, rad, word in t:			
		res.append(word)
	print res


words=('aku','appu','ammu','aru')
sort_by_length(words)
