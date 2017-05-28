import urllib  

def Zipcodes(z):
	t=test_zip(z)
	if t is True:
		u='http://www.uszip.com/zip/'+z
		conn = urllib.urlopen(u)
		
		for line in conn.fp:
	    		if 'population' in line.strip():
				print line.strip()
	conn.close()

def test_zip(z):
	if len(z)==5:
		for c in z:
			if not c.isdigit():
				return False		
			return True
	return False
z=raw_input("enter zip code\n")
Zipcodes(z)
