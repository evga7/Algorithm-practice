import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
N,M=map(int,input().split())
dp=[[[[-1 for _ in range(M+1)] for _ in range(N+1)] for _ in range(2)] for _ in range(2)]
def go(dir,op,x,y):
    if not is_inside(x,y,N,M):
        return 0
    if x==N-1 and y==M-1:
        return 1
    if dp[dir][op][x][y]!=-1:
        return dp[dir][op][x][y]
    ret=0
    if not op:
        n_dir=1-dir
        ret+=go(n_dir,1,x+dx[n_dir],y+dy[n_dir])
    ret+=go(dir,0,x+dx[dir],y+dy[dir])
    dp[dir][op][x][y]=ret
    return dp[dir][op][x][y]%100000
print((go(0,1,0,0)+go(1,1,0,0))%100000)