def reverse(w1,w2):
	len1=len(w1)-1
	len2=len(w2)-1
	if len1==len2:
		i=0
		j=len2
		while i<j:
			if w1[i]!=w2[j]:
				return False
			i=i+1
			j=j-1
		return True
	return False
def rev_pair(t):
		i=0
		rev=[]
		while i<len(t):
			j=i+1
			while j<len(t):
				if reverse(t[i],t[j])==True:
					rev.append(t[i])
					rev.append(t[j])
				j=j+1
			i=i+1
		if rev!=[]:
			return rev
		else:
			return False
t=['arun','amru','candy','nura']
print rev_pair(t)

