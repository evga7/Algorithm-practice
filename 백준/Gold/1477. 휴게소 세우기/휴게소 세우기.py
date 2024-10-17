import bisect
import heapq
import itertools
import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N,M,L=map(int,input().split())
a=list(map(int,input().split()))
a.append(L)
b=[]
a.sort()
left=1
right=L
while left<=right:
    back=0
    mid=left+right>>1
    cnt=0
    for i in range(N+1):
        cal=(a[i]-back-1)
        cnt+=cal//mid
        back=a[i]
    if cnt<=M:
        right=mid-1
    else:
        left=mid+1
print(left)
