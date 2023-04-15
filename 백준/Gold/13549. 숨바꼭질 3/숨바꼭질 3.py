import sys
from collections import *
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
q=deque()
q.append((N,0))
res=-1
v=[0 for _ in range(100001)]
v[N]=1
while q:
    x,c=q.popleft()
    if x==M:
        res=c
        break
    for nxt in [x*2,x-1,x+1]:
        if 0<=nxt<=100000 and not v[nxt]:
            v[nxt]=1
            if nxt==x*2:
                q.append((nxt,c))
            else:
                q.append((nxt,c+1))
print(res)