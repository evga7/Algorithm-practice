import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
a=[list(input()) for _ in range(N)]
chk=[[] for _ in range(M)]
T=int(input())
def go(x,y,sy):
    while x+1<N:
        chk[sy].append((x,y))
        if x+1<N and a[x+1][y]=='.':
            x+=1
        elif x+1<N and a[x+1][y]=='X':
            break
        elif x+1<N and a[x+1][y]=='O':
            if x+1<N and y-1>=0 and a[x][y-1]=='.' and a[x+1][y-1]=='.':
                x+=1
                y-=1
            elif x+1<N and y+1<M and a[x][y+1]=='.' and a[x+1][y+1]=='.':
                x+=1
                y+=1
            else:
                break
    if a[x][y]=='.':
        a[x][y]='O'
for i in range(T):
    x=0
    sy=int(input())-1
    y=sy
    while chk[sy]:
        x,y=chk[sy][-1]
        if a[x][y]=='.':
            break
        chk[sy].pop()
    go(x,y,sy)
for i in range(N):
    for j in range(M):
        print(a[i][j],end='')
    print('')
    