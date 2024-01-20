from collections import *
from functools import cmp_to_key
from typing import List

dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M

import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
while True:
    N,M=map(int,input().split())
    if not N and not M:
        break
    m=defaultdict(int)
    for i in range(N):
        a=list(map(int,input().split()))
        for cur in a:
            m[cur]+=1
    b=sorted(set(m.values()),reverse=True)
    for cur in sorted(m.keys()):
        if m[cur]==b[1]:
            print(cur,end=' ')
    print('')