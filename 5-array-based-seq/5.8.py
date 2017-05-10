"""
Experimentally evaluate the efficiency of the pop method of Python's list class when using varying indices as a parameter, as we did for insert on page 205. Report your results akin to Table 5.5
"""

import time

N = [100, 1000, 10000, 100000, 1000000]

def eval_pop(k, n):
    l = [None] * 2 * n

    start_t = time.time()
    for i in range(n):
        l.pop(k)
    end_t = time.time()
    avg_t = (end_t - start_t)/n
    print 'Avg. time: {0} when (k,n) = ({1},{2})'.format(avg_t, k, n)

for n in N:
    for k in [0, n//2 ,n]:
        eval_pop(k, n)
