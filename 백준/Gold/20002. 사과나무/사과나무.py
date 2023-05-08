import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
dp=[[0 for _ in range(N+1)]for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j]=a[i-1][j-1]+dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]
res=-987654321
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,min(i,j)+1):
            s=dp[i][j]-dp[i-k][j]-dp[i][j-k]+dp[i-k][j-k]
            res=max(res,s)
print(res)