import sys
def input():return sys.stdin.readline().rstrip()
dp=[[0 for _ in range(301)] for _ in range(301)]
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
K=int(input())
for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j]=arr[i-1][j-1]+dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]
for i in range(K):
    x1,y1,x2,y2=map(int,input().split())
    print(dp[x2][y2]+dp[x1-1][y1-1]-dp[x1-1][y2]-dp[x2][y1-1])
