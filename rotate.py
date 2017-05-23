def rotate_word(s,n):
	l=len(s)
	i=0
	li=[]
	while i<l:
		c=ord(s[i])
		c=c+n
		li.append(chr(c))
		i=i+1
	s=''.join(li)
	print s
	return s
li=['ammu','aru','appu']
def dict_rotate(li,n):
	d=dict()
	for t in li:
		d[t]=rotate_word(t,n)
	return d

print dict_rotate(li,2)
