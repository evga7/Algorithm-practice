import bisect
import heapq
import itertools
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
a=list(map(int,input().split()))
res=0
def go(idx,cnt,score,before,cnt2):
    if cnt==10:
        global res
        if score>=5:
            res+=1
        return
    for i in range(1,6):
        n_score=score
        n_cnt2=cnt2
        if a[cnt]==i:
            n_score+=1
        if before==i:
            n_cnt2+=1
            if n_cnt2 == 3: continue
            go(i,cnt+1,n_score,i,n_cnt2)
        else:
            go(i,cnt+1,n_score,i,1)
go(0,0,0,0,0)
print(res)
