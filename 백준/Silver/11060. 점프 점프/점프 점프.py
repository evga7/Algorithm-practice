import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
a=list(map(int,input().split()))
dp=[-1 for _ in range(N+1)]
def go(idx):
    if idx>=N-1:
        return 0
    if dp[idx]!=-1:
        return dp[idx]
    dp[idx]=987654321
    for i in range(1,a[idx]+1):
        dp[idx]=min(dp[idx],go(idx+i)+1)
    return dp[idx]
res=go(0)
if res==987654321:
    res=-1
print(res)