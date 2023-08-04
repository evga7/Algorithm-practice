import sys
from collections import *
from functools import cmp_to_key
dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
T=int(input())
def go(idx):
    for i in range(N):
        for j in range(M):
            if a[i][j]==idx:
                return i,j
while T:
    T-=1
    N,M=map(int,input().split())
    a=[deque(map(int,input().split())) for _ in range(N)]
    mx=0
    for cur in a:
        mx=max(mx,max(cur))
    res=0
    idx=1
    while idx<=mx:
        n_x,n_y=go(idx)
        cnt=0
        cur_q = a[n_x]
        if n_y<M-n_y:
            while cur_q[0]!=idx:
                cur_q.append(cur_q.popleft())
                cnt+=1
        else:
            while cur_q[0]!=idx:
                cur_q.appendleft(cur_q.pop())
                cnt+=1
        p=n_x*20
        p+=cnt*5
        res+=p
        idx+=1

    print(res)