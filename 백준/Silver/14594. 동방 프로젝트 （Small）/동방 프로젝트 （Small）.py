from collections import *
import bisect
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
m=defaultdict(int)
N=int(input())
M=int(input())
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

for i in range(M):
    a,b=map(int,input().split())
    for j in range(a+1,b+1):
        uni(a,j)
num=find(1)
res=1
st=set()
for i in range(1,N+1):
    st.add(find(i))
print(len(st))