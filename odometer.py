def palindrome(w):
	i=0
	j=len(w)-1
	while i<=j:
		if w[i]!=w[j]:
			return False
		i=i+1
		j=j-1
	return True

def odometer(no):
	s=str(no)
	r1=palindrome(s[2:])
	if r1==True:
		no=no+1
		s=str(no)
		r2=palindrome(s[1:])
		if r2==True:
			no=no+1			
			s=str(no)
			r3=palindrome(s[1:5])
			if r3==True:
				no=no+1
				s=str(no)
				r3=palindrome(s)
				if r3==True:
					return True
	return False
def check():
	i=100000
	while i<=999999:
		tf=odometer(i)
		if tf==True:
			print i
		i=i+1
check()
