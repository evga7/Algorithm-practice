import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
dp=[-1 for _ in range(N+1)]
def go(x):
    if x==N:
        return 0
    if dp[x]!=-1:
        return dp[x]
    ret=1
    for i in range(x+1,N):
        if a[x]<a[i]:
            ret=max(ret,go(i)+1)
    dp[x]=ret
    return dp[x]
res=0
for i in range(N):
    res=max(res,go(i))
print(res)