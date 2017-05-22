def has_duplicates(t):
	i=0
	while i<len(t):
		j=i+1
		while j<len(t):
			if t[i]==t[j]:
				return True
			j=j+1
		i=i+1
	return False
t=['a',1,'f',9,'l',1]
print has_duplicates(t)
