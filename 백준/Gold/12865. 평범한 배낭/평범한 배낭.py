import sys
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
dp=[[-1 for _ in range(100001)] for _ in range(101)]
def go(idx,cnt):
    if idx==N:
        return 0
    if dp[idx][cnt]!=-1:
        return dp[idx][cnt]
    ret=0
    if cnt+a[idx][0]<=M:
        ret=max(ret,go(idx+1,cnt+a[idx][0])+a[idx][1])
    ret=max(ret,go(idx+1,cnt))
    dp[idx][cnt]=ret
    return dp[idx][cnt]
print(go(0,0))