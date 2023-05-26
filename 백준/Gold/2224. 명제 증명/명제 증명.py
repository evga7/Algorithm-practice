import sys
from collections import *
def input():return sys.stdin.readline().rstrip()
N=int(input())
m=defaultdict(set)
v=[]
visited=defaultdict(set)

def go(start,cur):
    for nxt in m[cur]:
        if not nxt in visited[start]:
            visited[start].add(nxt)
            go(start,nxt)
    if start!=cur:
        v.append('%s => %s'%(start,cur))
a=[]
for i in range(N):
    s=input().split()
    a.append((s[0],s[2]))
    m[s[0]].add(s[2])
a.sort()
for cur in a:
    go(cur[0],cur[0])
print(len(v))
v.sort()
for cur in v:
    print(cur)