import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=[int(input()) for _ in range(N)]
dp=[-1001 for _ in range(N+1)]
a.sort()
def go(idx):
    if idx==N:
        return 0
    if dp[idx]!=-1001:
        return dp[idx]
    ret=-1001
    ret=max(ret,go(idx+1)+a[idx])
    if idx+1<N:
        ret=max(ret,go(idx+2)+(a[idx]*a[idx+1]))
    dp[idx]=ret
    return dp[idx]
print(go(0))