import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1,-1]
dy = [1, -1, 0, 0]
a=[int(input()) for _ in range(9)]
s=sum(a)
def go(x,y):
    for i in range(9):
        if i==x or i==y:continue
        print(a[i])
    exit(0)
    
for i in range(9):
    for j in range(i+1,9):
        if (s-(a[i]+a[j]))==100:
            go(i,j)