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
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=0
def go(idx,H,c):
    if idx==N:
        global res
        res=max(res,c)
        return
    go(idx+1,H,c)
    if H-a[idx]>0:
        go(idx+1,H-a[idx],c+b[idx])
go(0,100,0)
print(res)