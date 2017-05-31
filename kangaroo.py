class kangaroo(object):
        def __init__(self,):
                self.pouch_content=[]
	def put_in_pouch(self,content):
		self.pouch_content.append(content)
	def __str__(self):
		t=[]
		if self.pouch_content==[]:
			return 'no content in pouch 
		for k in self.pouch_content:
			s='   '+object.__str__(k)
			t.append(s)
		return ' '.join(t)

		
kanga=kangaroo()
roo=kangaroo()
kanga.put_in_pouch('ammu')
kanga.put_in_pouch('appu')
kanga.put_in_pouch(roo)
print kanga
print ' '
print roo
