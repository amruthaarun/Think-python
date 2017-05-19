import math
def estimate_pi():
	const=2*math.sqrt(2)/9801
	k=0
	sums=0.00
	term=1.00
	while term>1e-15:
		f1=fact(4*k)
		f2=fact(k)
		uterm=f1*(1103+26390*k)
		lterm=pow(f2,4)*pow(396,4*k)	
		term=uterm/lterm
		sums=sums+term
		k=k+1
	result=const*sums
	print result
	
def fact(k):
	f=1
	if k>0:
		while k>0:
			f=f*k
			k=k-1
		return f
	elif k==0:
		return 1
	else:
		return 0
estimate_pi()

