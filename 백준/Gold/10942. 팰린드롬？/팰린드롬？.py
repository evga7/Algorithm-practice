import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)
MAX = sys.maxsize
MOD = int(1e9) + 9
dp=[[-1 for _ in range(2001)] for _ in range(2001)]
N=int(input())
a=list(map(int,input().split()))
M=int(input())
def go(left,right):
    if left>=right:
        return 1
    if dp[left][right]!=-1:
        return dp[left][right]
    ret=0
    if a[left]==a[right]:
        ret=max(ret,go(left+1,right-1))
    dp[left][right]=ret
    return dp[left][right]
for i in range(M):
    q,w=map(int,input().split())
    print(go(q-1,w-1))