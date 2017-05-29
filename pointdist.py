class point(object):
    """Represents a point in 2-D space."""
def distance_between_point(p1,p2):
	dist=point()
	dist.y=p2.y-p1.y
	dist.x=p2.x-p1.x
	return dist
def main():

	p1=point()
	p1.x=2
	p1.y=10
	p2=point()
	p2.x=5
	p2.y=6
	p3=distance_between_point(p1,p2)
	print "DISTANCE IS ",p3.x,p3.y
main()

