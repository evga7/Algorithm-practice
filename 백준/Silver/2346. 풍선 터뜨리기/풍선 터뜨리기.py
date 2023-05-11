from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
q=deque()
for i,cur in enumerate(a):
    q.append((cur,i+1))
while q:
    nxt=q.popleft()
    print(nxt[1],end=' ')
    t=nxt[0]
    if t>0:
        q.rotate(-(t-1))
    else:
        q.rotate(-t)