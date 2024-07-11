from collections import *
#sys.setrecursionlimit(100000)
#dx = [1, -1, 0, 0]  # 아 위 오 왼
#dy = [0, 0, 1, -1]
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

import math
import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N=int(input())
a=[input() for _ in range(N)]
m=defaultdict(int)
for cur in a:
    m[cur]+=1
b=[]
for cur in m.keys():
    b.append((cur,m[cur]))
b.sort(key=lambda x : (-x[1],x[0]))
print(b[0][0])