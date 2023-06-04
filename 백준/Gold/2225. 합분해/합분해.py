import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
dp=[[-1 for _ in range(M+1)] for _ in range(N+1)]
def go(idx,cnt):
    if cnt==M:
        if idx==N:
            return 1
        return 0
    if dp[idx][cnt]!=-1:
        return dp[idx][cnt]
    ret=0
    for i in range(N+1):
        if idx+i<=N:
            ret+=go(idx+i,cnt+1)%int(1e9)
    dp[idx][cnt]=ret%int(1e9)
    return dp[idx][cnt]

print(go(0,0))