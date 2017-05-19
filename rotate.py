def rotate_word(s,n):
	l=len(s)
	i=0
	while i<l:
		c=ord(s[i])
		c=c+n
		print chr(c),
		
		i=i+1
rotate_word('abcd',2)

