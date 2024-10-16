import bisect
import heapq
import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
a.sort()
b=deque()
for cur in a:
    b.append(cur)
S=(3,1)
E=(11,30)
res=0
f=1
while b:
    cnt=0
    l=len(b)
    temp=(0,0)
    for s1,s2,e1,e2 in b:
        if (s1,s2)<=S:
            temp=max(temp,(e1,e2))
            cnt+=1
        else:
            cnt2=0
            while cnt2<cnt:
                cnt2+=1
                b.popleft()
            break
    if temp!=(0,0):
        S = temp
    res+=1
    if S>=(11,31):
        break
    if cnt==l or res==N:
        f=0
        break
if not f:
    res=0
print(res)
