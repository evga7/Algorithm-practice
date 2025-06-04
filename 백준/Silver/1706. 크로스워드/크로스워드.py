import bisect
import heapq
import itertools
import sys
from collections import *
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1,-1]
dy = [1, -1, 0, 0]
N,M=map(int,input().split())
a=[list(input()) for _ in range(N)]
v=[]
for i in range(N):
    cnt=0
    s=""
    for j in range(M):
        if a[i][j]!='#':
            s+=a[i][j]
            cnt+=1
        else:
            if cnt>1:
                v.append(s)
            s=""
            cnt=0
    if cnt>1:
        v.append(s)
for i in range(M):
    cnt=0
    s=""
    for j in range(N):
        if a[j][i]!='#':
            s+=a[j][i]
            cnt+=1
        else:
            if cnt>1:
                v.append(s)
            s=""
            cnt=0
    if cnt>1:
        v.append(s)
v.sort()
print(v[0])