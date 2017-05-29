class rectangle(object):
    """Represents a rectangle. 

    attributes: width, height, corner.
    """
class point(object):
    """Represents a point in 2-D space."""
def main():
	box = rectangle()
	box.width = 100.0
	box.height = 200.0
	box.corner = point()
	box.corner.x = 0.0
	box.corner.y = 0.0
	move_rect(box,2,5)
	print box.corner.x,box.corner.y
def move_rect(rect,dx,dy):
	rect.corner.x+=dx
	rect.corner.y+=dy
main()
