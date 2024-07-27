import sys
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
v=[[0 for _ in range(M+1)] for _ in range(N+1)]
def chk(num,x,y,op):
    s=a[x][y]*2
    if num==0:
        if x+1<N and y-1>=0:
            if op:
                if not v[x+1][y] and not v[x][y-1]:
                    v[x][y],v[x+1][y],v[x][y-1]=op,op,op
                    return s + a[x + 1][y] + a[x][y - 1]
            else:
                v[x][y], v[x + 1][y], v[x][y - 1] = op, op, op
        return -1
    if num==1:
        if x-1>=0 and y-1>=0:
            if op:
                if not v[x-1][y] and not v[x][y-1]:
                    v[x][y],v[x-1][y],v[x][y-1]=op,op,op
                    return s + a[x - 1][y] + a[x][y - 1]
            else:
                v[x][y], v[x - 1][y], v[x][y - 1] = op, op, op
        return -1
    if num==2:
        if x-1>=0 and y+1<M:
            if op:
                if not v[x-1][y] and not v[x][y+1]:
                    v[x][y],v[x-1][y],v[x][y+1]=op,op,op
                    return s + a[x - 1][y] + a[x][y + 1]
            else:
                v[x][y], v[x - 1][y], v[x][y + 1] = op, op, op
        return -1
    if num==3:
        if x+1<N and y+1<M:
            if op:
                if not v[x+1][y] and not v[x][y+1]:
                    v[x][y],v[x+1][y],v[x][y+1]=op,op,op
                    return s + a[x + 1][y] + a[x][y + 1]
            else:
                v[x][y], v[x + 1][y], v[x][y + 1] = op, op, op
        return -1

res=0
def go(x,score):
    global res
    res=max(res,score)
    for i in range(x,N):
        for j in range(M):
            for k in range(4):
                if v[i][j]:continue
                s=chk(k,i,j,1)
                if s!=-1:
                    go(i,score+s)
                    chk(k,i,j,0)

go(0,0)
print(res)