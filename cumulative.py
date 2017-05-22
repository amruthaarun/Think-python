def cumulative(t):
	tot=0
	res=[]
	for i in t:
		tot+=i
		res.append(tot)
	print res
t=[1,2,3,4]
cumulative(t)
