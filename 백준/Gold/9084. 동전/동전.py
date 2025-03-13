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
T=int(input())
while T:
    T-=1
    N=int(input())
    a=list(map(int,input().split()))
    M=int(input())
    dp=[0 for _ in range(M+1)]
    dp[0]=1
    for i in range(N):
        for j in range(a[i],M+1):
            dp[j]+=dp[j-a[i]]
    print(dp[M])



