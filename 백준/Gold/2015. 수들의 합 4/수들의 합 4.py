from collections import *
from itertools import *
import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
res=0
m=defaultdict(int)
b=list(accumulate(a))

for cur in b:
    if cur==M:
        res+=1
    res+=m[cur-M]
    m[cur]+=1
print(res)