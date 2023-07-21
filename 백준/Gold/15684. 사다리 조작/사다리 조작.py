import sys
def input(): return sys.stdin.readline().rstrip()
M,T,N=map(int,input().split())
arr=[[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(T):
    a,b=map(int,input().split())
    arr[a][b]=1
res=4
def chk():
    for i in range(1,M+1):
        x,y=1,i
        while x<=N:
            if arr[x][y] and y+1<=M:
                y+=1
            elif y-1>=0 and arr[x][y-1]:
                y-=1
            x+=1
        if y!=i:
            return False
    return True

def go(x,y,cnt):
    if chk():
        global res
        res=min(res,cnt)
        return
    if cnt>=3:
        return
    for i in range(x,N+1):
        for j in range(y,M+1):
            if not arr[i][j] and j+1<=M and not arr[i][j+1]:
                arr[i][j]=1
                go(i,j+2,cnt+1)
                arr[i][j]=0
        y=1
go(1,1,0)
if res>3:
    res=-1
print(res)