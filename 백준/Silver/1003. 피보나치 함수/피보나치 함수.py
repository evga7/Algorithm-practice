import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
T=int(input())
dp=[0 for _ in range(42)]
dp[0]=1
for i in range(2,42):
    dp[i]=dp[i-2]+dp[i-1]
while T:
    T-=1
    N=int(input())
    print(dp[N],dp[N+1])