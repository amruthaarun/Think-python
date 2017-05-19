def count(w,l):
	count=0
	i=0
	while i<len(w):
		if w[i]==l:
			count=count+1
		i=i+1
	print count
w=raw_input('enter word')
l=raw_input('enter letter')
count(w,l)
