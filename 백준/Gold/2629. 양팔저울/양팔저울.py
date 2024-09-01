import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
a=list(map(int,input().split()))
M=int(input())
b=list(map(int,input().split()))
a.sort()
dp=[[0 for _ in range(15001)] for _ in range(N+1)]
def go(idx,s):
    if dp[idx][s]:
        return dp[idx][s]
    dp[idx][s]=1
    if idx==N:
        return 0
    go(idx+1,s+a[idx])
    go(idx + 1, abs(s-a[idx]))
    go(idx + 1, s)
    return dp[idx][s]
go(0,0)
for cur in b:
    if cur>15000:
        print("N", end=' ')
        continue
    if dp[N][cur]:
        print("Y",end=' ')
    else:
        print("N", end=' ')