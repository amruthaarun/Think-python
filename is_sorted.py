def is_sorted(t):
	i=0
	t.sort(reverse=True)
	print t
	while i<len(t):
		j=i
		while j<len(t)-1:
			if t[j]>t[j+1]:
				return False
			j=j+1
		i=i+1
	
	return True
t=['a','k','c']
print is_sorted(t)
