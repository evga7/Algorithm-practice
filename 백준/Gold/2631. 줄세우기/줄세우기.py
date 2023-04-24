import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=list(int(input()) for _ in range(N))
res=0
dp=[-1 for _ in range(N+1)]
def go(idx):
    if dp[idx]!=-1:
        return dp[idx]
    ret=1
    for i in range(idx+1,N):
        if a[idx]<a[i]:
            ret=max(ret,go(i)+1)
    dp[idx]=ret
    return dp[idx]
for i in range(N):
    res=max(res,go(i))
print(N-res)