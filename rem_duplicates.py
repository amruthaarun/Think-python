def remove_duplicates(t):
	t.sort()
	i=0
	while i<len(t):
		c=t.count(t[i])-1
		if c>0:
			print c
			del t[i:i+c]
		i=i+1
	return t
t=[1,4,5,6,4,4,5]
print remove_duplicates(t)

