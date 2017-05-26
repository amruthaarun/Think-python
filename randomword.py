from string import *
import random
def random_word(h):
    d=[]
    tot=0
    f=[]
    d1={}
    for word,freq in h.items():
	d1[freq]=word
    sorted(d1,reverse=True)
    #print d1

    for freq,word in d1.items():
	tot+=freq
        d.append([word])
	f.append(tot)
	n=len(f)
    r=random.choice(f)
   # print f,"\n",tot, r
    if r!=False:
    
    
        ind=bisec(r,f)
	#print "\n",r,tot,ind
	#print ind,
        return d[ind]



def process_file(filename):
    hist = dict()
    d1={}
    d=[]
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
   
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')
    
    for word in line.split():
        word = word.strip(punctuation + whitespace)
        word = word.lower()

        hist[word] = hist.get(word, 0) + 1
	

hist = process_file('book.txt')

def bisec(tar,t):
	beg=0
	end=len(t)
	mid=(end+beg)/2
	while beg<end:
		if tar<t[mid]:
			end=mid-1
			mid=(end+beg)/2
		elif tar>t[mid]:
			beg=mid+1
			mid=(end+beg)/2
		elif tar==t[mid]:
			return mid
	print "no word found"
	return False




for i in range(10):
    print random_word(hist),

