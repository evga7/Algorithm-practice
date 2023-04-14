import sys
from collections import *
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
m=defaultdict(int)
left=0
right=0
cnt=0
res=0
while right<N:
    m[a[right]]+=1
    while m[a[right]]>M:
        m[a[left]]-=1
        left+=1
    right+=1
    res=max(res,right-left)
print(res)