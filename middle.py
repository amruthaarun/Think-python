def middle(t):
	res=[]
	i=1
	while i<len(t)-1:
		x=t.pop(i)
		res.append(x)
	return res
t = ['a', 'b', 'c', 'd', 'e', 'f']
print middle(t)
