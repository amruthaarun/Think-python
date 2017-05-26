def sed(pattern,replace,f1,f2):
	fin=open(f1,'r')
	fout=open(f2,'w')
	try:
		for line in fin:
			line1=line.replace(pattern,replace)
			fout.write(line1)
		print "writing completed"		
		fout.close()
		fin.close()
	except:
		print "something went wrong"


	
			
sed('amrutha','ammuuzz','word.txt','word2.txt')
