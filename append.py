import time
def use_method(f):
	fin=open(f)
	t=[]
	starttime=time.time()
	for line in fin:
		for word in line.strip():
			t.append(word)
	etime=time.time()-starttime
	print "time by using append method",etime
use_method('word.txt')
def use_sign(f):
        fin=open(f)
        t=[]
	stime=time.time()
        for line in fin:
                for word in line.strip():
                        t=t+[word]
        etime=time.time()-stime
	print "time by using + operator",etime
use_sign('word.txt')
		
