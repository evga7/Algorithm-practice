import sys
sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N,M=map(int,input().split())
a=list(map(int,input().split()))
dp=[-1 for _ in range(N+1)]
def go(idx):
    if idx==N-1:
        return 1
    if dp[idx]!=-1:
        return dp[idx]
    ret=0
    for i in range(idx+1,N):
        if ((i-idx)*(1+abs(a[idx]-a[i])))<=M:
            ret=max(go(i),ret)
    dp[idx]=ret
    return dp[idx]
res=go(0)
if res:
    print("YES")
else:
    print("NO")