import sys
sys.setrecursionlimit(10000)
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N=int(input())
a=list(map(int,input().split()))
dp=[-1 for _ in range(N+1)]
def go(cur):
    if cur==N-1:
        return 0
    if dp[cur]!=-1:
        return dp[cur]
    ret=987654321
    for i in range(cur+1,N):
        n_cost=(i-cur)*(1+abs(a[i]-a[cur]))
        ret=min(ret,max(n_cost,go(i)))
    dp[cur]=ret
    return dp[cur]
print(go(0))