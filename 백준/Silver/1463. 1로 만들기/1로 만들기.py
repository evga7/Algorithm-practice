import sys
def input():return sys.stdin.readline().rstrip()
dp=[987654321 for _ in range(10000001)]
N=int(input())
dp[1]=0
for i in range(2,N+1):
    if not i%3:
        dp[i]=min(dp[i],dp[i//3]+1)
    if not i%2:
        dp[i]=min(dp[i],dp[i//2]+1)
    dp[i]=min(dp[i],dp[i-1]+1)
print(dp[N])