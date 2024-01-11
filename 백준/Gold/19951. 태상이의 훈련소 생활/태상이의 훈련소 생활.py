import sys
from collections import *
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
arr=list(map(int,input().split()))
m=defaultdict(int)
for i in range(M):
    a,b,c=map(int,input().split())
    m[b]-=c
    m[a-1]+=c
res=0
c=0
for i in range(N):
    c+=m[i]
    print(arr[i]+c,end=' ')