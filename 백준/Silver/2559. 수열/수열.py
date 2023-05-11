import sys
from itertools import *
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
aa=list(accumulate(a))
res=aa[M-1]
for i in range(M,N):
    res=max(res,aa[i]-aa[i-M])
print(res)