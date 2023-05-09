import sys
from itertools import *
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
aa=list(accumulate(a))
res=0
# 벌벌 통
for i in range(1,N-1):
    s1=aa[N-1]-aa[0]-a[i]
    s2=aa[N-1]-aa[i]
    res=max(res,s1+s2)
# 통 벌벌
for i in range(N-2,0,-1):
    s1=aa[N-2]-a[i]
    s2=aa[i-1]
    res=max(res,s1+s2)
#벌 통 벌
for i in range(1,N):
    s1=aa[i]-aa[0]
    s2=aa[N-2]-aa[i-1]
    res=max(res,s1+s2)
print(res)