import bisect
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
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
dp=[-1 for _ in range(N+1)]
def go(idx):
    if idx==N:
        return 0
    if dp[idx]!=-1:
        return dp[idx]
    ret=0
    ret=max(ret,go(idx+1))
    if idx+a[idx][0]<=N:
        ret=max(ret,go(idx + a[idx][0]) + a[idx][1])
    dp[idx]=ret
    return dp[idx]
print(go(0))

