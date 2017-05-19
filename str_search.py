def find(w,l,i):
	while i<len(w):
		if w[i]==l:
			return i
		i=i+1
	return -1
w='welcome to python'
l='p'
i=3
print find(w,l,i)
