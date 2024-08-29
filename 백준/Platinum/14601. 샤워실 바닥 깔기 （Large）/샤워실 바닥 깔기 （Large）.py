import itertools
import math
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
N=int(input())
x,y=map(int,input().split())
c=N
N=pow(2,N)
x-=1
y=N-y
a=[[0 for _ in range(N+1)] for _ in range(N+1)]
num=0
a[y][x]=-1
def chk(x,y,l):
    for i in range(x,x+l):
        for j in range(y,y+l):
            if a[i][j]:
                return False
    return True
def go(x,y,ll):
    global num
    num+=1
    l=ll//2
    if chk(x,y,l):
        a[x+l-1][y+l-1]=num
    if chk(x,y+l,l):
        a[x+l-1][y+l]=num
    if chk(x+l,y,l):
        a[x+l][y+l-1]=num
    if chk(x+l,y+l,l):
        a[x+l][y+l]=num
    if ll==2:
        return
    go(x, y, l)
    go(x,y+l,l)
    go(x+l, y, l)
    go(x+l, y + l, l)
go(0,0,N)
for i in range(N):
    for j in range(N):
        print(a[i][j],end=' ')
    print('')
