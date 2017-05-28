import os

def walks(dirname):
	files=[]
	for name in os.listdir(dirname):
		path=os.path.join(dirname, name)
		if os.path.isfile(path):
		    if path[-4:]==".txt":
				files.append(path)
		else:
		    files.extend(walks(path))
    #print files
	return files



def checksum(filename):
	cmd='md5sum '+filename
	fp=os.popen(cmd)
	res=fp.read()
	stat=fp.close()
	if stat is None:
		return res


def double_check(s1,s2):
	cmd='diff %s %s' % (s1,s2)
	fp=os.popen(cmd)
	res=fp.read()
	stat=fp.close()
	if stat is None:
		return res

def search(dirs):
	files=walks(dirs)
	#print files
	d={}
	for filename in files:
		res=checksum(filename)
		res,_=res.split()
		if res in d:
			d[res].append(filename)
				
		else:
			d[res]=[filename]

 	return d
def check_duplicate():
	d=search('/home/user/python')	
	print d
	for d1,d2 in d.iteritems():
		if len(d2)>1:
			print d1
			for n in d2:
				print n
			print " "
		"""if double_check(d.values()):
			print "same"
"""
check_duplicate()
