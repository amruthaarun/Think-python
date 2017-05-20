def consecutive(w):
	i=0
	match=0
	l=len(w)-1
	f=0
	while i<l :
		if w[i]==w[i+1]:
			match=match+1
			i=i+2
		else:
			match=0
			i=i+1
		if match==3:
			f=1
			break
	if f==1:
		return w
	else :
		return "no word"


def check():
	f=raw_input("enter the file name\n")
	fin=open(f)
	for line in fin:
		for word in line.split():
			w=consecutive(word)
			if w!='no word':
				print w
check()
