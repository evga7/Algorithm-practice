import heapq
from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
q=[]
for i in range(N):
    a=int(input())
    if not a:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q,a)