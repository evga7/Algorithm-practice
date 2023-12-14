import sys
from collections import *
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
m=defaultdict(set)
g=[[] for _ in range(27)]
def go(cur,nxt):
    if nxt in m[cur]:return
    m[cur].add(nxt)
    for x in g[nxt]:
        go(cur,x)
q=[list(input().split()) for _ in range(N)]
for cur in q:
    a,b=cur[0],cur[2]
    g[ord(a)-ord('a')].append(ord(b)-ord('a'))
for cur in q:
    go(ord(cur[0])-ord('a'),ord(cur[2])-ord('a'))
M=int(input())
for i in range(M):
    a,b,c=input().split()
    a=ord(a)-ord('a')
    c=ord(c)-ord('a')
    if c in m[a]:
        print('T')
    else:
        print('F')