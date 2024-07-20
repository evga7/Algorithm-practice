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
N,M=map(int,input().split())
dq=[deque() for _ in range(M)]
a=[list(input()) for _ in range(N)]
res=0
b=[]
for j in range(M):
    s=""
    for i in range(1,N):
        s+=a[i][j]
    b.append(s)
for i in range(N-1):
    st=set()
    c=[]
    for cur in b:
        st.add(cur)
        c.append(cur[1:])
    if len(st)!=M:
        f=1
        break
    b=c
    res+=1
print(res)