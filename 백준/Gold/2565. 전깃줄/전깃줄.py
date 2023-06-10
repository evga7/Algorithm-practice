import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
dp=[-1 for _ in range(N)]
res=0
a.sort()
def go(idx):
    if idx==N:
        return 0
    if dp[idx]!=-1:
        return dp[idx]
    ret=1
    for i in range(idx+1,N):
        if a[idx][1]<a[i][1]:
            ret=max(ret,go(i)+1)
    dp[idx]=ret
    return dp[idx]
for i in range(N):
    res=max(res,go(i))
print(N-res)