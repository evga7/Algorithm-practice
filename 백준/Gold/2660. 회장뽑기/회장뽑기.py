import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
N=int(input())
p=[[MAX for _ in range(N+1)] for _ in range(N+1)]
while True:
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        break
    p[a][b]=1
    p[b][a]=1
for i in range(1,N+1):
    p[i][i]=0
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if p[i][j]==1:continue
            if p[i][j]>p[i][k]+p[k][j]:
                p[i][j]=p[i][k]+p[k][j]
v=[]
m=MAX
for i in range(1,N+1):
    c=max(p[i][1:])
    if m>=c:
        if m>c:
            v.clear()
        m=c
        v.append(i)
print(m,len(v))
print(*v)