import heapq
from collections import *
N,M=map(int,input().split())
a=list(map(int,input().split()))
left=1
right=N
def go(mid):
    q=[]
    for i in range(mid):
        q.append(0)
    cnt=0
    for cur in a:
        x=heapq.heappop(q)
        if x+cur<=M:
            heapq.heappush(q,(x+cur))
        else:
            return False
    if cnt+len(q)<=mid:
        return True
    return False
        
while left<=right:
    mid=left+right>>1
    if go(mid):
        right=mid-1
    else:
        left=mid+1
print(left)