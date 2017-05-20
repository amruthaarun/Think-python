def is_abecedarian(w):
	i=0
	j=1
	while i<len(w):
		j=i
		while j<len(w)-1:
			if ord(w[j])>ord(w[j+1]):
				return False
			j=j+1
		i=i+1
	return True


w=raw_input("enter word\n")
print is_abecedarian(w)
