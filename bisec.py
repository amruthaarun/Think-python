def bisec(t,tar):
	beg=0
	end=len(t)
	mid=(end-beg)/2
	while beg<end:
		if tar<t[mid]:
			end=mid-1
			mid=mid+1
		elif tar>t[mid]:
			beg=mid+1
			mid=mid+1
		elif tar==t[mid]:
			return mid
	print "no word found"
	return False

t=['ammu','aru','appu','amma','achan']
t.sort()
print t
print bisec(t,'aru')
