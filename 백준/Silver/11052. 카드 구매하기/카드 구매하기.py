import sys
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
b=list(map(int,input().split()))
a=[]
a.append(0)
for i in range(N):
    a.append(b[i])
dp=[-1 for _ in range(N+1)]
def go(idx):
    if idx==0:
        return 0
    if dp[idx]!=-1:
        return dp[idx]
    ret=0
    for i in range(1,N+1):
        if idx-i>=0:
            ret=max(ret,go(idx-i)+a[i])
    dp[idx]=ret
    return dp[idx]
print(go(N))