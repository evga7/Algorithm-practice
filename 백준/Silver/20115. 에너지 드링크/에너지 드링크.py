import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N=int(input())
a=list(map(int,input().split()))
q=[]
for cur in a:
    heapq.heappush(q,-cur)
while len(q)>1:
    cur,nxt=-heapq.heappop(q),-heapq.heappop(q)
    cur+=nxt/2
    heapq.heappush(q,-cur)
print(-q[0])