import time
known = {0:0, 1:1}

def fibonacci1(n):
    if n in known:
        return known[n]

    res = fibonacci1(n-1) + fibonacci1(n-2)
    known[n] = res
    return res
def fibonacci2(n):
    if n == 0:
        return 0
    elif  n == 1:
        return 1
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)

stime=time.time()
print fibonacci1(5)
etime=time.time()-stime
print "time to execute fib 1 is",etime
stime=time.time()
print fibonacci2(5)
etime=time.time()-stime
print "time to execute fib 2 is",etime
