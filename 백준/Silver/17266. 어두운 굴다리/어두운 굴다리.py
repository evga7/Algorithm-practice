import bisect
import heapq
import itertools
import math
from collections import *
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N=int(input())
M=int(input())
a=list(map(int,input().split()))
res=max(N-a[M-1],a[0])
for i in range(1,M):
    res=max(res,(a[i]-a[i-1]+1)//2)
print(res)