d=[[-1 for _ in range(101)] for _ in range(101)]
a=[[0 for _ in range(101)] for _ in range(101)]
def g(x,y,n,m):
    if x>=n or y>=m or a[x][y]:
        return 0
    if x==n-1 and y==m-1:
        return 1
    if d[x][y]!=-1:
        return d[x][y]
    ret=0
    ret+=(g(x+1,y,n,m)+g(x,y+1,n,m))%(int(1e9)+7)
    d[x][y]=ret
    return d[x][y]
def solution(m, n, puddles):
    for cur in puddles:
        a[cur[1]-1][cur[0]-1]=1
    return g(0,0,n,m)