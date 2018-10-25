import time

def time_cost(f):

    # where use closure can avoid model initial print.
    def time_cost_f(length):
        start=time.clock()
        a=f(length)
        end=time.clock()
        print "time cost is",end-start
        return a
    return time_cost_f

@time_cost
def for_loop(length):
    return [(x,y) for x in range(length) for y in range(length) if x*y>25 ]

for_loop(1000)