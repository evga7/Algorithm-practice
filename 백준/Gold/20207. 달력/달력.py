from collections import *
import bisect
# sys.setrecursionlimit(100000)
import sys
def input():
    return sys.stdin.readline().rstrip()
N=int(input())
res=0
right=0
left=0
a=[list(map(int,input().split())) for _ in range(N)]
m=defaultdict(int)
for cur in a:
    S,E=cur[0],cur[1]
    m[S]+=1
    m[E+1]-=1
cnt=0
mx=0
for cur in sorted(m.keys()):
    if not mx:
        SS=cur
    cnt+=m[cur]
    mx=max(mx,cnt)
    if cnt==0:
        res+=(cur-SS)*mx
        mx=0
    
print(res)
    
    