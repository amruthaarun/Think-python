def has_no_e(word):
	count=0.0
	ecount=0.0
	fin=open(word)
	for line in fin:
		i=0
		for word in line.split():
			v=word.find('e')
			if v>=0:
				count=count+1
			else:
				print word
				count=count+1
				ecount=ecount+1
	percentage=(ecount/count)*100
	print percentage
has_no_e('test.txt')
			
