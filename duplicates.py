def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
d=histogram('amruth')

def has_duplicates(t):
	for d in t:
		val=t[d]
		if val>1:
			return True
	return False
print has_duplicates(d)
