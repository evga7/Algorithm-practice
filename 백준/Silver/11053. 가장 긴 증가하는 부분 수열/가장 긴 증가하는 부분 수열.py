import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N=int(input())
a=list(map(int,input().split()))
dp=[-1 for _ in range(N+1)]
def go(idx):
    if idx==N-1:
        return 1
    if dp[idx]!=-1:
        return dp[idx]
    ret=1
    for i in range(idx+1,N):
        if a[idx]<a[i]:
            ret=max(ret,go(i)+1)
    dp[idx]=ret
    return dp[idx]
res=0
for i in range(N):
    res=max(res,go(i))
print(res)