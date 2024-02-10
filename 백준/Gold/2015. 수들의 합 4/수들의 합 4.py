from collections import *
import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N,M=map(int,input().split())
a=list(map(int,input().split()))
b=a
for i in range(1,N):
    b[i]+=b[i-1]
m=defaultdict(int)
res=0
for cur in a:
    if cur==M:
        res+=1
for cur in b:
    if cur-M in m:
        res+=m[cur-M]
    m[cur]+=1
print(res)