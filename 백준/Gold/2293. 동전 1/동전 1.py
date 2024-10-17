import sys
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[int(input()) for _ in range(N)]
a.sort()
dp=[0 for _ in range(M+1)]
dp[0]=1
for cur in a:
    for i in range(cur,M+1):
        dp[i]+=dp[i-cur]
print(dp[M])