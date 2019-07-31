import os
import timeit

outfile = "data.csv"
start = 0
datapoints = 1000
step = 1000
for i in range(start,datapoints*step,step):
    print i
    pre = timeit.default_timer()
    os.system("python sum.py {}".format(i))
    mid = timeit.default_timer()
    os.system("python src/main.py {}".format(i))
    post = timeit.default_timer()
    with open(outfile, "a") as f:
        f.write("{}, {}, {}\n".format(i, mid - pre, post - mid))

