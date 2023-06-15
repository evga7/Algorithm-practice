import sys
def input(): return sys.stdin.readline().rstrip()
dp=[[-1 for _ in range(31)] for _ in range(31)]
def go(W,H):
    if H<0:
        return 0
    if W==0:
        return 1
    if dp[W][H]!=-1:
        return dp[W][H]
    ret=0
    ret+=go(W-1,H+1)+go(W,H-1)
    dp[W][H]=ret
    return dp[W][H]
while True:
    N=int(input())
    if not N:
        break
    print(go(N,0))