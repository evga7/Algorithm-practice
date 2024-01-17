import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M,K=map(int,input().split())
visited=[0 for _ in range(N+1)]
a=[]
b=[]
def go(cnt):
    if cnt==M:
        b.append(a[:])
        return
    for i in range(N):
        if visited[i]:continue
        visited[i]=1
        a.append(i)
        go(cnt+1)
        visited[i]=0
        a.pop()
go(0)
res=0
for cur in b:
    st=set(cur)
    cnt=0
    for i in range(M):
        if i in st:
            cnt+=1
    if cnt>=K:
        res+=1
print(res/len(b))