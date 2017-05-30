def read_dictionary(filename='c06d'):
	d = dict()
        fin = open(filename)
        for line in fin:

		# skip over the comments
		if line[0] == '#': continue

		t = line.split()
		word = t[0].lower()
		pron = ' '.join(t[1:])
		d[word] = pron

    	return d

def homophone(d):
	print d
	for key in d:
		val=d[key]
		if val>1:
			print key
		
	print "no homophone found"

def histogram(s):
    d = dict()
    for c in s:
        if s[c] not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
d1=read_dictionary()
d=histogram(d1)
homophone(d)
