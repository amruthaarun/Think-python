def chop(t):
	del t[0]
	del t[len(t)-1]
	print t
t = ['a', 'b', 'c', 'd', 'e', 'f']
chop(t)
