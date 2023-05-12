import sys
def input():return sys.stdin.readline().rstrip()
n,m=map(int,input().split())
dp=[[-1 for _ in range(m+1)] for _ in range(n+1)]
def go(N,M):
    if M==0 or N==M:
        return 1
    if dp[N][M]!=-1:
        return dp[N][M]
    ret=0
    ret+=go(N-1,M-1)+go(N-1,M)
    dp[N][M]=ret
    return dp[N][M]
print(go(n,m))