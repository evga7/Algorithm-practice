import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N=int(input())
w=[]
b=[]
res=0
g=[[] for _ in range(N+1)]
for i in range(N):
    z,x=map(int,input().split())
    g[x].append(z)
for i in range(1,N+1):
    g[i].sort()
    for j in range(len(g[i])):
        s=987654321
        if j-1>=0:
            s=min(s,g[i][j]-g[i][j-1])
        if j+1<len(g[i]):
            s=min(s,g[i][j+1]-g[i][j])
        res+=s
print(res)