def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import copy
from collections import *
import bisect
# sys.setrecursionlimit(100000)
import sys
def input():
    return sys.stdin.readline().rstrip()
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
dp=[[[-1 for _ in range(3)] for _ in range(N+1)] for _ in range(N+1)]
def go(x,y,op):
    if not is_inside(x,y,N,N) or a[x][y]:
        return 0
    if x==N-1 and y==N-1:
        return 1
    if dp[x][y][op]!=-1:
        return dp[x][y][op]
    ret=0
    if op==0:
        if y+1<N and x+1<N and not a[x+1][y] and not a[x][y+1] and not a[x+1][y+1]:
            ret+=go(x+1,y+1,2)
        ret+=go(x,y+1,0)
    elif op==1:
        ret += go(x + 1, y, 1)
        if y + 1 < N and x + 1 < N and not a[x + 1][y] and not a[x][y + 1] and not a[x + 1][y + 1]:
            ret += go(x + 1, y + 1, 2)
    else:
        ret += go(x, y + 1, 0)
        ret += go(x + 1, y, 1)
        if y + 1 < N and x + 1 < N and not a[x + 1][y] and not a[x][y + 1] and not a[x + 1][y + 1]:
            ret += go(x + 1, y + 1, 2)
    dp[x][y][op]=ret
    return dp[x][y][op]
print(go(0,1,0))
