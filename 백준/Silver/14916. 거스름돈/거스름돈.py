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
dp=[-1 for _ in range(N+1)]
def go(idx):
    if idx<0:
        return 987654321
    if idx==0:
        return 0
    if dp[idx]!=-1:
        return dp[idx]
    ret=987654321
    ret=min(ret,go(idx-5)+1,go(idx-2)+1)
    dp[idx]=ret
    return dp[idx]
res=go(N)
if res==987654321:
    res=-1
print(res)