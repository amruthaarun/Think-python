class Time(object):
	def time_to_int(time):
	    minutes = time.hour * 60 + time.minute
	    seconds = minutes * 60 + time.second
	    return seconds
	def print_time(t):
		print '%.2d : %.2d : %.2d'%(t.hour,t.minute,t.second)

time1 = Time()
time1.hour = 11
time1.minute = 59
time1.second = 30
time1.print_time()
print time1.time_to_int()

