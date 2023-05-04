from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
m=defaultdict(int)
for cur in a:
    s=cur[0]
    e=cur[1]
    m[s]+=1
    m[e]-=1
res=0
cnt=0
for cur in sorted(m):
    cnt+=m[cur]
    res=max(res,cnt)
print(res)