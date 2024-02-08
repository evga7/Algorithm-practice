from collections import *
import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
res=0
N,D,K,C=map(int,input().split())
a=deque(int(input()) for _ in range(N))
m=defaultdict(int)
for j in range(K):
    m[a[j]]+=1
for i in range(N):
    l=len(m)
    if not C in m:
        res=max(res,l+1)
    else:
        res=max(res,l)
    m[a[K]]+=1
    m[a[0]]-=1
    if not m[a[0]]:
        m.pop(a[0])
    a.append(a.popleft())
print(res)