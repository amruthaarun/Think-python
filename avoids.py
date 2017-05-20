def avoids(word,strn):
	count=0
	f=0
	fin=open(word)
	for line in fin:
		for word in line.split():
			for char in strn:
				index=word.find(char)
				if index==-1:
					f=1
					
				else:
					f=0
					break
			if f==1:
				count=count+1
				print word
	print count
strn=raw_input("enter forbidden letters\n")	
avoids('aru.txt',strn)
