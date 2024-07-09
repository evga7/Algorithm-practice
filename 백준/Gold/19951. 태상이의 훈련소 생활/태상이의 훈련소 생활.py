from collections import *
#sys.setrecursionlimit(100000)
#dx = [1, -1, 0, 0]  # 아 위 오 왼
#dy = [0, 0, 1, -1]
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

import math
import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N,M=map(int,input().split())
a=list(map(int,input().split()))
m=defaultdict(int)
for i in range(M):
    q,w,e=map(int,input().split())
    m[q-1]+=e
    m[w]-=e
s=0
for i in range(N):
    if i in m:
        s+=m[i]
    print(a[i]+s,end=' ')