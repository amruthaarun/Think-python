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
increment(time1,130)
