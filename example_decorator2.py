import time
def time_cost(times):
    def time_cost_f(f):
        def time_cost_f_f(length):
            count_mini_time=1000000.0
            avg_time=0
            sum_time=0
            for i in range(times):
                start=time.clock()
                a=f(length)
                end=time.clock()
                sum_time+=(end-start)
                if (end-start)<count_mini_time:
                    count_mini_time=end-start
            avg_time=float(sum_time)/times
            print "mini_time= " +str(count_mini_time)+"  avg_time=  "+str(avg_time)
            return a
        return time_cost_f_f
    return time_cost_f

@time_cost(100)
def for_loop(length):
    return [(x,y) for x in range(length) for y in range(length) if x*y>25 ]
print len(for_loop(100))