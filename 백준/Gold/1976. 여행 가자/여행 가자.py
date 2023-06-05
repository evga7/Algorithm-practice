import sys
def input():return sys.stdin.readline().rstrip()
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
        p[y]=x

for i in range(N):
    a=list(map(int,input().split()))
    for j,cur in enumerate(a):
        if cur:
            uni(i+1,j+1)
b=list(map(int,input().split()))
r=p[b[0]]
for i in range(1,len(b)):
    if r!=find(b[i]):
        print("NO")
        exit(0)
print("YES")