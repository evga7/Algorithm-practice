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
dp=[[-1 for _ in range(31)] for _ in range(31)]
def go(N,half):
    if N==0:
        return 1
    if dp[N][half]!=-1:
        return dp[N][half]
    ret=0
    ret=go(N-1,half+1)
    if half:
        ret+=go(N,half-1)
    dp[N][half]=ret
    return dp[N][half]
while True:
    N=int(input())
    if not N:
        break
    print(go(N,0))