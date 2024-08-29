import itertools
import math
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
N,M=map(int,input().split())
st=set()
p=[i for i in range(N+1)]
v=[]
def find(x):
    if p[x]==x:
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
b=[list(map(int,input().split())) for _ in range(M)]
a=[list(map(int,input().split())) for _ in range(N)]
for x,y in b:
    uni(x,y)
res,res2=0,0
res_v=[]
for i in range(1,N):
    for j in range(i+1,N):
        v.append((a[i][j],i+1,j+1))
v.sort()
for cost,x,y in v:
    if uni(x,y):
        res+=cost
        res2+=1
        res_v.append(x)
        res_v.append(y)
print(res,res2)
if res_v:
    print(*res_v)
