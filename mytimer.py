import time
reps = 1000
repslist = range(reps)
def timer(func, *pargs, **kargs):
#    start = time.process_time()
    start = time.time()
    for i in repslist:
        ret = func(*pargs, **kargs)
#    elapsed = time.process_time() - start
    elapsed = time.time() - start
    return (elapsed, ret)