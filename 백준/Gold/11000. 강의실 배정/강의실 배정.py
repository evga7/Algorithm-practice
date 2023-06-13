from collections import *
import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
m=defaultdict(int)
c=[]
for i in range(N):
    a,b=map(int,input().split())
    m[a]+=1
    m[b]-=1
    c.append(a)
    c.append(b)
res=0
cnt=0
for cur in sorted(set(c)):
    cnt+=m[cur]
    res=max(res,cnt)
print(res)