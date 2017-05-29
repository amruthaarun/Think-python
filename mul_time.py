class Time(object):
    """Represents the time of day.
       
    attributes: hour, minute, second
    """
def print_time(t):
	print '%.2d : %.2d : %.2d'%(t.hour,t.minute,t.second)

time1 = Time()
time1.hour = 11
time1.minute = 59
time1.second = 30
print_time(time1)

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
def increment(time,sec):
    time.second+=sec
    seconds=time_to_int(time)
    time=int_to_time(seconds)
    print_time(time)
def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True
def mul_time(time,num):
	
	seconds=time_to_int(time)
	t=int_to_time(seconds*num)
	if t.hour>12:
		t.hour %=12
	return t
def race_avg(finish_time,distance):
	assert valid_time(finish_time)
	d=1.0/distance
	tavg=mul_time(finish_time,d)
	return tavg
	
t=race_avg(time1,5)
print_time(t)
