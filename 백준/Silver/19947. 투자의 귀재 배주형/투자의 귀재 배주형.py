import bisect
import heapq
import sys
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
N,M=map(int,input().split())
res=0
def go(idx,s,cnt):
    if idx==M:
        global res
        res=max(res,s)
        return
    if cnt==3:
        go(idx+1,int(s*1.2),1)
    if cnt==5:
        go(idx+1,int(s*1.35),1)
    go(idx+1,s,cnt+1)
    go(idx + 1, int(s*1.05), 1)
go(0,N,1)
print(res)