from collections import *
import bisect
import re
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
m=defaultdict(set)
N=int(input())
a=list(input() for _ in range(N))
l=len(a[0])
for cur in a:
    s=""
    for i,cur2 in enumerate(cur[::-1]):
        s+=cur2
        m[i+1].add(s)
for i in range(1,l+1):
    if len(m[i])==N:
        print(i)
        exit(0)