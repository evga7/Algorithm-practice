import math
import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=[list(map(float,input().split())) for _ in range(N)]
p=[i for i in range(N+1)]
def find(x):
    if x==p[x]:
        return x
    p[x]=find(p[x])
    return p[x]
def uni(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        if x<y:
            p[y]=x
        else:
            p[x]=y
        return True
    return False
v=[]
def cal(x1,y1,x2,y2):
    return math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
for i in range(N):
    for j in range(i+1,N):
        x1,y1,x2,y2=a[i][0],a[i][1],a[j][0],a[j][1]
        v.append((cal(x1,y1,x2,y2),i+1,j+1))
res=0
v.sort()
for cur in v:
    cost,x,y=cur[0],cur[1],cur[2]
    if uni(x,y):
        res+=cost
print('%.2f'%res)