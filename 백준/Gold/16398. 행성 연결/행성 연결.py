import bisect
import heapq
import itertools
import sys
from collections import *
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1,-1]
dy = [1, -1, 0, 0]
N=int(input())
p=[i for i in range(N+1)]
def find(x):
    if x==p[x]:
        return x
    p[x]=find(p[x])
    return p[x]
def uni(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if a<b:
            p[b]=a
        else:
            p[a]=b
        return True
    return False

b=[]
for i in range(N):
    a=list(map(int,input().split()))
    for j in range(N):
        cur=a[j]
        if not cur:continue
        b.append((cur,i,j))
b.sort()
res=0
for cur in b:
    cost,x,y=cur
    if uni(x,y):
        res+=cost
print(res)




