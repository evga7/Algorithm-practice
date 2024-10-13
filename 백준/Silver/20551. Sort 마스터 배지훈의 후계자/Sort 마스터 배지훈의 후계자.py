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
N,M=map(int,input().split())
a=[int(input()) for _ in range(N)]
a.sort()
for i in range(M):
    num=int(input())
    idx=bisect.bisect_left(a,num)
    if idx==N or a[idx]!=num:
        idx=-1
    print(idx)