import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
g=[[0 for _ in range(3)] for _ in range(N+1)]
v=[0 for _ in range(N+1)]
for i in range(N):
    a,b,c=map(int,input().split())
    g[a][0]=b
    g[a][1]=c
    if b!=-1:
        g[b][2]=a
    if c!=-1:
        g[c][2]=a
res=0
def f(x):
    if g[x][1]==-1:
        return x
    return f(g[x][1])
flag=0
def go(cur):
    global res,flag
    left=g[cur][0]
    right=g[cur][1]
    if left!=-1:
        res+=1
        go(left)
        if not flag:
            res+=1
    if right!=-1:
        res+=1
        go(right)
        if not flag:
            res+=1
    if cur==idx:
        flag=1
idx=f(1)
go(1)
print(res)