def sumall(*n):
	s=0
	for num in n:
		s+=num
	return s
n=(1,2,3,4)
print sumall(*n)
