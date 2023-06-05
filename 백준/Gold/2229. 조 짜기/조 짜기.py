import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
dp=[-1 for _ in range(N+2)]
def go(idx):
    if idx>=N:
        return 0
    if dp[idx]!=-1:
        return dp[idx]
    ret=0
    ret=max(ret,go(idx+1))
    for i in range(idx,N):
        ret=max(ret,go(i+1)+abs(a[idx]-a[i]))
    dp[idx]=ret
    return dp[idx]
print(go(0))