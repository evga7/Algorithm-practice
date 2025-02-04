import bisect
import heapq
import sys
from collections import *
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1,-1]
dy = [1, -1, 0, 0]
N=int(input())
a=list(map(int,input().split()))
s=[]
s.append(-1)
for cur in a:
    if s[-1]<cur:
        s.append(cur)
    else:
        idx=bisect.bisect_left(s,cur)
        s[idx]=cur
print(len(s)-1)
