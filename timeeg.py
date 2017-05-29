class Time(object):
    """Represents the time of day.
       
    attributes: hour, minute, second
    """
def print_time(t):
	print '%.2d : %.2d : %.2d'%(t.hour,t.minute,t.second)
def is_after(t1,t2):
	return t1>t2

time1 = Time()
time1.hour = 11
time1.minute = 59
time1.second = 30
print_time(time1)
time2 = Time()
time2.hour = 12
time2.minute = 59
time2.second = 30
print_time(time2)
print is_after(time1,time2)
print is_after(time2,time1)

#using pure function
def increment_pure(time, seconds):
    tsecond= time.second+seconds
    #print tsecond
    t=Time()
    if tsecond >= 60:
        t.second =tsecond%60
        t.minute = time.minute+tsecond/60

    if t.minute >= 60:
	t.hour =time.hour+t.minute/60
        t.minute %= 60
        
    return t

t=increment_pure(time1,130)
print_time(t)

#using modifier without loop

def increment(time, seconds):
    time.second += seconds
    #print time.second
    if time.second >= 60:
	time.minute += time.second/60
        time.second %= 60
        
    if time.minute >= 60:
	time.hour +=time.minute/60
        time.minute %= 60
increment(time1,130)
print_time(time1)
