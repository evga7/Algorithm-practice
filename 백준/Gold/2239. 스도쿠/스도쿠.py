import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
a=[list(map(int,input())) for _ in range(9)]
v=[]
f=0
X=[[0 for _ in range(10)] for _ in range(10)]
Y=[[0 for _ in range(10)] for _ in range(10)]
N=[[0 for _ in range(10)] for _ in range(10)]
for i in range(9):
    for j in range(9):
        if not a[i][j]:
            v.append((i,j))
        else:
            X[i][a[i][j]]=1
            Y[j][a[i][j]]=1
            num=((i//3)*3)+(j//3)
            N[num][a[i][j]]=1
def go(cnt):
    global f
    if f:
        return
    if cnt==len(v):
        for i in range(9):
            for j in range(9):
                print(a[i][j],end='')
            print('')
        f=1
        return
    x,y=v[cnt]
    for i in range(1,10):
        num=((x//3)*3)+(y//3)
        if not X[x][i] and not Y[y][i] and not N[num][i]:
            a[x][y]=i
            X[x][i]=1
            Y[y][i]=1
            N[num][i]=1
            go(cnt+1)
            a[x][y]=0
            N[num][i] = 0
            X[x][i] = 0
            Y[y][i] = 0
go(0)