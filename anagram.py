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
				d[s1].append([word])
	for word in d.keys():
		s=list(word)
		s.sort()
		s1=''.join(s)
		val=d[s1]
		if len(val)<=1:
			del d[s1]
	return d

d=is_anagram()

def find_length(s):
    d1 = dict()
    for c in s:
        length=len(s[c])
	d1[length]=s[c]
    return d1
d1=find_length(d)
def anagram_sort(d):
	d1=d.keys()
	d1.sort(reverse=True)
	for freq in d1:
		print freq,d[freq],"\n"
anagram_sort(d1)
