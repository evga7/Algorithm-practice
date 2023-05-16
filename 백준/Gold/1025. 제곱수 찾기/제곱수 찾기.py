import math
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
res=-1
a=[list(input()) for _ in range(N)]
def go(x,y,xx,yy,num,op):
    num1=int(num)
    num2=int(num[::-1])
    sq=math.sqrt(num1)
    sq2=math.sqrt(num2)
    global res
    if sq*sq==int(sq)*int(sq):
        res=max(res,num1)
    if sq2*sq2==int(sq2)*int(sq2):
        res=max(res,num2)
    if not is_inside(x,y,N,M):
        return
    if len(num)>=max(N,M):
        return
    if not op:
        go(x+xx,y+yy,xx,yy,num+a[x][y],op)
    else:
        go(x+xx,y-yy,xx,yy,num+a[x][y],op)
for i in range(N):
    for j in range(M):
        sq=math.sqrt(int(a[i][j]))
        if sq * sq == int(sq) * int(sq):
            res = max(res, int(a[i][j]))
        for k in range(N):
            for l in range(M):
                if k==0 and l==0:continue
                go(i+k,j+l,k,l,a[i][j],0)
                go(i + k, j - l, k, l, a[i][j],1)
print(res)