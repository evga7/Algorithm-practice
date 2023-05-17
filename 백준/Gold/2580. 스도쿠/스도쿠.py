import sys
def input():return sys.stdin.readline().rstrip()
a=[list(map(int,input().split())) for _ in range(9)]
row=[[0 for _ in range(10)] for _ in range(9)]
col=[[0 for _ in range(10)] for _ in range(9)]
idx=[[0 for _ in range(10)] for _ in range(9)]
def chk(x,y,k):
    if row[x][k]:
        return False
    if col[y][k]:
        return False
    cur = (x // 3) *3 + y // 3
    if idx[cur][k]:
        return False
    return True
def go2(x,y,k,op):
    cur = (x // 3) * 3 + y // 3
    if op:
        row[x][k]=1
        col[y][k]=1
        idx[cur][k]=1
    else:
        row[x][k]=0
        col[y][k]=0
        idx[cur][k]=0
cnt=0
v=[]
for i in range(9):
    for j in range(9):
        if not a[i][j]:
            cnt+=1
            v.append((i,j))
        else:
            cur = (i // 3) * 3 + j // 3
            k=a[i][j]
            row[i][k] = 1
            col[j][k] = 1
            idx[cur][k] = 1
def go(c):
    if c==len(v):
        for i in range(9):
            for j in range(9):
                print(a[i][j],end=' ')
            print('')
        exit(0)
    cur=v[c]
    i,j=cur[0],cur[1]
    for k in range(1,10):
        if chk(i,j,k):
            a[i][j]=k
            go2(i,j,k,1)
            go(c+1)
            a[i][j]=0
            go2(i, j, k, 0)
go(0)