import sys
sys.setrecursionlimit(100000)
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
for i in range(T):
    N,M=map(int,input().split())
    res=0
    for i in range(1,N):
        for j in range(i+1,N):
            if ((pow(i,2)+pow(j,2)+M)/(i*j))==((pow(i,2)+pow(j,2)+M)//(i*j)):
                res+=1
    print(res)