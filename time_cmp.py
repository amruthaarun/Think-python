class Time(object):
    """Represents the time of day.
       
    attributes: hour, minute, second
    """
    def __init__(self,second=0):
	
	self.second=second
	
    def __str__(self):
	time=self.int_to_time()
	return '%.2d : %.2d : %.2d'%(time.hour,time.minute,time.second)

    def __cmp__(self,other):
	return self.second-other.second

    def int_to_time(self):
	sec=self.second
	time=Time()
	time.minute,time.second=divmod(sec,60)
	time.hour,time.minute=divmod(time.minute,60)
	return time


time1 = Time(12456)

print time1
time2 = Time(14532)

print time2
c=cmp(time1,time2)
if c>0:
	print time1," is large"
elif c<0:
	print time2 ,"is large"
else:
	print "both are equal"

