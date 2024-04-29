import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9

T=int(input())
def go(n,m):
    if n==m or m==0:
        return 1
    if dp[n][m]!=-1:
        return dp[n][m]
    ret=0
    ret+=go(n-1,m)+go(n-1,m-1)
    dp[n][m]=ret
    return dp[n][m]
while T:
    T-=1
    N,M=map(int,input().split())
    dp = [[-1 for _ in range(31)] for _ in range(31)]
    print(go(M,N))