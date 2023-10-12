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
N=int(input())
m=defaultdict(int)
for i in range(N):
    s=input().split('.')
    m[s[1]]+=1
a=[]
for cur in m.keys():
    a.append((cur,m[cur]))
a.sort()
for cur in a:
    print(cur[0],cur[1])