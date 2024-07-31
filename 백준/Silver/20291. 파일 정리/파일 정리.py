from collections import *
#sys.setrecursionlimit(100000)
dx = [1, -1, 0, 0]  # 아 위 오 왼
dy = [0, 0, 1, -1]
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

import math
import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N=int(input())
m=defaultdict(int)
for i in range(N):
    s=input()
    ss=s[s.index('.')+1:]
    m[ss]+=1
for cur in sorted(list(m.keys())):
    print(cur,m[cur])