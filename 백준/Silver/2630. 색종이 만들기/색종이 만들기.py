import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
res1,res2=0,0
def go(s,x,y):
    cur=a[x][y]
    f=1
    for i in range(x,x+s):
        for j in range(y,y+s):
            if cur!=a[i][j]:
                f=0
                break
        if not f:
            break
    if f:
        global res1,res2
        if cur==0:
            res1+=1
        else:
            res2+=1
    else:
        half=s//2
        go(half,x,y)
        go(half, x, y+half)
        go(half, x+half, y)
        go(half, x+half, y + half)
go(N,0,0)
print(res1)
print(res2)

