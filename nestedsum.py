def nested_sum(t):
	tot=0
	for i in t:
		tot+=sum(i)
	print tot
t=[[1,0],[1,2,3],[2,3,4]]
nested_sum(t)
