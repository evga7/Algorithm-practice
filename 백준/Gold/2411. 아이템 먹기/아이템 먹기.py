def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import heapq
import sys
def input():return sys.stdin.readline().rstrip()
N,M,A,B=map(int,input().split())
a=[[0 for _ in range(101)] for _ in range(101)]
dp=[[[-1 for _ in range(101)] for _ in range(101)] for _ in range(101)]
for i in range(A):
    q,w=map(int,input().split())
    a[q-1][w-1]=1
for i in range(B):
    q,w=map(int,input().split())
    a[q-1][w-1]=2

def go(x,y,cnt):
    if x==N-1 and y==M-1:
        if cnt==A:
            return 1
        return 0
    if not is_inside(x,y,N,M) or a[x][y]==2:
        return 0
    if dp[x][y][cnt]!=-1:
        return dp[x][y][cnt]
    n_cnt=cnt
    if a[x][y]:
        n_cnt=cnt+1
    ret=0
    ret+=go(x+1,y,n_cnt)+go(x,y+1,n_cnt)
    dp[x][y][cnt]=ret
    return dp[x][y][cnt]
print(go(0,0,0))