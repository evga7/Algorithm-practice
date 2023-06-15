import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
N,M=map(int,input().split())
dp=[[[-1 for _ in range(M)] for _ in range(N)] for _ in range(2)]
a=[list(map(int,input().split())) for _ in range(N)]
def go(op,x,y):
    if not is_inside(x,y,N,M):
        return -987654321
    if op:
        if x==N-1 and y==M-1:
            return a[x][y]
    if dp[op][x][y]!=-1:
        return dp[op][x][y]
    ret=-987654321
    if not op:
        ret=max(ret,go(op,x-1,y)+a[x][y],go(op,x,y+1)+a[x][y],go(1,x,y)+a[x][y])
    else:
        ret = max(ret, go(op,x + 1, y)+a[x][y], go(op,x, y + 1)+a[x][y])
    dp[op][x][y]=ret
    return dp[op][x][y]
print(go(0,N-1,0))