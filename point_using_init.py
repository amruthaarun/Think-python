class point(object):
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def __str__(self):
		return '(%d,%d)' % (self.x,self.y)
	def __add__(self,other):
		new=point()
		if isinstance(other,point):
			new.x=self.x+other.x
			new.y=self.y+other.y
		else:
			new.x=self.x+other[0]
			new.y=self.y+other[1]
		return new
	def __radd__(self,other):
		return self.__add__(other)
p1=point(5)
p2=point(15,5)
print p2.__dict__
print getattr(p2, 'x')
t=(3,4)
print p1+t
