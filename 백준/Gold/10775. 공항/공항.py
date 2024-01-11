import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
M=int(input())
res=0
p=[i for i in range(100001)]
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

for i in range(1,M+1):
    num=int(input())
    x=find(num)
    if x==0:
        break
    if uni(x,x-1):
        res+=1
        
print(res)