import bisect
# sys.setrecursionlimit(100000)
import sys
import heapq
from collections import *
T=int(input())
a=[]
s=0
for i in range(1,1000):
    s+=i
    if s>1000:
        break
    a.append(s)
st=set()
def chk():
    for i in range(l):
        for j in range(l):
            s = a[i] + a[j]
            if s+a[bisect.bisect(a, N - s)-1]==N:
                return 1
    return 0
m=defaultdict(int)
while T:
    T-=1
    N=int(input())
    l=len(a)
    if not N in m:
        m[N]=chk()
    print(m[N])
    