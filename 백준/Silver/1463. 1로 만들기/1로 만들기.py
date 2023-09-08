import sys
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize

def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
N=int(input())
res=0
dp=[0 for _ in range(N+1)]
dp[1]=0
for i in range(2,N+1):
    dp[i]=dp[i-1]+1
    if i%3==0 and i//3>0:
        dp[i]=min(dp[i],dp[i//3]+1)
    if i%2==0 and i//2>0:
        dp[i]=min(dp[i],dp[i//2]+1)
print(dp[N])