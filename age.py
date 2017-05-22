def age():
	i=00
	c=0
	while i<99:
		j=i
		while j<99:
			r=rev(j)
			if i==r:
				c=c+1
				print j,r
			j=j+1
		i=i+1


def rev(n):
	rev=0
	r=0
	while n>0:
		r=n%10
		rev=rev*10+r
		n=n/10
	return rev

age()
