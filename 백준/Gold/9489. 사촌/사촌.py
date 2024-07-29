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

    
while True:
    N,K=map(int,input().split())
    if not N and not K:
        break
    m=defaultdict(int)
    a=list(map(int,input().split()))
    idx=0
    for i in range(1,N):
        m[a[i]]=a[idx]
        if i+1<N and a[i]+1!=a[i+1]:
            idx+=1
    p=m[K]
    pp=m[p]
    res=0
    if pp:
        for cur in list(m.keys()):
            if cur==K:continue
            if p!=m[cur] and pp==m[m[cur]]:
                res+=1
    print(res)