import sys
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
a=[int(input()) for _ in range(N)]
dp=[-1 for _ in range(N+1)]
a.sort()
def solve(idx):
    if idx>=N:
        return 0
    if dp[idx]!=-1:
        return dp[idx]
    ret=-987654321
    if idx+2<=N:
        ret=max(ret,solve(idx + 2) + (a[idx] * a[idx + 1]))
    ret=max(ret,solve(idx+1)+a[idx])
    dp[idx]=ret
    return dp[idx]
print(solve(0))