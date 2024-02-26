import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
#sys.setrecursionlimit(10000)
def input():return sys.stdin.readline().rstrip()
N=int(input())
visited=[[0 for _ in range(1001)] for _ in range(1001)]
q=[]
q.append((0,1,0))
while q:
    cost,x,copy=heapq.heappop(q)
    if x==N:
        print(cost)
        exit(0)
    if x>copy and not visited[x][x]:
        visited[x][x]=1
        heapq.heappush(q,(cost+1,x,x))
    if x+copy<=1000 and not visited[x][x+copy]:
        visited[x][x+copy]=1
        heapq.heappush(q,(cost+1,x+copy,copy))
    if x-1>=0 and not visited[x-1][copy]:
        visited[x-1][copy]=1
        heapq.heappush(q,(cost+1,x-1,copy))