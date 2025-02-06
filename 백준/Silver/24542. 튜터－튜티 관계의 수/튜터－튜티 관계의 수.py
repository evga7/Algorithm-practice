from collections import *
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
#dx = [0, 0, 1, -1]
#dy = [1, -1, 0, 0]
dx=[1,1,1]
dy=[-1,0,1]
N,M=map(int,input().split())
p=[i for i in range(N+1)]
def find(x):
    if x==p[x]:
        return x
    p[x]=find(p[x])
    return p[x]
def uni(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if a<b:
            p[b]=a
        else:
            p[a]=b
        return True
    return False
for i in range(M):
    a,b=map(int,input().split())
    uni(a,b)
st=set()
m=defaultdict(int)
for i in range(1,N+1):
    m[find(i)]+=1
res=1
for cur in m.keys():
    res*=m[cur]%(int(1e9)+7)
print(res%(int(1e9)+7))


