import heapq
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import copy
from collections import *
import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
a,b=map(int,input().split())
st=set()
q=[]
q.append((0,"",a))
st.add(a)
m=int(1e9)
while q:
    cost,op,cur=heapq.heappop(q)
    if cur==b:
        if cost==0:
            op="0"
        print(op)
        exit(0)
    if cur==0:continue
    nxt = cur * cur
    if 0<=nxt<=m and not nxt in st:
        st.add(nxt)
        heapq.heappush(q,(cost+1,op+'*',nxt))
    nxt=cur+cur
    if 0<=nxt<=m and not nxt in st:
        st.add(nxt)
        heapq.heappush(q,(cost+1,op+'+',nxt))
    nxt = cur - cur
    if 0<=nxt<=m and not nxt in st:
        st.add(nxt)
        heapq.heappush(q,(cost+1,op+'-',nxt))

    nxt = cur // cur
    if 0<=nxt<=m and not nxt in st:
        st.add(nxt)
        heapq.heappush(q,(cost+1,op+'/',nxt))
print(-1)