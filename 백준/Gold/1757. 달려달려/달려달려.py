import sys
sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
dp=[[-1 for _ in range(M+1)] for _ in range(N+1)]
a=[int(input()) for _ in range(N)]
def go(idx,cnt):
    if idx==N:
        if cnt==0:
            return 0
        return -987654321
    if dp[idx][cnt]!=-1:
        return dp[idx][cnt]
    ret=-987654321
    if cnt:
        if idx+cnt<=N:
            ret=max(ret,go(idx+cnt,0))
    else:
        ret=max(ret,go(idx+1,0))
    if cnt+1<=M:
        ret=max(ret,go(idx+1,cnt+1)+a[idx])
    dp[idx][cnt]=ret
    return dp[idx][cnt]
print(go(0,0))