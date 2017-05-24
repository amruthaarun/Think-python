def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
d=histogram('amrutha arun')

def most_frequent(t):
	d1=list(t.keys())
	d2=list(t.values())
	d3=zip(d2,d1)
	d3.sort(reverse=True)
	for freq,letter in d3:
		print freq,letter
print most_frequent(d)
