import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[[0 for _ in range(26)] for _ in range(26)]
res=0
def go(x,y):
    if y==M+1:
        y=1
        x+=1
    if x==N+1:
        global res
        res+=1
        return
    if not (a[x-1][y] and a[x-1][y-1] and a[x][y-1]):
        a[x][y]=1
        go(x,y+1)
        a[x][y]=0
    go(x,y+1)
go(1,1)
print(res)