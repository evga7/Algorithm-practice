dx = [-1,0]  # 오 왼 위 아
dy = [0,-1]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import itertools
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N,M=map(int,input().split())
dp=[[-1 for _ in range(31)] for _ in range(31)]
def go(x,y):
    if not is_inside(x,y,31,31) or y>x:
        return 0
    if dp[x][y]!=-1:
        return dp[x][y]
    if x==M and y==M:
        return 1
    ret=0
    for i in range(2):
        n_x=x+dx[i]
        n_y=y+dy[i]
        ret+=go(n_x,n_y)
    dp[x][y]=ret
    return dp[x][y]
if N<M:
    N,M=M,N
print(go(N,N))