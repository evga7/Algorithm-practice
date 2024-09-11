import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
a=list(int(input()) for _ in range(N))
dp=[[-1 for _ in range(N+1)] for _ in range(N+1)]
def go(left,right):
    if left>=right:
        return a[left]*N
    if dp[left][right]!=-1:
        return dp[left][right]
    ret=0
    num=N-(right-left)
    ret=max(ret,go(left+1,right)+(a[left]*num),go(left,right-1)+(a[right]*num))
    dp[left][right]=ret
    return dp[left][right]
print(go(0,N-1))