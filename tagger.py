from Wobbler import *
import math
class Tagger(Wobbler):
	"""class inherits from Wobbler
	"""
	def __init__(self):
		self.it=0
		self.other=0

	def steer(self,x=0,y=0):
		x=self.x-x
		y=self.y-y
		heading=math.atan2(x,y)
		return heading*180/math.pi

if __name__ == '__main__':
    world = make_world(Tagger)
    world.mainloop()
	
