import math
def square_root(a):
	a=float(a)
	x=a/2
	i=0
	while i<10:
		y=(x+a/x)/2
		x=y
		i=i+1
	return y

def test_sqrt(a):
	while a<10:
		c=float(square_root(a))
		m=float(math.sqrt(a))
		ab=abs(c-m)
		print a,"\t\t",c,"\t\t",m,"\t\t",ab
		a=a+1
test_sqrt(1)
