import heapq
import itertools
import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
#dx=[0,1,0,-1,-1,-1,1,1]
#dy=[1,0,-1,0,-1,1,1,-1]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
N=int(input())
a=list(map(int,input().split()))
st=set()
s=int(input())
q=deque()
q.append(s-1)
st.add(s-1)
while q:
    cur=q.popleft()
    num=a[cur]
    for nxt in [cur+a[cur],cur-a[cur]]:
        if 0<=nxt<N and not nxt in st:
            st.add(nxt)
            q.append(nxt)
print(len(st))


