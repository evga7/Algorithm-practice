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
N=int(input())
a=list(int(input()) for _ in range(N))
b=[0]+list(itertools.accumulate(a))
S=b[N]
res=0
for i in range(N):
    left=i
    right=N
    while left<=right:
        mid=left+right>>1
        SS=b[mid]-b[i]
        SS2=S-SS
        if SS<SS2:
            left=mid+1
        else:
            right=mid-1
        res=max(res,min(SS,SS2))
print(res)