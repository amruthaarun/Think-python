from swampy.World import World

class rectangle(object):
    """Represents a rectangle. 

    attributes: width, height, corner.
    """
class point(object):
    """Represents a point in 2-D space."""
class Circle(object):
    """circle with center points and radius. center point refers to point object"""
def main():
	box = rectangle()
	box.width = 100.0
	box.height = 200.0
	box.ll = point()
	box.ll.x = 10.0
	box.ll.y=10.0
	box.ur = point()
	box.ur.x = 200.0
	box.ur.y=200.0
	box.color='red'
	bbox=[[box.ll.x,box.ll.y],[box.ur.x,box.ur.y]]
	world=World()
	canvas=world.ca(width=500, height=500, background='white')
	draw_rectangle(canvas,box)
	draw_point(canvas,box.ll)
	circle=Circle()
	circle.center=point()
	circle.center.x=100.0
	circle.center.y=100.0
	circle.radius=10.0
	draw_circle(canvas,circle)

	world.mainloop()

def draw_rectangle(canvas,box):
	bbox=[[box.ll.x,box.ll.y],[box.ur.x,box.ur.y]]
	canvas.rectangle(bbox, outline='pink', width=5, fill=box.color)
def draw_point(canvas,box):
	c=[box.x+.5,box.y+.5]
	canvas.circle(c,.5,width=3, fill='green')
def draw_circle(c,circle):
	center=[circle.center.x,circle.center.y]
	c.circle(center,circle.radius,width=1,fill='navy',outline='blue')
main()

def flag_czech():
	world=World()
	canvas=world.ca(width=1500, height=500, background='white')
	points = [[0,00], [150, -100], [0, -200]]
	canvas.polygon(points, fill='blue4')
	points=[[0,00],[500,00],[500,-100],[150,-100],[0,00]]
	canvas.polygon(points, fill='white', outline='black')
	points=[[150,-100],[500,-100],[500,-200],[0,-200],[150,-100]]
	canvas.polygon(points, fill='red',outline='black')
	world.mainloop()
flag_czech()
