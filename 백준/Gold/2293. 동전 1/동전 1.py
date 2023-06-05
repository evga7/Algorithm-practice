import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[int(input()) for _ in range(N)]
dp=[0 for _ in range(M+1)]
dp[0]=1
a.sort()
for cur in a:
    for j in range(cur,M+1):
        dp[j]+=dp[j-cur]
print(dp[M])