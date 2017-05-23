def reverse_lookup(d, v):
	l=[]
	for k in d:
		if d[k]==v:
			l.append(k)
	return l	


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
d=histogram('amrutha')
print reverse_lookup(d,1)

