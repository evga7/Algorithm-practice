from collections import *
import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
m=defaultdict(int)
res=pow(2,62)
c=0
for i in range(N):
    num=int(input())
    m[num]+=1
    cc=m[num]
    if c<=cc:
        if c==cc:
            res=min(res,num)
        else:
            res=num
        c=cc
print(res)