dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import heapq
import sys
def input():return sys.stdin.readline().rstrip()
N,M,K=map(int,input().split())
a=[list(input()) for _ in range(N)]

def go(x,y,cnt):
    if cnt==len(s):
        global res
        res+=1
        return
    for i in range(8):
        n_x=(x+dx[i]+N)%N
        n_y=(y+dy[i]+M)%M
        if a[n_x][n_y]==s[cnt]:
            go(n_x,n_y,cnt+1)

m=defaultdict(int)
for i in range(K):
    s=input()
    if not s in m:
        res = 0
        for i in range(N):
            for j in range(M):
                if a[i][j] == s[0]:
                    go(i, j, 1)
        m[s]=res
    print(m[s])