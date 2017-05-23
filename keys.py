def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
	print d
    return d

def print_hist(h):
	d=h.keys()
	d.sort()
	for k in d:
		print k,h.get(k,0)

h=histogram('amrutha')
print_hist(h)
