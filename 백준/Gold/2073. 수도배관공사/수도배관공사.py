import sys
def input():return sys.stdin.readline().rstrip()
D,N=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
dp=[0 for _ in range(D+1)]
dp[0]=987654321
for i in range(N):
    pos=a[i][0]
    cost=a[i][1]
    for j in range(D,pos-1,-1):
        dp[j]=max(dp[j],min(dp[j-pos],cost))
print(dp[D])