
from collections import *
import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
# map(int,input().split())
INF = sys.maxsize
T=int(input())
res=0
def f(idx):
    for i in range(N):
        for j in range(M):
            if a[i][j]==idx:
                return (i,j)
    return (-1,-1)
while T:
    T-=1
    N,M=map(int,input().split())
    a=[deque(map(int,input().split())) for _ in range(N)]
    idx=1
    x, y = 0, 0
    while True:
        dx, dy = f(idx)
        if dx==-1:
            break
        #오른쪽으로 움직이기
        cnt=0
        if M-dy<=dy:
            while a[dx][0]!=idx:
                cnt+=1
                a[dx].appendleft(a[dx].pop())
        else:
            while a[dx][0]!=idx:
                cnt+=1
                a[dx].append(a[dx].popleft())
        a[dx][0]=-1
        res+=dx*20
        res+=cnt*5
        idx+=1
    print(res)
    res=0