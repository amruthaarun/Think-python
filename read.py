from string import *
def read_file(f):
	starts='***'
	t=[]
	for line in open(f):
		if starts not in line:
			for word in line.split():
				w1=word.strip(whitespace)
				w=w1.strip(punctuation)
				t.append(lower(w))
	return t
				
def count(l='book.txt'):
	t=read_file(l)
	d=dict()
	for li in t:
		d[li]=1+d.get(li,0)
	return d
	#print l," Total no of words",len(d)
#lis=['book.txt','words.txt']
#for l in lis:
#	count(l.strip())
def most_frequent():
	d=count()
	i=0
	d1=list(d.keys())
	d2=list(d.values())
	#print d2
	d3=zip(d2,d1)
	d3.sort(reverse=True)
	for dd,f in  d3:
		print dd,f
		i+=1
		if i>20:
			break

#most_frequent()
def subtract():
	t1=set(read_file('book.txt'))
	t2=set(read_file('words.txt'))
	#print t1
	'''common=0
	diff=0
	for t in t1:
		if t not in t2:
			print t
		else :
			common+=1
	print "not in word list ", len(t1)-common
	print "common\t",common
	#print "typos \t",typos'''
	t=t1.difference(t2)
	print t
subtract()
