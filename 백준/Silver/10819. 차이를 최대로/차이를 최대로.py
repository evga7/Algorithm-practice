from itertools import *
import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
res=0
aa=permutations(a)
for cur in aa:
    s=0
    for i in range(N-1):
        s+=abs(cur[i]-cur[i+1])
    res=max(res,s)
print(res)