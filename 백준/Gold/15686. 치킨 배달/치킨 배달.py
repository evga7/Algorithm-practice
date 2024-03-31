import sys
def input():
    return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
c=[]
h=[]
v=[]
res=987654321
def chk():
    c=0
    for nxt in h:
        cc=987654321
        hx, hy = nxt[0], nxt[1]
        for cur in v:
            cx,cy=cur[0],cur[1]
            cc = min(abs(cx - hx) + abs(cy - hy), cc)
        c+=cc
    return c

def go(idx,cnt):
    if cnt==M:
        global res
        res=min(res,chk())
        return
    for i in range(idx,len(c)):
        v.append(c[i])
        go(i+1,cnt+1)
        v.pop()

for i in range(N):
    for j in range(N):
        if a[i][j]==2:
            c.append((i,j))
        elif a[i][j]==1:
            h.append((i,j))
go(0,0)
print(res)
