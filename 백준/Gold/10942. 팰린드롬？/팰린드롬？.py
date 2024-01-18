import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
arr=list(map(int,input().split()))
M=int(input())
dp=[[-1 for _ in range(N+1)] for _ in range(N+1)]
def go(left,right):
    if left>=right:
        return 1
    if dp[left][right]!=-1:
        return dp[left][right]
    ret=0
    if arr[left]==arr[right]:
        ret=max(ret,go(left+1,right-1))
    dp[left][right]=ret
    return dp[left][right]
for i in range(M):
    a,b=map(int,input().split())
    print(go(a-1,b-1))