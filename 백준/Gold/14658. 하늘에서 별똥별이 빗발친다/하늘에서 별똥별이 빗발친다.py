import sys
def input():return sys.stdin.readline().rstrip()
N,M,L,K=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(K)]
def go(x,y):
    lux,luy=max(0,x-L),max(0,y-L)
    rux, ruy = max(0, x - L), min(M, y + L)
    ldx,ldy=min(N,x+L),max(0,y-L)
    rdx,rdy=min(N,x+L),min(M,y+L)
    lu_cnt = 0
    ru_cnt = 0
    ld_cnt = 0
    rd_cnt = 0
    for cur in a:
        xx,yy=cur[0],cur[1]
        if lux<=xx<=x and luy<=yy<=y:
            lu_cnt+=1
        if x<=xx<=rux and ruy<=yy<=y:
            ru_cnt+=1
        if x<=xx<=ldx and ldy<=yy<=y:
            ld_cnt+=1
        if x<=xx<=rdx and y<=yy<=rdy:
            rd_cnt+=1
    return max(lu_cnt,ru_cnt,ld_cnt,rd_cnt)
res=0
for cur in a:
    for cur2 in a:
        res=max(res,go(cur[0],cur2[1]))
print(K-res)