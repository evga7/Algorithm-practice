import heapq
from collections import *
N=int(input())
m=defaultdict(list)
res=0
for i in range(N):
    op,name,num,*a=list(input().split())
    if op=='1':
        for cur in a:
            heapq.heappush(m[name],-int(cur))
    else:
        l=int(num)
        ml=len(m[name])
        while ml and l:
            ml-=1
            l-=1
            res+=heapq.heappop(m[name])
print(-res)
    
    