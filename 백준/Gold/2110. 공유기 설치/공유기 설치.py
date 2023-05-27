import sys
import math
from collections import *
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[int(input()) for _ in range(N)]
a.sort()
left=1
right=int(1e10)
while left<=right:
    mid=left+right>>1
    cnt=1
    back=a[0]
    for i in range(1,N):
        cur=a[i]
        if cur-back<mid:continue
        back=cur
        cnt+=1
    if cnt>=M:
        left=mid+1
    else:
        right=mid-1
print(left-1)