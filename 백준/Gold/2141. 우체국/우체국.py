import sys
import math
from collections import *
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
a.sort()
left=1
right=N
s=[0 for _ in range(N+1)]
res=int(1e10)
for i in range(1,N+1):
    s[i]=a[i-1][1]+s[i-1]
while left<=right:
    mid=left+right>>1
    if s[mid]>=s[N]-s[mid]:
        res=min(res,a[mid-1][0])
        right=mid-1
    else:
        left=mid+1
print(res)