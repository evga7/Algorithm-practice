import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1,-1]
dy = [1, -1, 0, 0]
dp=[[-1 for _ in range(1001)] for _ in range(1001)]
s=input()
s2=input()
L=len(s)
L2=len(s2)
def go(idx,idx2):
    if idx==L or idx2==L2:
        return 0
    if dp[idx][idx2]!=-1:
        return dp[idx][idx2]
    ret=0
    if s[idx]==s2[idx2]:
        ret=max(ret,go(idx+1,idx2+1)+1)
    else:
        ret=max(ret,go(idx,idx2+1),go(idx+1,idx2))
    dp[idx][idx2]=ret
    return dp[idx][idx2]
print(go(0,0))