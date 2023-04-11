from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
m=defaultdict(int)
N,M=map(int,input().split())
for i in range(N):
    a,b=input().split()
    if int(b) in m:continue
    m[int(b)]=a
a=list(m.items())
a.sort()
for i in range(M):
    b=int(input())
    left=0
    right=len(a)
    while left<=right:
        mid=left+right>>1
        if a[mid][0]>=b:
            right=mid-1
        else:
            left=mid+1
    print(a[left][1])